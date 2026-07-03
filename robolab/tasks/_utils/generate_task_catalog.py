# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generate a task catalog grouped by scene metadata.

The output is a Markdown table with one row per task. Scene-level columns are
repeated for each task so scenes with multiple tasks naturally span multiple
rows when sorted together.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
TASK_META_PATH = ROOT / "robolab/tasks/_metadata/task_metadata.json"
SCENE_META_PATH = ROOT / "assets/scenes/_metadata/scene_metadata.json"
DEFAULT_OUT_PATH = ROOT / "robolab/tasks/_metadata/task_catalog.md"
DEFAULT_IMAGE_BASE_URL = "https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images"

STATIC_INFRA = {
    "Looks",
    "PhysicsScene",
    "PhysicsMaterial",
    "GroundPlane",
    "franka_table",
    "world_camera",
    "white_void",
    "PushGraph",
    "table",
}


def markdown_cell(value: Any) -> str:
    """Escape a value for a GitHub Markdown pipe-table cell."""
    text = "" if value is None else str(value)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")


def count_scene_objects(prims: Any) -> int:
    """Count scene object prims with payloads, excluding table and static infrastructure."""
    if not isinstance(prims, list):
        return 0
    return sum(
        1
        for prim in prims
        if isinstance(prim, dict) and prim.get("name") not in STATIC_INFRA and (prim.get("payload") or [])
    )


def task_description(task: dict[str, Any]) -> str:
    """Return the task's default human-facing description."""
    instruction = task.get("instruction")
    if instruction:
        return str(instruction)
    variants = task.get("instruction_variants")
    if isinstance(variants, dict):
        return str(variants.get("default", ""))
    return ""


def scene_image_link(scene_name: str, image_base_url: str) -> str:
    """Return a Markdown link to the scene PNG using the repository blob URL format."""
    image_name = f"{Path(scene_name).stem}.png"
    return f"[{image_name}]({image_base_url.rstrip('/')}/{image_name})"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def build_rows(
    tasks: list[dict[str, Any]],
    scene_meta: dict[str, Any],
    image_base_url: str,
) -> list[list[str]]:
    rows: list[tuple[tuple[int, int, str, str], list[str]]] = []
    for task in tasks:
        scene_name = str(task.get("scene", ""))
        scene_object_count = count_scene_objects(scene_meta.get(scene_name, []))
        subtask_count = int(task.get("num_subtasks") or 0)
        task_name = str(task.get("task_name", ""))
        rows.append(
            (
                (scene_object_count, subtask_count, scene_name.lower(), task_name.lower()),
                [
                    scene_image_link(scene_name, image_base_url) if scene_name else "",
                    str(scene_object_count),
                    task_name,
                    task_description(task),
                    str(subtask_count),
                ],
            )
        )

    return [row for _, row in sorted(rows, key=lambda item: item[0])]


def render_catalog(rows: list[list[str]]) -> str:
    headers = [
        "scene image",
        "scene object count",
        "task name",
        "task description",
        "subtask counts",
    ]
    lines = [
        "# RoboLab Task Catalog",
        "",
        f"{len(rows)} task rows sorted by scene object count, then subtask count.",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    lines.extend("| " + " | ".join(markdown_cell(cell) for cell in row) + " |" for row in rows)
    lines.append("")
    return "\n".join(lines)


def generate_task_catalog(
    task_metadata_path: Path = TASK_META_PATH,
    scene_metadata_path: Path = SCENE_META_PATH,
    output_path: Path = DEFAULT_OUT_PATH,
    image_base_url: str = DEFAULT_IMAGE_BASE_URL,
) -> Path:
    tasks = load_json(task_metadata_path)
    scene_meta = load_json(scene_metadata_path)
    if not isinstance(tasks, list):
        raise ValueError(f"Expected a list in {task_metadata_path}")
    if not isinstance(scene_meta, dict):
        raise ValueError(f"Expected a mapping in {scene_metadata_path}")

    rows = build_rows(tasks, scene_meta, image_base_url)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_catalog(rows), encoding="utf-8")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate robolab/tasks/_metadata/task_catalog.md")
    parser.add_argument("--task-metadata", type=Path, default=TASK_META_PATH, help="Path to task_metadata.json")
    parser.add_argument("--scene-metadata", type=Path, default=SCENE_META_PATH, help="Path to scene_metadata.json")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT_PATH, help="Path to write task_catalog.md")
    parser.add_argument(
        "--image-base-url",
        default=DEFAULT_IMAGE_BASE_URL,
        help="Base URL for scene image links",
    )
    args = parser.parse_args()

    output_path = generate_task_catalog(
        task_metadata_path=args.task_metadata,
        scene_metadata_path=args.scene_metadata,
        output_path=args.output,
        image_base_url=args.image_base_url,
    )
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
