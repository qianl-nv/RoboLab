# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generate HTML and Markdown scene catalogs for RoboLab benchmark tasks."""

from __future__ import annotations

import ast
import html
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCENE_META_PATH = ROOT / "assets/scenes/_metadata/scene_metadata.json"
TASK_META_PATH = ROOT / "robolab/tasks/_metadata/task_metadata.json"
SCENES_DIR = ROOT / "assets/scenes"
IMAGES_DIR = SCENES_DIR / "_images"
METADATA_DIR = SCENES_DIR / "_metadata"
BENCHMARK_DIR = ROOT / "robolab/tasks/benchmark"

STATIC_INFRA = {
    "Looks", "PhysicsScene", "PhysicsMaterial", "GroundPlane", "franka_table",
    "world_camera", "white_void", "PushGraph", "table",
}


@dataclass(frozen=True)
class CatalogSpec:
    key: str
    out_name: str
    page_title: str
    heading: str
    filter_description: str
    filter_description_md: str

    @property
    def md_out_name(self) -> str:
        return Path(self.out_name).with_suffix(".md").name


CATALOGS = (
    CatalogSpec(
        key="atomic",
        out_name="pnp_atomic_scene_catalog.html",
        page_title="RoboLab Scene Catalog — Single-Object Pick &amp; Place",
        heading="RoboLab PnP Atomic Scene Catalog",
        filter_description=(
            "Filter: exactly one <code>pick_and_place</code> or "
            "<code>pick_and_place_on_surface</code> subtask with a single object."
        ),
        filter_description_md=(
            "Filter: exactly one `pick_and_place` or `pick_and_place_on_surface` "
            "subtask with a single object."
        ),
    ),
    CatalogSpec(
        key="multi",
        out_name="pnp_multi_scene_catalog.html",
        page_title="RoboLab Scene Catalog — Multi-Target Pick &amp; Place",
        heading="RoboLab PnP Multi Scene Catalog",
        filter_description=(
            "Filter: <code>pick_and_place</code> or <code>pick_and_place_on_surface</code> "
            "with multiple objects and/or multiple subtasks."
        ),
        filter_description_md=(
            "Filter: `pick_and_place` or `pick_and_place_on_surface` with multiple objects "
            "and/or multiple subtasks."
        ),
    ),
    CatalogSpec(
        key="other",
        out_name="other_scene_catalog.html",
        page_title="RoboLab Scene Catalog — Other Tasks",
        heading="RoboLab Other Scene Catalog",
        filter_description=(
            "Filter: benchmark tasks without <code>pick_and_place</code> / "
            "<code>pick_and_place_on_surface</code> (stacking, reorientation, spatial, etc.)."
        ),
        filter_description_md=(
            "Filter: benchmark tasks without `pick_and_place` / `pick_and_place_on_surface` "
            "(stacking, reorientation, spatial, etc.)."
        ),
    ),
)


def get_table_payloads(prims: list) -> list[str]:
    """Return USD payload path(s) for the table prim in a scene."""
    if not isinstance(prims, list):
        return []
    for p in prims:
        if p.get("name") == "table":
            return list(p.get("payload") or [])
    return []


def format_table_payload(prims: list) -> str:
    payloads = get_table_payloads(prims)
    if not payloads:
        return '<code>""</code>'
    if len(payloads) == 1:
        return f"<code>{html.escape(payloads[0])}</code>"
    items = "".join(f"<li><code>{html.escape(pl)}</code></li>" for pl in payloads)
    return f"<ul>{items}</ul>"


def extract_call_args(src: str, func_name: str) -> list[tuple[str, dict]]:
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    results = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.id if isinstance(fn, ast.Name) else (fn.attr if isinstance(fn, ast.Attribute) else None)
        if name != func_name:
            continue
        kwargs: dict = {}
        for kw in node.keywords:
            if kw.arg is None:
                continue
            try:
                kwargs[kw.arg] = ast.literal_eval(kw.value)
            except (ValueError, TypeError):
                kwargs[kw.arg] = None
        if node.args:
            try:
                kwargs.setdefault("object", ast.literal_eval(node.args[0]))
            except (ValueError, TypeError):
                pass
        results.append((func_name, kwargs))
    return results


def object_count(obj_param) -> int | None:
    if isinstance(obj_param, str):
        return 1
    if isinstance(obj_param, list):
        return len(obj_param)
    return None


def humanize(name: str) -> str:
    return name.replace("_", " ")


def pnp_calls_from_src(src: str) -> list[tuple[str, dict]]:
    return extract_call_args(src, "pick_and_place") + extract_call_args(src, "pick_and_place_on_surface")


def classify_pnp_category(calls: list[tuple[str, dict]]) -> str:
    """Return 'atomic', 'multi', or 'other'."""
    if not calls:
        return "other"
    if len(calls) == 1 and object_count(calls[0][1].get("object")) == 1:
        return "atomic"
    return "multi"


def objects_from_param(obj_param) -> list[str]:
    if isinstance(obj_param, str):
        return [obj_param]
    if isinstance(obj_param, list):
        return list(obj_param)
    return []


def placement_phrase(func_name: str, args: dict) -> str:
    objects = objects_from_param(args.get("object"))
    on_surface = func_name == "pick_and_place_on_surface"
    target = args.get("surface") if on_surface else args.get("container")
    target_h = humanize(str(target))
    if len(objects) == 1:
        picked_h = humanize(objects[0])
        if on_surface and target == "table":
            return f"place the {picked_h} on the table"
        prep = "on" if on_surface else "into"
        return f"place the {picked_h} {prep} the {target_h} on the table"
    picked_h = ", ".join(humanize(o) for o in objects)
    if on_surface and target == "table":
        return f"place {picked_h} on the table"
    prep = "on" if on_surface else "into"
    return f"place {picked_h} {prep} the {target_h} on the table"


def involved_entities(calls: list[tuple[str, dict]]) -> set[str]:
    involved: set[str] = {"table"}
    for func_name, args in calls:
        involved.update(objects_from_param(args.get("object")))
        on_surface = func_name == "pick_and_place_on_surface"
        target = args.get("surface") if on_surface else args.get("container")
        if isinstance(target, str):
            involved.add(target)
    return involved


def append_distractors(prompt: str, contact_objects: list[str], exclude: set[str]) -> str:
    distractors = [humanize(o) for o in contact_objects if o not in exclude]
    if not distractors:
        return prompt
    shown = distractors[:8]
    extra = len(distractors) - len(shown)
    tail = f", and {extra} more" if extra > 0 else ""
    return f"{prompt}. Other objects on the table as distractors: {', '.join(shown)}{tail}"


def build_atomic_arena_prompt(
    instruction: str,
    picked: str,
    target: str,
    on_surface: bool,
    contact_objects: list[str],
) -> str:
    picked_h = humanize(picked)
    target_h = humanize(target)
    if on_surface and target == "table":
        placement = f"place the {picked_h} on the table"
    else:
        prep = "on" if on_surface else "into"
        placement = f"place the {picked_h} {prep} the {target_h} on the table"
    instr = instruction.rstrip(".")
    prompt = f"droid {instr}. Using maple table background: {placement}"
    return append_distractors(prompt, contact_objects, {picked, target, "table"})


def build_multi_arena_prompt(
    instruction: str,
    calls: list[tuple[str, dict]],
    contact_objects: list[str],
) -> str:
    instr = instruction.rstrip(".")
    placements = "; ".join(placement_phrase(func_name, args) for func_name, args in calls)
    prompt = f"droid {instr}. Using maple table background: {placements}"
    return append_distractors(prompt, contact_objects, involved_entities(calls))


def build_generic_arena_prompt(instruction: str, contact_objects: list[str]) -> str:
    instr = instruction.rstrip(".")
    prompt = f"droid {instr}. Using maple table background."
    return append_distractors(prompt, contact_objects, {"table"})


def parse_benchmark_task(tf: Path, task_meta: dict) -> dict | None:
    src = tf.read_text()
    scene_m = re.search(r'import_scene\("([^"]+)"', src)
    class_m = re.search(r'class\s+(\w+Task)\s*\(', src)
    col_m = re.search(r'contact_object_list\s*=\s*(\[[^\]]+\])', src, re.DOTALL)
    if not scene_m or not class_m or not col_m:
        return None

    calls = pnp_calls_from_src(src)
    category = classify_pnp_category(calls)
    contact = ast.literal_eval(col_m.group(1))
    task_name = class_m.group(1)
    meta = task_meta.get(task_name, {})
    instruction = meta.get("instruction") or (meta.get("instruction_variants") or {}).get("default", "")
    filename = meta.get("filename") or f"benchmark/{tf.name}"

    if category == "atomic":
        func_name, args = calls[0]
        obj = args.get("object")
        picked = obj[0] if isinstance(obj, list) else obj
        on_surface = func_name == "pick_and_place_on_surface"
        target = args.get("surface") if on_surface else args.get("container")
        prompt = build_atomic_arena_prompt(instruction, picked, target, on_surface, contact)
    elif category == "multi":
        prompt = build_multi_arena_prompt(instruction, calls, contact)
    else:
        prompt = build_generic_arena_prompt(instruction, contact)

    return {
        "task_name": task_name,
        "file": f"robolab/tasks/{filename}",
        "instruction": instruction,
        "scene": scene_m.group(1),
        "category": category,
        "contact_objects": contact,
        "prompt": prompt,
    }


def count_scene_objects(prims: list) -> int:
    """Count scene object prims with payloads, excluding table and static infrastructure."""
    if not isinstance(prims, list):
        return 0
    return sum(
        1
        for p in prims
        if p.get("name") not in STATIC_INFRA and (p.get("payload") or [])
    )


def build_payloads(prims: list) -> str:
    rows = []
    for p in prims:
        name = p.get("name", "?")
        if name in STATIC_INFRA:
            continue
        payloads = p.get("payload") or []
        if not payloads:
            continue
        for pl in payloads:
            rows.append(f"<li><code>{html.escape(name)}</code> → <code>{html.escape(pl)}</code></li>")
    if not rows:
        return "<em>No payloads listed.</em>"
    return "<ul>" + "".join(rows) + "</ul>"


def build_task_list(tasks: list[dict]) -> str:
    items = []
    for t in sorted(tasks, key=lambda x: x["task_name"]):
        items.append(
            "<li>"
            f"<strong>{html.escape(t['task_name'])}</strong><br>"
            f"<code>{html.escape(t['file'])}</code><br>"
            f"{html.escape(t['instruction'])}"
            "</li>"
        )
    return f"<ul>{''.join(items)}</ul><p><em>{len(tasks)} task(s)</em></p>"


def build_prompt_list(tasks: list[dict]) -> str:
    items = []
    for t in sorted(tasks, key=lambda x: x["task_name"]):
        items.append(
            "<li>"
            f"<strong>{html.escape(t['task_name'])}</strong>"
            f"<div class=\"prompt-text\">{html.escape(t['prompt'])}</div>"
            "</li>"
        )
    return f"<ul>{''.join(items)}</ul>"


def scene_image_rel(scene_file: str) -> str | None:
    stem = Path(scene_file).stem
    if (IMAGES_DIR / f"{stem}.png").is_file():
        return f"../_images/{stem}.png"
    return None


def build_catalog_table_rows(
    scenes: list[str],
    tasks_by_scene: dict[str, list[dict]],
    scene_meta: dict,
) -> list[str]:
    rows = []
    for scene_file in scenes:
        prims = scene_meta.get(scene_file, [])
        prims_list = prims if isinstance(prims, list) else []
        num_objects = count_scene_objects(prims_list)
        img_rel = scene_image_rel(scene_file)
        img_cell = (
            f'<img src="{html.escape(img_rel)}" alt="{html.escape(scene_file)}" width="180" />'
            if img_rel else "<em>No snapshot available</em>"
        )
        rows.append(
            "<tr>"
            f'<td valign="top"><code>{html.escape(scene_file)}</code></td>'
            f'<td valign="top">{img_cell}</td>'
            f'<td valign="top" align="center">{num_objects}</td>'
            f'<td valign="top">{format_table_payload(prims_list)}</td>'
            f'<td valign="top">{build_payloads(prims_list)}</td>'
            f'<td valign="top">{build_task_list(tasks_by_scene[scene_file])}</td>'
            f'<td valign="top">{build_prompt_list(tasks_by_scene[scene_file])}</td>'
            "</tr>"
        )
    return rows


CATALOG_TABLE_HEAD = """
<thead>
  <tr>
    <th>Scene (.usda)</th>
    <th>Snapshot</th>
    <th>Objects</th>
    <th>Table payload</th>
    <th>Object payloads</th>
    <th>Benchmark tasks</th>
    <th>Arena env prompt</th>
  </tr>
</thead>
"""


def wrap_catalog_table(rows: list[str]) -> str:
    """HTML table for GitHub markdown preview (pipe tables cannot fit this layout)."""
    return (
        '<table border="1" cellpadding="8" cellspacing="0" width="100%">'
        f"{CATALOG_TABLE_HEAD}<tbody>{''.join(rows)}</tbody></table>"
    )


def load_task_meta() -> dict[str, dict]:
    return {
        t["task_name"]: t
        for t in json.loads(TASK_META_PATH.read_text())
        if t.get("filename", "").startswith("benchmark/")
    }


def collect_catalog_data(category: str) -> tuple[list[str], dict[str, list], dict, int]:
    """Return (sorted_scenes, tasks_by_scene, scene_meta, task_count) for one category."""
    scene_meta = json.loads(SCENE_META_PATH.read_text())
    task_meta = load_task_meta()

    tasks_by_scene: dict[str, list[dict]] = defaultdict(list)
    for tf in sorted(BENCHMARK_DIR.glob("*.py")):
        if tf.name == "__init__.py":
            continue
        info = parse_benchmark_task(tf, task_meta)
        if info and info["category"] == category:
            tasks_by_scene[info["scene"]].append(info)

    scenes = sorted(
        tasks_by_scene.keys(),
        key=lambda s: (
            count_scene_objects(scene_meta.get(s, [])),
            s,
        ),
    )
    task_count = sum(len(v) for v in tasks_by_scene.values())
    return scenes, dict(tasks_by_scene), scene_meta, task_count


HTML_STYLE = """
    :root {
      color-scheme: light dark;
      --border: #ccc;
      --muted: #666;
      --bg: #fff;
      --header-bg: #f5f5f5;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --border: #444;
        --muted: #aaa;
        --bg: #1a1a1a;
        --header-bg: #2a2a2a;
      }
    }
    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
      margin: 1.5rem;
      background: var(--bg);
      line-height: 1.45;
    }
    h1 { margin-bottom: 0.25rem; }
    .subtitle { color: var(--muted); margin-bottom: 1.5rem; max-width: 56rem; }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
    }
    th, td {
      border: 1px solid var(--border);
      padding: 0.75rem;
      vertical-align: top;
    }
    th {
      background: var(--header-bg);
      text-align: left;
      position: sticky;
      top: 0;
      z-index: 1;
    }
    .scene-name { width: 10rem; word-break: break-word; }
    .snapshot { width: 200px; }
    .object-count { width: 4rem; text-align: center; }
    .table-payload { width: 12%; }
    .snapshot img {
      max-width: 180px;
      max-height: 140px;
      display: block;
      border-radius: 4px;
      border: 1px solid var(--border);
    }
    .payloads { width: 22%; }
    .tasks { width: 20%; }
    .prompts { width: 28%; }
    ul { margin: 0.25rem 0; padding-left: 1.2rem; }
    li { margin-bottom: 0.75rem; }
    code { font-size: 0.85em; word-break: break-all; }
    em { color: var(--muted); }
    .prompt-text {
      margin-top: 0.35rem;
      font-size: 0.88em;
      line-height: 1.4;
      white-space: pre-wrap;
    }
"""


def generate_catalog_html(spec: CatalogSpec) -> Path:
    scenes, tasks_by_scene, scene_meta, task_count = collect_catalog_data(spec.key)
    rows = build_catalog_table_rows(scenes, tasks_by_scene, scene_meta)

    out_path = METADATA_DIR / spec.out_name
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{spec.page_title}</title>
  <style>{HTML_STYLE}
  </style>
</head>
<body>
  <h1>{html.escape(spec.heading)}</h1>
  <p class="subtitle">
    {len(scenes)} benchmark scenes · {task_count} tasks<br>
    {spec.filter_description}<br>
    Prompts target <code>EnvironmentGenerationAgent.generate_spec()</code> with the DROID embodiment.
  </p>
  <table>
    {CATALOG_TABLE_HEAD}
    <tbody>
      {''.join(rows)}
    </tbody>
  </table>
</body>
</html>
"""
    out_path.write_text(content, encoding="utf-8")
    return out_path


def generate_catalog_markdown(spec: CatalogSpec) -> Path:
    scenes, tasks_by_scene, scene_meta, task_count = collect_catalog_data(spec.key)
    rows = build_catalog_table_rows(scenes, tasks_by_scene, scene_meta)

    parts = [
        f"# {spec.heading}",
        "",
        f"{len(scenes)} benchmark scenes · {task_count} tasks",
        "",
        spec.filter_description_md,
        "",
        "Prompts target `EnvironmentGenerationAgent.generate_spec()` with the DROID embodiment.",
        "",
        wrap_catalog_table(rows),
        "",
    ]

    out_path = METADATA_DIR / spec.md_out_name
    out_path.write_text("\n".join(parts), encoding="utf-8")
    return out_path


if __name__ == "__main__":
    for catalog in CATALOGS:
        html_path = generate_catalog_html(catalog)
        md_path = generate_catalog_markdown(catalog)
        scenes, _, _, task_count = collect_catalog_data(catalog.key)
        print(f"Wrote {html_path} ({len(scenes)} scenes, {task_count} tasks)")
        print(f"Wrote {md_path} ({md_path.stat().st_size / 1024:.1f} KB)")
