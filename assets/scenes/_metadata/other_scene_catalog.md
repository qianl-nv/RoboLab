# RoboLab Other Scene Catalog

16 benchmark scenes · 25 tasks

Filter: benchmark tasks without `pick_and_place` / `pick_and_place_on_surface` (stacking, reorientation, spatial, etc.).

Prompts target `EnvironmentGenerationAgent.generate_spec()` with the DROID embodiment.

---

## bowls_2_table.usda

![bowls_2_table.usda](../_images/bowls_2_table.png)

- **Objects:** 2
- **Table payload:** `../fixtures/table_maple.usd`

### Object payloads

- `bowl_1` → `../objects/ycb/bowl.usd`
- `bowl_2` → `../objects/ycb/bowl.usd`

### Benchmark tasks

#### BowlStackingLeftOnRightTask

- **File:** `robolab/tasks/benchmark/bowl_stacking_left_on_right.py`
- **Instruction:** Stack the left bowl on the right bowl
- **Arena env prompt:** droid Stack the left bowl on the right bowl. Using maple table background.. Other objects on the table as distractors: bowl 1, bowl 2

#### BowlStackingRightOnLeftTask

- **File:** `robolab/tasks/benchmark/bowl_stacking_right_on_left.py`
- **Instruction:** Stack the right bowl on the left bowl
- **Arena env prompt:** droid Stack the right bowl on the left bowl. Using maple table background.. Other objects on the table as distractors: bowl 1, bowl 2

---

## blue.usda

![blue.usda](../_images/blue.png)

- **Objects:** 3
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `plasticjerrican_a02` → `../objects/vomp/plasticjerrican_a02/plasticjerrican_a02.usd`
- `plasticpail_a02` → `../objects/vomp/plasticpail_a02/plasticpail_a02.usd`
- `pitcher` → `../objects/ycb/pitcher.usd`

### Benchmark tasks

#### PickUpBluePitcherTask

- **File:** `robolab/tasks/benchmark/pick_up_blue_pitcher.py`
- **Instruction:** Pick up the large blue pitcher
- **Arena env prompt:** droid Pick up the large blue pitcher. Using maple table background.. Other objects on the table as distractors: plasticjerrican a02, plasticpail a02, pitcher

---

## rubiks_cube_3.usda

![rubiks_cube_3.usda](../_images/rubiks_cube_3.png)

- **Objects:** 3
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `rubiks_cube` → `../objects/hot3d/rubiks_cube.usd`
- `rubiks_cube_1` → `../objects/hot3d/rubiks_cube.usd`
- `rubiks_cube_2` → `../objects/hot3d/rubiks_cube.usd`

### Benchmark tasks

#### Stack3RubiksCubeTask

- **File:** `robolab/tasks/benchmark/rubiks_cube_stacking_task.py`
- **Instruction:** Stack the rubiks cubes in a tower
- **Arena env prompt:** droid Stack the rubiks cubes in a tower. Using maple table background.. Other objects on the table as distractors: rubiks cube, rubiks cube 1, rubiks cube 2

---

## rubiks_cube_banana_bowl.usda

![rubiks_cube_banana_bowl.usda](../_images/rubiks_cube_banana_bowl.png)

- **Objects:** 3
- **Table payload:** `../fixtures/table_maple.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `rubiks_cube` → `../objects/hot3d/rubiks_cube.usd`
- `banana` → `../objects/ycb/banana.usd`

### Benchmark tasks

#### RubiksCubeBehindBowlTask

- **File:** `robolab/tasks/benchmark/rubiks_cube_behind_bowl.py`
- **Instruction:** Put the rubiks cube behind the bowl
- **Arena env prompt:** droid Put the rubiks cube behind the bowl. Using maple table background.. Other objects on the table as distractors: rubiks cube, banana, bowl

#### RubiksCubeInFrontOfBowlTask

- **File:** `robolab/tasks/benchmark/rubiks_cube_in_front_of_bowl.py`
- **Instruction:** Put the rubiks cube in front of the bowl
- **Arena env prompt:** droid Put the rubiks cube in front of the bowl. Using maple table background.. Other objects on the table as distractors: rubiks cube, banana, bowl

#### RubiksCubeLeftOfBowlTask

- **File:** `robolab/tasks/benchmark/rubiks_cube_left_of_bowl.py`
- **Instruction:** Put the rubiks cube to the left of the bowl
- **Arena env prompt:** droid Put the rubiks cube to the left of the bowl. Using maple table background.. Other objects on the table as distractors: rubiks cube, banana, bowl

---

## colored_blocks.usda

![colored_blocks.usda](../_images/colored_blocks.png)

- **Objects:** 4
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `blue_block` → `../objects/basic/blue_block.usd`
- `green_block` → `../objects/basic/green_block.usd`
- `red_block` → `../objects/basic/red_block.usd`
- `yellow_block` → `../objects/basic/yellow_block.usd`

### Benchmark tasks

#### BlockStackingOrderAgnosticTask

- **File:** `robolab/tasks/benchmark/block_stacking_order_agnostic_task.py`
- **Instruction:** Stack the blocks into a tower
- **Arena env prompt:** droid Stack the blocks into a tower. Using maple table background.. Other objects on the table as distractors: red block, blue block, green block, yellow block

#### BlockStackingSpecifiedOrderTask

- **File:** `robolab/tasks/benchmark/block_stacking_specified_order_task.py`
- **Instruction:** Stack the blocks in the order from bottom to top: red, blue, green, yellow
- **Arena env prompt:** droid Stack the blocks in the order from bottom to top: red, blue, green, yellow. Using maple table background.. Other objects on the table as distractors: red block, blue block, green block, yellow block

---

## green.usda

![green.usda](../_images/green.png)

- **Objects:** 4
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `blackandbrassbowl_large` → `../objects/vomp/blackandbrassbowl_large/blackandbrassbowl_large.usd`
- `screwtoppail_a01` → `../objects/vomp/screwtoppail_a01/screwtoppail_a01.usd`
- `utilityjug_a02` → `../objects/vomp/utilityjug_a02/utilityjug_a02.usd`
- `frozen_vegetable_block` → `../objects/hot3d/frozen_vegetable_block.usd`

### Benchmark tasks

#### PickUpGreenObjectTask

- **File:** `robolab/tasks/benchmark/pick_up_green_object.py`
- **Instruction:** Pick up the green vegetable block
- **Arena env prompt:** droid Pick up the green vegetable block. Using maple table background.. Other objects on the table as distractors: frozen vegetable block, blackandbrassbowl large, screwtoppail a01, utilityjug a02

---

## rubiks_cube_banana_bowl_mug_bin.usda

![rubiks_cube_banana_bowl_mug_bin.usda](../_images/rubiks_cube_banana_bowl_mug_bin.png)

- **Objects:** 5
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `rubiks_cube` → `../objects/hot3d/rubiks_cube.usd`
- `banana` → `../objects/ycb/banana.usd`
- `grey_bin` → `../fixtures/grey_bin.usd`
- `mug` → `../objects/ycb/mug.usd`

### Benchmark tasks

#### RubiksCubeRightOfBowlTask

- **File:** `robolab/tasks/benchmark/rubiks_cube_right_of_bowl.py`
- **Instruction:** Put the rubiks cube to the right of the bowl
- **Arena env prompt:** droid Put the rubiks cube to the right of the bowl. Using maple table background.. Other objects on the table as distractors: rubiks cube, banana, bowl, mug, grey bin

---

## bananas_5_grey_bin.usda

![bananas_5_grey_bin.usda](../_images/bananas_5_grey_bin.png)

- **Objects:** 6
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `banana` → `../objects/ycb/banana.usd`
- `banana_01` → `../objects/ycb/banana.usd`
- `banana_02` → `../objects/ycb/banana.usd`
- `banana_03` → `../objects/ycb/banana.usd`
- `banana_04` → `../objects/ycb/banana.usd`
- `grey_bin` → `../fixtures/grey_bin.usd`

### Benchmark tasks

#### BananasOutOfBinTask

- **File:** `robolab/tasks/benchmark/bananas_out_of_bin.py`
- **Instruction:** Take the bananas out
- **Arena env prompt:** droid Take the bananas out. Using maple table background.. Other objects on the table as distractors: banana, banana 01, banana 02, banana 03, banana 04, grey bin

---

## mugs4_measuringcup_drill_bowl.usda

![mugs4_measuringcup_drill_bowl.usda](../_images/mugs4_measuringcup_drill_bowl.png)

- **Objects:** 7
- **Table payload:** `../fixtures/table_maple.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `ceramic_mug` → `../objects/hot3d/ceramic_mug.usd`
- `red_mug` → `../objects/ycb/mug.usd`
- `measuring_cup` → `../objects/handal/measuring_cups.usd`
- `cordless_drill` → `../objects/ycb/cordless_drill.usd`
- `sideways_white_mug` → `../objects/hot3d/mug.usd`
- `upright_white_mug` → `../objects/hot3d/mug.usd`

### Benchmark tasks

#### PickDrillTask

- **File:** `robolab/tasks/benchmark/pick_drill.py`
- **Instruction:** Pick up the cordless drill.
- **Arena env prompt:** droid Pick up the cordless drill. Using maple table background.. Other objects on the table as distractors: red mug, bowl, ceramic mug, upright white mug, sideways white mug, cordless drill, measuring cup

#### ReorientAllMugsTask

- **File:** `robolab/tasks/benchmark/reorient_all_mugs_task.py`
- **Instruction:** Reorient all the mugs upright so that the opening is facing upwards.
- **Arena env prompt:** droid Reorient all the mugs upright so that the opening is facing upwards. Using maple table background.. Other objects on the table as distractors: red mug, bowl, ceramic mug, upright white mug, sideways white mug, cordless drill, measuring cup

#### ReorientRedMugTask

- **File:** `robolab/tasks/benchmark/reorient_red_mugs_task.py`
- **Instruction:** Put the red mug upright so that the opening is facing upwards.
- **Arena env prompt:** droid Put the red mug upright so that the opening is facing upwards. Using maple table background.. Other objects on the table as distractors: red mug, bowl, ceramic mug, upright white mug, sideways white mug, cordless drill, measuring cup

#### StackWhiteMugsTask

- **File:** `robolab/tasks/benchmark/stack_white_mugs_task.py`
- **Instruction:** Stack the white mugs on top of each other.
- **Arena env prompt:** droid Stack the white mugs on top of each other. Using maple table background.. Other objects on the table as distractors: red mug, bowl, ceramic mug, upright white mug, sideways white mug, cordless drill, measuring cup

---

## mugs4_measuringcup_drill_bowl_v2.usda

![mugs4_measuringcup_drill_bowl_v2.usda](../_images/mugs4_measuringcup_drill_bowl_v2.png)

- **Objects:** 7
- **Table payload:** `../fixtures/table_maple.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `ceramic_mug` → `../objects/hot3d/ceramic_mug.usd`
- `red_mug` → `../objects/ycb/mug.usd`
- `measuring_cup` → `../objects/handal/measuring_cups.usd`
- `cordless_drill` → `../objects/ycb/cordless_drill.usd`
- `upright_white_mug` → `../objects/hot3d/mug.usd`
- `sideways_white_mug` → `../objects/hot3d/mug.usd`

### Benchmark tasks

#### ReorientWhiteMugsTask

- **File:** `robolab/tasks/benchmark/reorient_white_mugs.py`
- **Instruction:** Make sure all the white mugs are upright so that the opening is facing upwards.
- **Arena env prompt:** droid Make sure all the white mugs are upright so that the opening is facing upwards. Using maple table background.. Other objects on the table as distractors: red mug, bowl, ceramic mug, upright white mug, sideways white mug, cordless drill, measuring cup

#### TakeMeasuringSpoonOutTask

- **File:** `robolab/tasks/benchmark/take_measuring_spoon_out.py`
- **Instruction:** Take the white colored measuring spoon out of the red bowl and put it on the table.
- **Arena env prompt:** droid Take the white colored measuring spoon out of the red bowl and put it on the table. Using maple table background.. Other objects on the table as distractors: red mug, bowl, ceramic mug, upright white mug, sideways white mug, cordless drill, measuring cup

---

## objects_around_table.usda

![objects_around_table.usda](../_images/objects_around_table.png)

- **Objects:** 8
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `banana` → `../objects/ycb/banana.usd`
- `alphabet_soup_can` → `../objects/hot3d/soup_can.usd`
- `milk_carton` → `../objects/hope/milk_carton.usd`
- `orange_juice_carton` → `../objects/hope/orange_juice_carton.usd`
- `smartphone` → `../objects/hot3d/smartphone.usd`
- `rubiks_cube` → `../objects/hot3d/rubiks_cube.usd`
- `mug` → `../objects/hot3d/mug.usd`

### Benchmark tasks

#### WhiteMugInCenterOfTableTask

- **File:** `robolab/tasks/benchmark/white_mug_in_center_of_table.py`
- **Instruction:** Put the white mug in the center of the table.
- **Arena env prompt:** droid Put the white mug in the center of the table. Using maple table background.. Other objects on the table as distractors: mug, bowl, alphabet soup can, orange juice carton, smartphone, milk carton, banana, rubiks cube

---

## shelf_with_cleaning_products.usda

![shelf_with_cleaning_products.usda](../_images/shelf_with_cleaning_products.png)

- **Objects:** 8
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `large_storage_rack` → `../objects/vomp/bulkstoragerack_a01/bulkstoragerack_a01.usd`
- `whitepackerbottle_a01` → `../objects/vomp/whitepackerbottle_a01/whitepackerbottle_a01.usd`
- `whitepackerbottle_a02` → `../objects/vomp/whitepackerbottle_a02/whitepackerbottle_a02.usd`
- `utilityjug_a01` → `../objects/vomp/utilityjug_a01/utilityjug_a01.usd`
- `utilityjug_a02` → `../objects/vomp/utilityjug_a02/utilityjug_a02.usd`
- `squarepail_a01` → `../objects/vomp/squarepail_a01/squarepail_a01.usd`
- `plasticpail_a02` → `../objects/vomp/plasticpail_a02/plasticpail_a02.usd`
- `whitepackerbottle_a03` → `../objects/vomp/whitepackerbottle_a03/whitepackerbottle_a03.usd`

### Benchmark tasks

#### ReorientJugTask

- **File:** `robolab/tasks/benchmark/reorient_jug.py`
- **Instruction:** Stand the jug upright
- **Arena env prompt:** droid Stand the jug upright. Using maple table background.. Other objects on the table as distractors: large storage rack, whitepackerbottle a01, whitepackerbottle a02, utilityjug a01, utilityjug a02, squarepail a01, plasticpail a02, whitepackerbottle a03

---

## toys_cleanup.usda

![toys_cleanup.usda](../_images/toys_cleanup.png)

- **Objects:** 11
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `rubiks_cube` → `../objects/hot3d/rubiks_cube.usd`
- `rubiks_cube_1` → `../objects/hot3d/rubiks_cube.usd`
- `rubiks_cube_2` → `../objects/hot3d/rubiks_cube.usd`
- `grey_bin` → `../fixtures/grey_bin.usd`
- `lizard_figurine` → `../objects/hot3d/lizard_figurine.usd`
- `birdhouse` → `../objects/hot3d/birdhouse.usd`
- `yellow_block` → `../objects/basic/yellow_block.usd`
- `red_block` → `../objects/basic/red_block.usd`
- `green_block` → `../objects/basic/green_block.usd`
- `blue_block` → `../objects/basic/blue_block.usd`
- `lizard_figurine_01` → `../objects/hot3d/lizard_figurine.usd`

### Benchmark tasks

#### StackYellowOnRedTask

- **File:** `robolab/tasks/benchmark/stack_yellow_on_red.py`
- **Instruction:** Stack the yellow block on the red block
- **Arena env prompt:** droid Stack the yellow block on the red block. Using maple table background.. Other objects on the table as distractors: rubiks cube, rubiks cube 1, rubiks cube 2, grey bin, lizard figurine, birdhouse, yellow block, red block, and 3 more

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

#### PickGlassesTask

- **File:** `robolab/tasks/benchmark/pick_glasses_task.py`
- **Instruction:** Pick up the eye glasses
- **Arena env prompt:** droid Pick up the eye glasses. Using maple table background.. Other objects on the table as distractors: ceramic mug, glasses, keyboard, lizard figurine, marker, remote control, rubiks cube, smartphone, and 6 more

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

#### PickOrangeObjectTask

- **File:** `robolab/tasks/benchmark/cooking_orange_object.py`
- **Instruction:** Pick up the orange measuring cup
- **Arena env prompt:** droid Pick up the orange measuring cup. Using maple table background.. Other objects on the table as distractors: redonion, serving bowl, clay plates, wooden spoons, spatula, storage box, tomato sauce can, measuring cups 1, and 7 more

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

#### GrabABagelTask

- **File:** `robolab/tasks/benchmark/grab_a_bagel.py`
- **Instruction:** Grab a bagel
- **Arena env prompt:** droid Grab a bagel. Using maple table background.. Other objects on the table as distractors: bowl, banana, bagel 07, coffee can, banana 01, yogurt cup, coffee pot, ceramic mug, and 11 more

#### GrabAFruitTask

- **File:** `robolab/tasks/benchmark/grab_a_fruit.py`
- **Instruction:** Pick up a fruit
- **Arena env prompt:** droid Pick up a fruit. Using maple table background.. Other objects on the table as distractors: bowl, banana, bagel 07, coffee can, banana 01, yogurt cup, coffee pot, ceramic mug, and 11 more
