# RoboLab PnP Atomic Scene Catalog

23 benchmark scenes · 35 tasks

Filter: exactly one `pick_and_place` or `pick_and_place_on_surface` subtask with a single object.

Prompts target `EnvironmentGenerationAgent.generate_spec()` with the DROID embodiment.

---

## banana_bowl.usda

![banana_bowl.usda](../_images/banana_bowl.png)

- **Objects:** 2
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `banana` → `../objects/ycb/banana.usd`

### Benchmark tasks

#### BananaInBowlTask

- **File:** `robolab/tasks/benchmark/banana_in_bowl_task.py`
- **Instruction:** Pick up the banana and place it in the bowl
- **Arena env prompt:** droid Pick up the banana and place it in the bowl. Using maple table background: place the banana into the bowl on the table

---

## butter_raisin_box.usda

![butter_raisin_box.usda](../_images/butter_raisin_box.png)

- **Objects:** 2
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `butter` → `../objects/hope/butter.usd`
- `raisin_box` → `../objects/hope/raisin_box.usd`

### Benchmark tasks

#### ButterAboveRaisinTask

- **File:** `robolab/tasks/benchmark/butter_above_raisin_task.py`
- **Instruction:** Pick up the butter box and place it on top of the raisin box
- **Arena env prompt:** droid Pick up the butter box and place it on top of the raisin box. Using maple table background: place the butter into the raisin box on the table

---

## mustard_raisin_box.usda

![mustard_raisin_box.usda](../_images/mustard_raisin_box.png)

- **Objects:** 2
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `raisin_box` → `../objects/hope/raisin_box.usd`
- `mustard_bottle` → `../objects/hope/mustard_bottle.usd`

### Benchmark tasks

#### MustardAboveRaisinTask

- **File:** `robolab/tasks/benchmark/mustard_above_raisin_task.py`
- **Instruction:** Place the mustard on the raisin box. 
- **Arena env prompt:** droid Place the mustard on the raisin box. . Using maple table background: place the mustard bottle into the raisin box on the table

---

## rubiks_cube_bowl.usda

![rubiks_cube_bowl.usda](../_images/rubiks_cube_bowl.png)

- **Objects:** 2
- **Table payload:** `../fixtures/table_maple.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `rubiks_cube` → `../objects/hot3d/rubiks_cube.usd`

### Benchmark tasks

#### RubiksCubeTask

- **File:** `robolab/tasks/benchmark/rubiks_cube_task.py`
- **Instruction:** Put the cube in the bowl
- **Arena env prompt:** droid Put the cube in the bowl. Using maple table background: place the rubiks cube into the bowl on the table

---

## butter_raisin_box_grey_bin.usda

![butter_raisin_box_grey_bin.usda](../_images/butter_raisin_box_grey_bin.png)

- **Objects:** 3
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `butter` → `../objects/hope/butter.usd`
- `raisin_box` → `../objects/hope/raisin_box.usd`
- `grey_bin` → `../fixtures/grey_bin.usd`

### Benchmark tasks

#### LargerObjectRaisinBoxInBinTask

- **File:** `robolab/tasks/benchmark/bigger_object.py`
- **Instruction:** Place the larger object in the grey bin.
- **Arena env prompt:** droid Place the larger object in the grey bin. Using maple table background: place the raisin box into the grey bin on the table. Other objects on the table as distractors: butter

#### SmallerObjectButterInBinTask

- **File:** `robolab/tasks/benchmark/smaller_object.py`
- **Instruction:** Place the smaller object in the grey bin.
- **Arena env prompt:** droid Place the smaller object in the grey bin. Using maple table background: place the butter into the grey bin on the table. Other objects on the table as distractors: raisin box

---

## two_bin.usda

![two_bin.usda](../_images/two_bin.png)

- **Objects:** 3
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `mustard` → `../objects/ycb/mustard.usd`
- `grey_bin_right` → `../fixtures/grey_bin.usd`
- `grey_bin_left` → `../fixtures/grey_bin.usd`

### Benchmark tasks

#### MustardInLeftBinTask

- **File:** `robolab/tasks/benchmark/mustard_in_left_bin.py`
- **Instruction:** Put the mustard in the left bin
- **Arena env prompt:** droid Put the mustard in the left bin. Using maple table background: place the mustard into the grey bin left on the table. Other objects on the table as distractors: grey bin right

#### MustardInRightBinTask

- **File:** `robolab/tasks/benchmark/mustard_in_right_bin.py`
- **Instruction:** Put the mustard in the right bin
- **Arena env prompt:** droid Put the mustard in the right bin. Using maple table background: place the mustard into the grey bin right on the table. Other objects on the table as distractors: grey bin left

---

## bottles_crate.usda

![bottles_crate.usda](../_images/bottles_crate.png)

- **Objects:** 4
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `salad_dressing_bottle` → `../objects/hope/ranch_dressing.usd`
- `ceramic_mug` → `../objects/hot3d/ceramic_mug.usd`
- `bbq_sauce_bottle` → `../objects/hot3d/bbq_sauce_bottle.usd`
- `purple_crate` → `https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/4.5/Isaac/Props/KLT_Bin/small_KLT_visual_collision.usd`

### Benchmark tasks

#### SauceBottlesCrateTask

- **File:** `robolab/tasks/benchmark/sauce_bottles_crate_task.py`
- **Instruction:** Put the red bbq sauce bottle in the crate
- **Arena env prompt:** droid Put the red bbq sauce bottle in the crate. Using maple table background: place the bbq sauce bottle into the purple crate on the table. Other objects on the table as distractors: ceramic mug, salad dressing bottle

---

## foodpacking_1bin_1box_1can.usda

![foodpacking_1bin_1box_1can.usda](../_images/foodpacking_1bin_1box_1can.png)

- **Objects:** 4
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `bin_a06` → `../objects/vomp/bin_a06/bin_a06.usd`
- `cheez_it` → `../objects/ycb/cheez_it.usd`
- `mustard` → `../objects/ycb/mustard.usd`
- `tomato_soup_can` → `../objects/ycb/tomato_soup_can.usd`

### Benchmark tasks

#### FoodPacking1BoxesTask

- **File:** `robolab/tasks/benchmark/foodpacking_1bin_1box.py`
- **Instruction:** Pack boxed foods into the bin
- **Arena env prompt:** droid Pack boxed foods into the bin. Using maple table background: place the cheez it into the bin a06 on the table. Other objects on the table as distractors: mustard, tomato soup can

#### FoodPacking1CansTask

- **File:** `robolab/tasks/benchmark/foodpacking_1bin_1can.py`
- **Instruction:** Pack canned foods into the bin
- **Arena env prompt:** droid Pack canned foods into the bin. Using maple table background: place the tomato soup can into the bin a06 on the table. Other objects on the table as distractors: cheez it, mustard

---

## bagel_plate_banana_bowl.usda

![bagel_plate_banana_bowl.usda](../_images/bagel_plate_banana_bowl.png)

- **Objects:** 5
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `plate_large` → `https://omniverse-content-staging.s3.us-west-2.amazonaws.com/Assets/simready_content/common_assets/props/plate_large/plate_large.usd`
- `banana` → `../objects/ycb/banana.usd`
- `bagel_00` → `../objects/objaverse/bagel_00.usd`
- `bagel_06` → `../objects/objaverse/bagel_06.usd`

### Benchmark tasks

#### BananaOnPlateTask

- **File:** `robolab/tasks/benchmark/banana_on_plate_task.py`
- **Instruction:** Pick up the banana and put it on the plate
- **Arena env prompt:** droid Pick up the banana and put it on the plate. Using maple table background: place the banana on the plate large on the table. Other objects on the table as distractors: bagel 00, bagel 06, bowl

---

## bin_mug_mustard_marker_bowl.usda

![bin_mug_mustard_marker_bowl.usda](../_images/bin_mug_mustard_marker_bowl.png)

- **Objects:** 5
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `grey_bin` → `../fixtures/grey_bin.usd`
- `mug` → `../objects/ycb/mug.usd`
- `bowl` → `../objects/ycb/bowl.usd`
- `mustard` → `../objects/ycb/mustard.usd`
- `dry_erase_marker` → `../objects/ycb/dry_erase_marker.usd`

### Benchmark tasks

#### BowlInBinTask

- **File:** `robolab/tasks/benchmark/bowl_in_bin_task.py`
- **Instruction:** put the bowl in the grey bin
- **Arena env prompt:** droid put the bowl in the grey bin. Using maple table background: place the bowl into the grey bin on the table. Other objects on the table as distractors: mustard, dry erase marker, mug

---

## shelf_mugs_jug_bowl.usda

![shelf_mugs_jug_bowl.usda](../_images/shelf_mugs_jug_bowl.png)

- **Objects:** 5
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `ceramic_mug` → `../objects/hot3d/ceramic_mug.usd`
- `mug` → `../objects/hot3d/mug.usd`
- `rack_l04` → `../objects/vomp/rack_l04/rack_l04.usd`
- `serving_bowl` → `../objects/vomp/serving_bowl/serving_bowl.usd`
- `utilityjug_a01` → `../objects/vomp/utilityjug_a01/utilityjug_a01.usd`

### Benchmark tasks

#### PutBowlOnShelfTopTask

- **File:** `robolab/tasks/benchmark/put_bowl_on_shelf.py`
- **Instruction:** Put the serving bowl anywhere on the shelf in front of you
- **Arena env prompt:** droid Put the serving bowl anywhere on the shelf in front of you. Using maple table background: place the serving bowl into the rack l04 on the table. Other objects on the table as distractors: ceramic mug, mug, utilityjug a01

---

## tools_container.usda

![tools_container.usda](../_images/tools_container.png)

- **Objects:** 6
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `cordless_drill` → `../objects/ycb/cordless_drill.usd`
- `spring_clamp` → `../objects/ycb/spring_clamp.usd`
- `red_hammer` → `../objects/handal/hammer_7.usd`
- `husky_hammer` → `../objects/handal/hammer_8.usd`
- `left_bin` → `../objects/vomp/container_f24/container_f24.usd`
- `right_bin` → `../objects/vomp/bin_b04/bin_b04.usd`

### Benchmark tasks

#### ClampInRightBinTask

- **File:** `robolab/tasks/benchmark/clamp_in_right_bin.py`
- **Instruction:** Put the spring clamp in the right bin
- **Arena env prompt:** droid Put the spring clamp in the right bin. Using maple table background: place the spring clamp into the right bin on the table. Other objects on the table as distractors: left bin, red hammer, husky hammer, cordless drill

---

## wire_shelf_mugs_plate_spatula.usda

![wire_shelf_mugs_plate_spatula.usda](../_images/wire_shelf_mugs_plate_spatula.png)

- **Objects:** 8
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `wireshelving_a01` → `../objects/vomp/wireshelving_a01/wireshelving_a01.usd`
- `spatula_01` → `../objects/vomp/spatula_01/spatula_01.usd`
- `plate_small` → `../objects/vomp/plate_small/plate_small.usd`
- `fork_big` → `../objects/vomp/fork_big/fork_big.usd`
- `fork_small` → `../objects/vomp/fork_small/fork_small.usd`
- `ceramic_mug` → `../objects/hot3d/ceramic_mug.usd`
- `mug` → `../objects/hot3d/mug.usd`
- `mug_01` → `../objects/ycb/mug.usd`

### Benchmark tasks

#### TakeSpatulaOffShelfTask

- **File:** `robolab/tasks/benchmark/take_spatula_off_shelf.py`
- **Instruction:** Take the spatula off the shelf and put it on the table
- **Arena env prompt:** droid Take the spatula off the shelf and put it on the table. Using maple table background: place the spatula 01 on the table. Other objects on the table as distractors: wireshelving a01, plate small, fork big, fork small, ceramic mug, mug, mug 01

---

## tools_picking.usda

![tools_picking.usda](../_images/tools_picking.png)

- **Objects:** 11
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `clamp` → `../objects/ycb/clamp.usd`
- `cordless_drill` → `../objects/ycb/cordless_drill.usd`
- `spring_clamp` → `../objects/ycb/spring_clamp.usd`
- `clamp_01` → `../objects/ycb/clamp.usd`
- `right_bin` → `../objects/vomp/bin_b03/bin_b03.usd`
- `center_bin` → `../objects/vomp/bin_b03/bin_b03.usd`
- `left_bin` → `../objects/vomp/bin_b03/bin_b03.usd`
- `husky_hammer` → `../objects/handal/hammer_1.usd`
- `wood_hammer` → `../objects/handal/hammer_2.usd`
- `red_hammer` → `../objects/handal/hammer_3.usd`
- `blue_hammer` → `../objects/handal/hammer_6.usd`

### Benchmark tasks

#### ToolsPickingDrillTask

- **File:** `robolab/tasks/benchmark/tools_picking_drill.py`
- **Instruction:** Select the cordless drill and put it on the table
- **Arena env prompt:** droid Select the cordless drill and put it on the table. Using maple table background: place the cordless drill on the table. Other objects on the table as distractors: clamp, spring clamp, husky hammer, blue hammer, red hammer, wood hammer, left bin, center bin, and 2 more

#### ToolsPickingHammerTask

- **File:** `robolab/tasks/benchmark/tools_picking_hammer.py`
- **Instruction:** Select the blue hammer and put it on the table
- **Arena env prompt:** droid Select the blue hammer and put it on the table. Using maple table background: place the blue hammer on the table. Other objects on the table as distractors: clamp, cordless drill, spring clamp, husky hammer, red hammer, wood hammer, left bin, center bin, and 2 more

---

## bin_condiments.usda

![bin_condiments.usda](../_images/bin_condiments.png)

- **Objects:** 12
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `grey_bin` → `../fixtures/grey_bin.usd`
- `mug` → `../objects/ycb/mug.usd`
- `mustard` → `../objects/ycb/mustard.usd`
- `bowl` → `../objects/ycb/bowl.usd`
- `ranch_dressing` → `../objects/hope/ranch_dressing.usd`
- `bbq_sauce_bottle` → `../objects/hope/bbq_sauce_bottle.usd`
- `oatmeal_raisin_cookies` → `../objects/hope/oatmeal_raisin_cookies.usd`
- `canned_tuna` → `../objects/hope/canned_tuna.usd`
- `soft_scrub` → `../objects/ycb/soft_scrub.usd`
- `wood_block` → `../objects/ycb/wood_block.usd`
- `coffee_pot` → `../objects/hot3d/coffee_pot.usd`
- `bbq_sauce_bottle_01` → `../objects/hot3d/bbq_sauce_bottle.usd`

### Benchmark tasks

#### CannedFoodInBinTask

- **File:** `robolab/tasks/benchmark/canned_food_in_bin_task.py`
- **Instruction:** Put the canned food in the grey bin
- **Arena env prompt:** droid Put the canned food in the grey bin. Using maple table background: place the canned tuna into the grey bin on the table. Other objects on the table as distractors: mug, mustard, bowl, ranch dressing, bbq sauce bottle, oatmeal raisin cookies, soft scrub, wood block, and 2 more

#### CoffeePotInBinTask

- **File:** `robolab/tasks/benchmark/coffee_pot_in_bin.py`
- **Instruction:** Put the coffee pot in the grey bin
- **Arena env prompt:** droid Put the coffee pot in the grey bin. Using maple table background: place the coffee pot into the grey bin on the table. Other objects on the table as distractors: mug, mustard, bowl, ranch dressing, bbq sauce bottle, oatmeal raisin cookies, canned tuna, soft scrub, and 2 more

---

## ladle_pot.usda

![ladle_pot.usda](../_images/ladle_pot.png)

- **Objects:** 13
- **Table payload:** ""

### Object payloads

- `anza_medium` → `../objects/vomp/anza_medium/anza_medium.usd`
- `ladle` → `../objects/handal/ladle.usd`
- `plate_large` → `../objects/vomp/plate_large/plate_large.usd`
- `plate_small` → `../objects/vomp/plate_small/plate_small.usd`
- `fork_big` → `../objects/vomp/fork_big/fork_big.usd`
- `fork_small` → `../objects/vomp/fork_small/fork_small.usd`
- `spatula_13` → `../objects/vomp/spatula_13/spatula_13.usd`
- `spatula_14` → `../objects/vomp/spatula_14/spatula_14.usd`
- `spatula_15` → `../objects/vomp/spatula_15/spatula_15.usd`
- `pink_spaghetti_spoon` → `../objects/handal/pink_spaghetti_spoon.usd`
- `ladle_01` → `../objects/handal/ladle.usd`
- `red_serving_spoon` → `../objects/handal/red_serving_spoon.usd`
- `green_serving_spoon` → `../objects/handal/green_serving_spoon.usd`

### Benchmark tasks

#### PinkSpoonInPotTask

- **File:** `robolab/tasks/benchmark/pink_spoon_in_pot.py`
- **Instruction:** Put the pink spaghetti spoon in the pot
- **Arena env prompt:** droid Put the pink spaghetti spoon in the pot. Using maple table background: place the pink spaghetti spoon into the anza medium on the table. Other objects on the table as distractors: ladle, plate large, plate small, fork big, fork small, spatula 13, spatula 14, spatula 15, and 3 more

---

## workdesk_bin.usda

![workdesk_bin.usda](../_images/workdesk_bin.png)

- **Objects:** 13
- **Table payload:** ""

### Object payloads

- `ceramic_mug` → `../objects/hot3d/ceramic_mug.usd`
- `glasses` → `../objects/hot3d/glasses.usd`
- `keyboard` → `../objects/hot3d/keyboard.usd`
- `lizard_figurine` → `../objects/hot3d/lizard_figurine.usd`
- `marker` → `../objects/ycb/dry_erase_marker.usd`
- `remote_control` → `../objects/hot3d/remote_control.usd`
- `smartphone` → `../objects/hot3d/smartphone.usd`
- `wooden_bowl` → `../objects/hot3d/wooden_bowl.usd`
- `spoon_big` → `../objects/vomp/spoon_big/spoon_big.usd`
- `computer_mouse` → `../objects/hot3d/computer_mouse.usd`
- `yogurt_cup` → `../objects/hope/yogurt_cup.usd`
- `granola_bars` → `../objects/hope/granola_bars.usd`
- `grey_bin` → `../fixtures/grey_bin.usd`

### Benchmark tasks

#### KeyboardOutOfBinTask

- **File:** `robolab/tasks/benchmark/keyboard_out_of_bin_task.py`
- **Instruction:** Take the keyboard out of the bin and put it on the table
- **Arena env prompt:** droid Take the keyboard out of the bin and put it on the table. Using maple table background: place the keyboard on the table. Other objects on the table as distractors: ceramic mug, glasses, lizard figurine, marker, remote control, smartphone, wooden bowl, spoon big, and 4 more

#### SmartphoneInBinTask

- **File:** `robolab/tasks/benchmark/smartphone_in_bin_task.py`
- **Instruction:** Put the smartphone in the grey bin
- **Arena env prompt:** droid Put the smartphone in the grey bin. Using maple table background: place the smartphone into the grey bin on the table. Other objects on the table as distractors: ceramic mug, glasses, keyboard, lizard figurine, marker, remote control, wooden bowl, spoon big, and 3 more

#### SpoonInMugTask

- **File:** `robolab/tasks/benchmark/spoon_in_mug_task.py`
- **Instruction:** Put the metal spoon that's in the wooden bowl in the mug
- **Arena env prompt:** droid Put the metal spoon that's in the wooden bowl in the mug. Using maple table background: place the spoon big into the ceramic mug on the table. Other objects on the table as distractors: glasses, keyboard, lizard figurine, marker, remote control, smartphone, wooden bowl, computer mouse, and 3 more

#### ToyInBinTask

- **File:** `robolab/tasks/benchmark/lizard_in_bin_task.py`
- **Instruction:** Put the lizard away in the bin
- **Arena env prompt:** droid Put the lizard away in the bin. Using maple table background: place the lizard figurine into the grey bin on the table. Other objects on the table as distractors: ceramic mug, glasses, keyboard, marker, remote control, smartphone, wooden bowl, spoon big, and 3 more

---

## workdesk_snacks.usda

![workdesk_snacks.usda](../_images/workdesk_snacks.png)

- **Objects:** 13
- **Table payload:** ""

### Object payloads

- `ceramic_mug` → `../objects/hot3d/ceramic_mug.usd`
- `glasses` → `../objects/hot3d/glasses.usd`
- `keyboard` → `../objects/hot3d/keyboard.usd`
- `marker` → `../objects/ycb/dry_erase_marker.usd`
- `remote_control` → `../objects/hot3d/remote_control.usd`
- `smartphone` → `../objects/hot3d/smartphone.usd`
- `wooden_bowl` → `../objects/hot3d/wooden_bowl.usd`
- `spoon_big` → `../objects/vomp/spoon_big/spoon_big.usd`
- `computer_mouse` → `../objects/hot3d/computer_mouse.usd`
- `yogurt_cup` → `../objects/hope/yogurt_cup.usd`
- `pitcher` → `../objects/hot3d/pitcher.usd`
- `plasticpail_a02` → `../objects/vomp/plasticpail_a02/plasticpail_a02.usd`
- `apple_01` → `../objects/objaverse/apple_01.usd`

### Benchmark tasks

#### ThrowAwayAppleTask

- **File:** `robolab/tasks/benchmark/throw_away_apple_task.py`
- **Instruction:** Throw away the apple
- **Arena env prompt:** droid Throw away the apple. Using maple table background: place the apple 01 into the plasticpail a02 on the table. Other objects on the table as distractors: ceramic mug, glasses, keyboard, marker, remote control, smartphone, wooden bowl, spoon big, and 3 more

---

## workdesk.usda

![workdesk.usda](../_images/workdesk.png)

- **Objects:** 14
- **Table payload:** ""

### Object payloads

- `ceramic_mug` → `../objects/hot3d/ceramic_mug.usd`
- `glasses` → `../objects/hot3d/glasses.usd`
- `keyboard` → `../objects/hot3d/keyboard.usd`
- `lizard_figurine` → `../objects/hot3d/lizard_figurine.usd`
- `marker` → `../objects/ycb/dry_erase_marker.usd`
- `remote_control` → `../objects/hot3d/remote_control.usd`
- `rubiks_cube` → `../objects/hot3d/rubiks_cube.usd`
- `smartphone` → `../objects/hot3d/smartphone.usd`
- `wooden_bowl` → `../objects/hot3d/wooden_bowl.usd`
- `spoon_big` → `../objects/vomp/spoon_big/spoon_big.usd`
- `computer_mouse` → `../objects/hot3d/computer_mouse.usd`
- `yogurt_cup` → `../objects/hope/yogurt_cup.usd`
- `oatmeal_raisin_cookies` → `../objects/hope/oatmeal_raisin_cookies.usd`
- `granola_bars` → `../objects/hope/granola_bars.usd`

### Benchmark tasks

#### MarkerInMugTask

- **File:** `robolab/tasks/benchmark/marker_in_mug_task.py`
- **Instruction:** Put the whiteboard marker in the mug
- **Arena env prompt:** droid Put the whiteboard marker in the mug. Using maple table background: place the marker into the ceramic mug on the table. Other objects on the table as distractors: glasses, keyboard, lizard figurine, remote control, rubiks cube, smartphone, wooden bowl, spoon big, and 4 more

#### MouseOnKeyboardTask

- **File:** `robolab/tasks/benchmark/mouse_on_keyboard.py`
- **Instruction:** Put the computer mouse on the keyboard
- **Arena env prompt:** droid Put the computer mouse on the keyboard. Using maple table background: place the computer mouse into the keyboard on the table. Other objects on the table as distractors: ceramic mug, glasses, lizard figurine, marker, remote control, rubiks cube, smartphone, wooden bowl, and 4 more

---

## cooking_table.usda

![cooking_table.usda](../_images/cooking_table.png)

- **Objects:** 15
- **Table payload:** ""

### Object payloads

- `redonion` → `../objects/fruits_veggies/red_onion.usd`
- `serving_bowl` → `../objects/vomp/serving_bowl/serving_bowl.usd`
- `clay_plates` → `../objects/hot3d/clay_plates.usd`
- `wooden_spoons` → `../objects/hot3d/wooden_spoons.usd`
- `spatula` → `../objects/hot3d/spatula.usd`
- `storage_box` → `../objects/hot3d/storage_box.usd`
- `tomato_sauce_can` → `../objects/hope/tomato_sauce_can.usd`
- `measuring_cups_1` → `../objects/handal/measuring_cups_1.usd`
- `pink_spaghetti_spoon` → `../objects/handal/pink_spaghetti_spoon.usd`
- `spoon_1` → `../objects/handal/spoon_1.usd`
- `green_serving_spoon` → `../objects/handal/green_serving_spoon.usd`
- `storage_box_01` → `../objects/hot3d/storage_box.usd`
- `ladle` → `../objects/handal/ladle.usd`
- `wooden_bowl` → `../objects/hot3d/wooden_bowl.usd`
- `potato_masher` → `../objects/hot3d/potato_masher.usd`

### Benchmark tasks

#### CookingPickPastaToolTask

- **File:** `robolab/tasks/benchmark/cooking_pick_pasta_tool.py`
- **Instruction:** Move the pink tool from this utensil container to the other utensil holder
- **Arena env prompt:** droid Move the pink tool from this utensil container to the other utensil holder. Using maple table background: place the pink spaghetti spoon into the storage box 01 on the table. Other objects on the table as distractors: redonion, serving bowl, clay plates, wooden spoons, spatula, storage box, tomato sauce can, measuring cups 1, and 5 more

---

## fruits_in_basket.usda

![fruits_in_basket.usda](../_images/fruits_in_basket.png)

- **Objects:** 16
- **Table payload:** ""

### Object payloads

- `lemon_01` → `../objects/fruits_veggies/lemon1.usd`
- `lemon_02` → `../objects/fruits_veggies/lemon2.usd`
- `lime01` → `../objects/fruits_veggies/lime.usd`
- `lime01_01` → `../objects/fruits_veggies/lime.usd`
- `orange_01` → `../objects/fruits_veggies/orange1.usd`
- `orange_02` → `../objects/fruits_veggies/orange2.usd`
- `pomegranate01` → `../objects/fruits_veggies/pomegranate.usd`
- `pumpkinlarge` → `../objects/vomp/pumpkinlarge/pumpkinlarge.usd`
- `pumpkinsmall` → `../objects/vomp/pumpkinsmall/pumpkinsmall.usd`
- `redonion` → `../objects/fruits_veggies/red_onion.usd`
- `serving_bowl` → `../objects/vomp/serving_bowl/serving_bowl.usd`
- `clay_plates` → `../objects/hot3d/clay_plates.usd`
- `wooden_bowl` → `../objects/hot3d/wooden_bowl.usd`
- `wooden_spoons` → `../objects/hot3d/wooden_spoons.usd`
- `spatula` → `../objects/hot3d/spatula.usd`
- `storage_box` → `../objects/hot3d/storage_box.usd`

### Benchmark tasks

#### FruitsOnionTask

- **File:** `robolab/tasks/benchmark/fruits_onion_to_bowl.py`
- **Instruction:** Put the onion in the wood bowl
- **Arena env prompt:** droid Put the onion in the wood bowl. Using maple table background: place the redonion into the wooden bowl on the table. Other objects on the table as distractors: lemon 01, lemon 02, lime01, lime01 01, orange 01, orange 02, pomegranate01, pumpkinlarge, and 6 more

#### FruitsOnionToPlateTask

- **File:** `robolab/tasks/benchmark/fruits_onion_to_plate.py`
- **Instruction:** Put the onion on the plate
- **Arena env prompt:** droid Put the onion on the plate. Using maple table background: place the redonion on the clay plates on the table. Other objects on the table as distractors: lemon 01, lemon 02, lime01, lime01 01, orange 01, orange 02, pomegranate01, pumpkinlarge, and 6 more

#### WoodSpatulaToBowlTask

- **File:** `robolab/tasks/benchmark/wood_spatula_to_bowl.py`
- **Instruction:** Put the wooden spatula in the bowl
- **Arena env prompt:** droid Put the wooden spatula in the bowl. Using maple table background: place the wooden spoons into the wooden bowl on the table. Other objects on the table as distractors: lemon 01, lemon 02, lime01, lime01 01, orange 01, orange 02, pomegranate01, pumpkinlarge, and 6 more

---

## clutter_fruit_bottle_bluebin.usda

![clutter_fruit_bottle_bluebin.usda](../_images/clutter_fruit_bottle_bluebin.png)

- **Objects:** 17
- **Table payload:** ""

### Object payloads

- `lemon_01` → `../objects/fruits_veggies/lemon1.usd`
- `lemon_02` → `../objects/fruits_veggies/lemon2.usd`
- `lime01` → `../objects/fruits_veggies/lime.usd`
- `lime01_01` → `../objects/fruits_veggies/lime.usd`
- `orange_01` → `../objects/fruits_veggies/orange1.usd`
- `orange_02` → `../objects/fruits_veggies/orange2.usd`
- `pomegranate01` → `../objects/fruits_veggies/pomegranate.usd`
- `pumpkinlarge` → `../objects/vomp/pumpkinlarge/pumpkinlarge.usd`
- `pumpkinsmall` → `../objects/vomp/pumpkinsmall/pumpkinsmall.usd`
- `whitepackerbottle_a01` → `../objects/vomp/whitepackerbottle_a01/whitepackerbottle_a01.usd`
- `avocado01` → `../objects/fruits_veggies/avocado.usd`
- `crabbypenholder` → `../objects/vomp/crabbypenholder/crabbypenholder.usd`
- `milkjug_a01` → `../objects/vomp/milkjug_a01/milkjug_a01.usd`
- `serving_bowl` → `../objects/vomp/serving_bowl/serving_bowl.usd`
- `utilityjug_a03` → `../objects/vomp/utilityjug_a03/utilityjug_a03.usd`
- `right_bin` → `../objects/vomp/container_f24/container_f24.usd`
- `red_onion` → `../objects/fruits_veggies/red_onion.usd`

### Benchmark tasks

#### BigPumpkinInBinTask

- **File:** `robolab/tasks/benchmark/clutter_big_pumpkin_task.py`
- **Instruction:** Put the bigger pumpkin in the bin
- **Arena env prompt:** droid Put the bigger pumpkin in the bin. Using maple table background: place the pumpkinlarge into the right bin on the table. Other objects on the table as distractors: lemon 01, lemon 02, lime01, lime01 01, orange 01, orange 02, pomegranate01, pumpkinsmall, and 7 more

#### SmallPumpkinInBinTask

- **File:** `robolab/tasks/benchmark/clutter_small_pumpkin_task.py`
- **Instruction:** Put the small pumpkin in the bin
- **Arena env prompt:** droid Put the small pumpkin in the bin. Using maple table background: place the pumpkinsmall into the right bin on the table. Other objects on the table as distractors: lemon 01, lemon 02, lime01, lime01 01, orange 01, orange 02, pomegranate01, pumpkinlarge, and 7 more

---

## breakfast_table.usda

![breakfast_table.usda](../_images/breakfast_table.png)

- **Objects:** 19
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `banana` → `../objects/ycb/banana.usd`
- `bagel_07` → `../objects/objaverse/bagel_06.usd`
- `coffee_can` → `../objects/ycb/coffee_can.usd`
- `banana_01` → `../objects/ycb/banana.usd`
- `yogurt_cup` → `../objects/hope/yogurt_cup.usd`
- `coffee_pot` → `../objects/hot3d/coffee_pot.usd`
- `ceramic_mug` → `../objects/hot3d/ceramic_mug.usd`
- `pitcher` → `../objects/hot3d/pitcher.usd`
- `fork_big` → `../objects/vomp/fork_big/fork_big.usd`
- `spoon_big` → `../objects/vomp/spoon_big/spoon_big.usd`
- `apple_01` → `../objects/objaverse/apple_01.usd`
- `orange2` → `../objects/fruits_veggies/orange2.usd`
- `milk_carton` → `../objects/hope/milk_carton.usd`
- `orange_juice_carton` → `../objects/hope/orange_juice_carton.usd`
- `bagel_01` → `../objects/objaverse/bagel_00.usd`
- `bagel_02` → `../objects/objaverse/bagel_06.usd`
- `plate_small` → `../objects/vomp/plate_small/plate_small.usd`
- `plate_large` → `../objects/vomp/plate_large/plate_large.usd`

### Benchmark tasks

#### YogurtInBowlTask

- **File:** `robolab/tasks/benchmark/yogurt_in_bowl.py`
- **Instruction:** Put the small red yogurt in the red bowl
- **Arena env prompt:** droid Put the small red yogurt in the red bowl. Using maple table background: place the yogurt cup into the bowl on the table. Other objects on the table as distractors: banana, bagel 07, coffee can, banana 01, coffee pot, ceramic mug, pitcher, fork big, and 9 more
