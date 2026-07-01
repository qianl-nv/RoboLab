# RoboLab PnP Multi Scene Catalog

29 benchmark scenes · 60 tasks

Filter: `pick_and_place` or `pick_and_place_on_surface` with multiple objects and/or multiple subtasks.

Prompts target `EnvironmentGenerationAgent.generate_spec()` with the DROID embodiment.

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

#### BananaThenRubiksCubeTask

- **File:** `robolab/tasks/benchmark/banana_then_rubiks_cube.py`
- **Instruction:** put the banana then the cube in the bowl
- **Arena env prompt:** droid put the banana then the cube in the bowl. Using maple table background: place the banana into the bowl on the table; place the rubiks cube into the bowl on the table

#### RubiksCubeAndBananaTask

- **File:** `robolab/tasks/benchmark/rubiks_cube_and_banana_task.py`
- **Instruction:** Put the cube and the banana in the bowl
- **Arena env prompt:** droid Put the cube and the banana in the bowl. Using maple table background: place rubiks cube, banana into the bowl on the table

#### RubiksCubeOrBananaTask

- **File:** `robolab/tasks/benchmark/rubiks_cube_or_banana_task.py`
- **Instruction:** Put the cube or the banana in the bowl
- **Arena env prompt:** droid Put the cube or the banana in the bowl. Using maple table background: place rubiks cube, banana into the bowl on the table

#### RubiksCubeThenBananaTask

- **File:** `robolab/tasks/benchmark/rubiks_cube_then_banana.py`
- **Instruction:** Put the cube then the banana in the bowl
- **Arena env prompt:** droid Put the cube then the banana in the bowl. Using maple table background: place the rubiks cube into the bowl on the table; place the banana into the bowl on the table

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

#### BagelsOnPlateTask

- **File:** `robolab/tasks/benchmark/bagel_on_plate_task.py`
- **Instruction:** Put the bagels on the plate
- **Arena env prompt:** droid Put the bagels on the plate. Using maple table background: place bagel 00, bagel 06 on the plate large on the table. Other objects on the table as distractors: banana, bowl

---

## mugs_on_shelf.usda

![mugs_on_shelf.usda](../_images/mugs_on_shelf.png)

- **Objects:** 5
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `ceramic_mug` → `../objects/hot3d/ceramic_mug.usd`
- `mug` → `../objects/hot3d/mug.usd`
- `rack_l04` → `../objects/vomp/rack_l04/rack_l04.usd`
- `serving_bowl` → `../objects/vomp/serving_bowl/serving_bowl.usd`
- `utilityjug_a01` → `../objects/vomp/utilityjug_a01/utilityjug_a01.usd`

### Benchmark tasks

#### TakeMugsOffOfShelfTask

- **File:** `robolab/tasks/benchmark/take_mugs_off_of_shelf.py`
- **Instruction:** Take the mugs off the shelf
- **Arena env prompt:** droid Take the mugs off the shelf. Using maple table background: place ceramic mug, mug on the table. Other objects on the table as distractors: rack l04, serving bowl, utilityjug a01

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

#### RedDishesInBinTask

- **File:** `robolab/tasks/benchmark/red_dishes_in_bin.py`
- **Instruction:** Put the red dishware in the grey bin
- **Arena env prompt:** droid Put the red dishware in the grey bin. Using maple table background: place mug, bowl into the grey bin on the table. Other objects on the table as distractors: banana, rubiks cube

#### RedItemsInBinTask

- **File:** `robolab/tasks/benchmark/red_items_in_bin.py`
- **Instruction:** Put all the red things in the grey bin
- **Arena env prompt:** droid Put all the red things in the grey bin. Using maple table background: place mug, bowl into the grey bin on the table. Other objects on the table as distractors: banana, rubiks cube

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

#### PutMugsOnShelfTask

- **File:** `robolab/tasks/benchmark/put_mugs_on_shelf.py`
- **Instruction:** Put the two mugs on the shelf
- **Arena env prompt:** droid Put the two mugs on the shelf. Using maple table background: place ceramic mug, mug into the rack l04 on the table. Other objects on the table as distractors: serving bowl, utilityjug a01

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

#### BananasInBinOneMoreTask

- **File:** `robolab/tasks/benchmark/bananas_in_bin_one_more.py`
- **Instruction:** Put one (1) more bananas in the grey bin.
- **Arena env prompt:** droid Put one (1) more bananas in the grey bin. Using maple table background: place banana, banana 01, banana 03 into the grey bin on the table. Other objects on the table as distractors: banana 02, banana 04

#### BananasInBinThreeTotalTask

- **File:** `robolab/tasks/benchmark/bananas_in_bin_three.py`
- **Instruction:** Make sure there are 3 (three) bananas in the grey bin.
- **Arena env prompt:** droid Make sure there are 3 (three) bananas in the grey bin. Using maple table background: place banana, banana 01, banana 03 into the grey bin on the table. Other objects on the table as distractors: banana 02, banana 04

---

## bananas_5_in_crate.usda

![bananas_5_in_crate.usda](../_images/bananas_5_in_crate.png)

- **Objects:** 6
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `banana` → `../objects/ycb/banana.usd`
- `purple_crate` → `https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/4.5/Isaac/Props/KLT_Bin/small_KLT_visual_collision.usd`
- `banana_01` → `../objects/ycb/banana.usd`
- `banana_02` → `../objects/ycb/banana.usd`
- `banana_03` → `../objects/ycb/banana.usd`
- `banana_04` → `../objects/ycb/banana.usd`

### Benchmark tasks

#### BananasInCrateTask

- **File:** `robolab/tasks/benchmark/bananas_in_crate.py`
- **Instruction:** Put 2 bananas in the crate
- **Arena env prompt:** droid Put 2 bananas in the crate. Using maple table background: place banana, banana 02, banana 03, banana 04 into the purple crate on the table. Other objects on the table as distractors: banana 01

---

## foodpacking_1bin_2box_2can.usda

![foodpacking_1bin_2box_2can.usda](../_images/foodpacking_1bin_2box_2can.png)

- **Objects:** 6
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `bin_a06` → `../objects/vomp/bin_a06/bin_a06.usd`
- `cheez_it` → `../objects/ycb/cheez_it.usd`
- `mustard` → `../objects/ycb/mustard.usd`
- `sugar_box` → `../objects/ycb/sugar_box.usd`
- `tomato_soup_can` → `../objects/ycb/tomato_soup_can.usd`
- `tuna_can` → `../objects/ycb/tuna_can.usd`

### Benchmark tasks

#### FoodPacking2BoxesTask

- **File:** `robolab/tasks/benchmark/foodpacking_1bin_2box.py`
- **Instruction:** Pack boxed foods into the bin
- **Arena env prompt:** droid Pack boxed foods into the bin. Using maple table background: place cheez it, sugar box into the bin a06 on the table. Other objects on the table as distractors: mustard, tomato soup can, tuna can

#### FoodPacking2CansTask

- **File:** `robolab/tasks/benchmark/foodpacking_1bin_2can.py`
- **Instruction:** Pack canned foods into the bin
- **Arena env prompt:** droid Pack canned foods into the bin. Using maple table background: place tomato soup can, tuna can into the bin a06 on the table. Other objects on the table as distractors: cheez it, mustard, sugar box

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

#### HammersInLeftBinTask

- **File:** `robolab/tasks/benchmark/tool_organization_left_task.py`
- **Instruction:** Put the red hammer and black hammer in the left bin
- **Arena env prompt:** droid Put the red hammer and black hammer in the left bin. Using maple table background: place red hammer, husky hammer into the left bin on the table. Other objects on the table as distractors: right bin, cordless drill, spring clamp

#### NonHammerToolsInRightBinTask

- **File:** `robolab/tasks/benchmark/non_hammer_tools_in_right_bin.py`
- **Instruction:** Put the non-hammer tools in the right bin
- **Arena env prompt:** droid Put the non-hammer tools in the right bin. Using maple table background: place cordless drill, spring clamp into the right bin on the table. Other objects on the table as distractors: left bin, red hammer, husky hammer

#### ToolOrganizationBothTask

- **File:** `robolab/tasks/benchmark/tool_organization_both_task.py`
- **Instruction:** Put hammers in the right bin and do not touch anything else
- **Arena env prompt:** droid Put hammers in the right bin and do not touch anything else. Using maple table background: place red hammer, husky hammer into the right bin on the table. Other objects on the table as distractors: left bin, cordless drill, spring clamp

#### ToolOrganizationTask

- **File:** `robolab/tasks/benchmark/tool_organization_task.py`
- **Instruction:** Put the red hammer and black hammer in the left bin
- **Arena env prompt:** droid Put the red hammer and black hammer in the left bin. Using maple table background: place red hammer, husky hammer into the left bin on the table. Other objects on the table as distractors: right bin, cordless drill, spring clamp

---

## cartons_in_crate.usda

![cartons_in_crate.usda](../_images/cartons_in_crate.png)

- **Objects:** 8
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `alphabet_soup_can` → `../objects/hot3d/soup_can.usd`
- `milk_carton` → `../objects/hope/milk_carton.usd`
- `orange_juice_carton` → `../objects/hope/orange_juice_carton.usd`
- `smartphone` → `../objects/hot3d/smartphone.usd`
- `mug` → `../objects/hot3d/mug.usd`
- `container_a01` → `../objects/vomp/container_a01/container_a01.usd`
- `mayonnaise_bottle` → `../objects/hope/mayonnaise_bottle.usd`
- `ketchup_bottle` → `../objects/hope/ketchup_bottle.usd`

### Benchmark tasks

#### RecycleCartonTask

- **File:** `robolab/tasks/benchmark/recycle_cartons.py`
- **Instruction:** Put the recyclable cartons in the grey bin
- **Arena env prompt:** droid Put the recyclable cartons in the grey bin. Using maple table background: place milk carton, orange juice carton into the container a01 on the table. Other objects on the table as distractors: alphabet soup can, smartphone, mayonnaise bottle, ketchup bottle, mug

---

## cartons_in_vertical_crate.usda

![cartons_in_vertical_crate.usda](../_images/cartons_in_vertical_crate.png)

- **Objects:** 8
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `alphabet_soup_can` → `../objects/hot3d/soup_can.usd`
- `milk_carton` → `../objects/hope/milk_carton.usd`
- `orange_juice_carton` → `../objects/hope/orange_juice_carton.usd`
- `smartphone` → `../objects/hot3d/smartphone.usd`
- `mug` → `../objects/hot3d/mug.usd`
- `container_a01` → `../objects/vomp/container_a01/container_a01.usd`
- `mayonnaise_bottle` → `../objects/hope/mayonnaise_bottle.usd`
- `ketchup_bottle` → `../objects/hope/ketchup_bottle.usd`

### Benchmark tasks

#### RecycleCartonsVerticalCrateTask

- **File:** `robolab/tasks/benchmark/recycle_cartons_vertical_crate.py`
- **Instruction:** Put the cartons that can be recycled in the vertical crate
- **Arena env prompt:** droid Put the cartons that can be recycled in the vertical crate. Using maple table background: place milk carton, orange juice carton into the container a01 on the table. Other objects on the table as distractors: alphabet soup can, smartphone, mayonnaise bottle, ketchup bottle, mug

---

## cartons_on_box.usda

![cartons_on_box.usda](../_images/cartons_on_box.png)

- **Objects:** 8
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `alphabet_soup_can` → `../objects/hot3d/soup_can.usd`
- `milk_carton` → `../objects/hope/milk_carton.usd`
- `orange_juice_carton` → `../objects/hope/orange_juice_carton.usd`
- `smartphone` → `../objects/hot3d/smartphone.usd`
- `mug` → `../objects/hot3d/mug.usd`
- `mayonnaise_bottle` → `../objects/hope/mayonnaise_bottle.usd`
- `ketchup_bottle` → `../objects/hope/ketchup_bottle.usd`
- `cubebox_a02` → `../objects/vomp/cubebox_a02/cubebox_a02.usd`

### Benchmark tasks

#### RecycleCartonsOnBoxTask

- **File:** `robolab/tasks/benchmark/recycle_cartons_on_box.py`
- **Instruction:** Put the cartons that can be recycled on the box
- **Arena env prompt:** droid Put the cartons that can be recycled on the box. Using maple table background: place milk carton, orange juice carton on the cubebox a02 on the table. Other objects on the table as distractors: alphabet soup can, smartphone, mayonnaise bottle, ketchup bottle, mug

---

## foodpacking_1bin_3box_3can.usda

![foodpacking_1bin_3box_3can.usda](../_images/foodpacking_1bin_3box_3can.png)

- **Objects:** 8
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `bin_a06` → `../objects/vomp/bin_a06/bin_a06.usd`
- `cheez_it` → `../objects/ycb/cheez_it.usd`
- `chocolate_pudding` → `../objects/ycb/chocolate_pudding.usd`
- `mustard` → `../objects/ycb/mustard.usd`
- `spam_can` → `../objects/ycb/spam_can.usd`
- `sugar_box` → `../objects/ycb/sugar_box.usd`
- `tomato_soup_can` → `../objects/ycb/tomato_soup_can.usd`
- `tuna_can` → `../objects/ycb/tuna_can.usd`

### Benchmark tasks

#### FoodPacking3BoxesTask

- **File:** `robolab/tasks/benchmark/foodpacking_1bin_3box.py`
- **Instruction:** Pack boxed foods into the bin
- **Arena env prompt:** droid Pack boxed foods into the bin. Using maple table background: place cheez it, chocolate pudding, sugar box into the bin a06 on the table. Other objects on the table as distractors: mustard, spam can, tomato soup can, tuna can

#### FoodPacking3CansTask

- **File:** `robolab/tasks/benchmark/foodpacking_1bin_3can.py`
- **Instruction:** Pack canned foods into the bin
- **Arena env prompt:** droid Pack canned foods into the bin. Using maple table background: place spam can, tomato soup can, tuna can into the bin a06 on the table. Other objects on the table as distractors: cheez it, chocolate pudding, mustard, sugar box

---

## mug_banana_ketchup_bowl_rubiks3_bin.usda

![mug_banana_ketchup_bowl_rubiks3_bin.usda](../_images/mug_banana_ketchup_bowl_rubiks3_bin.png)

- **Objects:** 8
- **Table payload:** `../fixtures/table_maple.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `ketchup_bottle` → `../objects/hope/ketchup_bottle.usd`
- `grey_bin` → `../fixtures/grey_bin.usd`
- `mug` → `../objects/hot3d/mug.usd`
- `rubiks_cube_middle` → `../objects/hot3d/rubiks_cube.usd`
- `rubiks_cube_top` → `../objects/hot3d/rubiks_cube.usd`
- `rubiks_cube_bottom` → `../objects/hot3d/rubiks_cube.usd`
- `banana` → `../objects/ycb/banana.usd`

### Benchmark tasks

#### UnstackRubiksCubeTask

- **File:** `robolab/tasks/benchmark/unstack_rubiks_cube.py`
- **Instruction:** Unstack the rubiks cube tower
- **Arena env prompt:** droid Unstack the rubiks cube tower. Using maple table background: place rubiks cube middle, rubiks cube top on the table. Other objects on the table as distractors: mug, banana, ketchup bottle, rubiks cube bottom, bowl, grey bin

#### YellowAndWhiteObjectsInBinTask

- **File:** `robolab/tasks/benchmark/yellow_and_white_objects_in_bin.py`
- **Instruction:** Put all white objects and yellow objects in the grey bin
- **Arena env prompt:** droid Put all white objects and yellow objects in the grey bin. Using maple table background: place mug, banana into the grey bin on the table. Other objects on the table as distractors: bowl, ketchup bottle, rubiks cube top, rubiks cube middle, rubiks cube bottom

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

#### JugsOnShelfTask

- **File:** `robolab/tasks/benchmark/jugs_on_shelf_task.py`
- **Instruction:** Put all the jugs on the shelf
- **Arena env prompt:** droid Put all the jugs on the shelf. Using maple table background: place utilityjug a01, utilityjug a02 into the large storage rack on the table. Other objects on the table as distractors: whitepackerbottle a01, whitepackerbottle a02, squarepail a01, plasticpail a02, whitepackerbottle a03

#### OneBottleInSquarePailTask

- **File:** `robolab/tasks/benchmark/one_bottle_in_square_pail.py`
- **Instruction:** Put any white plastic bottle in the square pail
- **Arena env prompt:** droid Put any white plastic bottle in the square pail. Using maple table background: place whitepackerbottle a01, whitepackerbottle a02, whitepackerbottle a03 into the squarepail a01 on the table. Other objects on the table as distractors: utilityjug a01, utilityjug a02, plasticpail a02, large storage rack

#### OneBottleOnShelfTask

- **File:** `robolab/tasks/benchmark/one_bottle_on_shelf_task.py`
- **Instruction:** Put any white plastic bottle on the shelf
- **Arena env prompt:** droid Put any white plastic bottle on the shelf. Using maple table background: place whitepackerbottle a01, whitepackerbottle a02, whitepackerbottle a03 into the large storage rack on the table. Other objects on the table as distractors: utilityjug a01, utilityjug a02, squarepail a01, plasticpail a02

#### PlasticBottlesInSquarePailTask

- **File:** `robolab/tasks/benchmark/bottles_on_shelf_task.py`
- **Instruction:** Put all the small plastic bottles in the square pail
- **Arena env prompt:** droid Put all the small plastic bottles in the square pail. Using maple table background: place whitepackerbottle a01, whitepackerbottle a02, whitepackerbottle a03 into the squarepail a01 on the table. Other objects on the table as distractors: large storage rack, utilityjug a01, utilityjug a02, plasticpail a02

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

#### PutTwoMugsOnShelfTask

- **File:** `robolab/tasks/benchmark/put_two_mugs_on_shelf.py`
- **Instruction:** Put two (2) mugs on the wire shelf
- **Arena env prompt:** droid Put two (2) mugs on the wire shelf. Using maple table background: place ceramic mug, mug, mug 01 into the wireshelving a01 on the table. Other objects on the table as distractors: spatula 01, plate small, fork big, fork small

---

## food_packing.usda

![food_packing.usda](../_images/food_packing.png)

- **Objects:** 9
- **Table payload:** `../fixtures/table_oak.usd`

### Object payloads

- `bin_a06` → `../objects/vomp/bin_a06/bin_a06.usd`
- `cheez_it` → `../objects/ycb/cheez_it.usd`
- `chocolate_pudding` → `../objects/ycb/chocolate_pudding.usd`
- `coffee_can` → `../objects/ycb/coffee_can.usd`
- `mustard` → `../objects/ycb/mustard.usd`
- `spam_can` → `../objects/ycb/spam_can.usd`
- `sugar_box` → `../objects/ycb/sugar_box.usd`
- `tomato_soup_can` → `../objects/ycb/tomato_soup_can.usd`
- `bin_b03` → `../objects/vomp/bin_b03/bin_b03.usd`

### Benchmark tasks

#### FoodPackingByColorTask

- **File:** `robolab/tasks/benchmark/food_packing_by_color_task.py`
- **Instruction:** Pack yellow objects in right container and blue object in the left container
- **Arena env prompt:** droid Pack yellow objects in right container and blue object in the left container. Using maple table background: place the mustard into the bin a06 on the table; place the coffee can into the bin b03 on the table. Other objects on the table as distractors: cheez it, chocolate pudding, spam can, sugar box, tomato soup can

---

## mugs2_bananas2_ketchup_rubiks3_bin.usda

![mugs2_bananas2_ketchup_rubiks3_bin.usda](../_images/mugs2_bananas2_ketchup_rubiks3_bin.png)

- **Objects:** 10
- **Table payload:** `../fixtures/table_maple.usd`

### Object payloads

- `bowl` → `../objects/ycb/bowl.usd`
- `ketchup_bottle` → `../objects/hope/ketchup_bottle.usd`
- `grey_bin` → `../fixtures/grey_bin.usd`
- `mug` → `../objects/hot3d/mug.usd`
- `mug_01` → `../objects/hot3d/mug.usd`
- `banana_near` → `../objects/ycb/banana.usd`
- `banana_far` → `../objects/ycb/banana.usd`
- `rubiks_cube_middle` → `../objects/hot3d/rubiks_cube.usd`
- `rubiks_cube_top` → `../objects/hot3d/rubiks_cube.usd`
- `rubiks_cube_bottom` → `../objects/hot3d/rubiks_cube.usd`

### Benchmark tasks

#### DishesInBinTask

- **File:** `robolab/tasks/benchmark/dishes_in_bin.py`
- **Instruction:** Put the dishware in the grey bin
- **Arena env prompt:** droid Put the dishware in the grey bin. Using maple table background: place mug, mug 01, bowl into the grey bin on the table. Other objects on the table as distractors: banana near, banana far, rubiks cube top, rubiks cube middle, rubiks cube bottom, ketchup bottle

#### WhiteMugsInBinTask

- **File:** `robolab/tasks/benchmark/white_mugs_in_bin.py`
- **Instruction:** Clean up the white mugs
- **Arena env prompt:** droid Clean up the white mugs. Using maple table background: place mug, mug 01 into the grey bin on the table. Other objects on the table as distractors: banana near, banana far, rubiks cube middle, rubiks cube top, rubiks cube bottom, ketchup bottle, bowl

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

#### ToolsPickingAllHammersTask

- **File:** `robolab/tasks/benchmark/tools_picking_all_hammers.py`
- **Instruction:** Take out all the hammers and put them on the table
- **Arena env prompt:** droid Take out all the hammers and put them on the table. Using maple table background: place husky hammer, blue hammer, red hammer, wood hammer on the table. Other objects on the table as distractors: clamp, cordless drill, spring clamp, left bin, center bin, right bin, clamp 01

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

#### AnimalsInBinTask

- **File:** `robolab/tasks/benchmark/animals_in_bin.py`
- **Instruction:** Put the lizards in the bin
- **Arena env prompt:** droid Put the lizards in the bin. Using maple table background: place lizard figurine, lizard figurine 01 into the grey bin on the table. Other objects on the table as distractors: rubiks cube, rubiks cube 1, rubiks cube 2, birdhouse, yellow block, red block, green block, blue block

#### BlocksInBinTask

- **File:** `robolab/tasks/benchmark/blocks_in_bin.py`
- **Instruction:** Sort all colored blocks into the bin
- **Arena env prompt:** droid Sort all colored blocks into the bin. Using maple table background: place yellow block, red block, green block, blue block into the grey bin on the table. Other objects on the table as distractors: rubiks cube, rubiks cube 1, rubiks cube 2, lizard figurine, birdhouse, lizard figurine 01

#### CleanUpToysTask

- **File:** `robolab/tasks/benchmark/clean_up_toys.py`
- **Instruction:** Clean up all the smaller toys and leave the birdhouse on the table
- **Arena env prompt:** droid Clean up all the smaller toys and leave the birdhouse on the table. Using maple table background: place rubiks cube, rubiks cube 1, rubiks cube 2, lizard figurine, yellow block, red block, green block, blue block, lizard figurine 01 into the grey bin on the table. Other objects on the table as distractors: birdhouse

#### CubesAndBlocksInBinTask

- **File:** `robolab/tasks/benchmark/cubes_and_blocks_in_bin.py`
- **Instruction:** Put all the cubes and blocks in the bin
- **Arena env prompt:** droid Put all the cubes and blocks in the bin. Using maple table background: place rubiks cube, rubiks cube 1, rubiks cube 2 into the grey bin on the table; place yellow block, red block, green block, blue block into the grey bin on the table. Other objects on the table as distractors: lizard figurine, birdhouse, lizard figurine 01

#### RubiksCubesInBinTask

- **File:** `robolab/tasks/benchmark/rubiks_cubes_in_bin.py`
- **Instruction:** Sort all rubiks cubes into the bin
- **Arena env prompt:** droid Sort all rubiks cubes into the bin. Using maple table background: place rubiks cube, rubiks cube 1, rubiks cube 2 into the grey bin on the table. Other objects on the table as distractors: lizard figurine, birdhouse, yellow block, red block, green block, blue block, lizard figurine 01

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

#### BBQSauceInBinTask

- **File:** `robolab/tasks/benchmark/bbq_sauce_in_bin_task.py`
- **Instruction:** Put the red BBQ sauce bottles in the grey bin
- **Arena env prompt:** droid Put the red BBQ sauce bottles in the grey bin. Using maple table background: place bbq sauce bottle, bbq sauce bottle 01 into the grey bin on the table. Other objects on the table as distractors: mug, mustard, bowl, ranch dressing, oatmeal raisin cookies, canned tuna, soft scrub, wood block, and 1 more

#### CondimentsInBinTask

- **File:** `robolab/tasks/benchmark/condiments_in_bin_task.py`
- **Instruction:** Sort the sauce condiments into the grey bin
- **Arena env prompt:** droid Sort the sauce condiments into the grey bin. Using maple table background: place mustard, ranch dressing, bbq sauce bottle, bbq sauce bottle 01 into the grey bin on the table. Other objects on the table as distractors: mug, bowl, oatmeal raisin cookies, canned tuna, soft scrub, wood block, coffee pot

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

#### GreenSpoonsInPotTask

- **File:** `robolab/tasks/benchmark/green_spoons_in_pot.py`
- **Instruction:** Put the green spoons in the pot
- **Arena env prompt:** droid Put the green spoons in the pot. Using maple table background: place ladle, ladle 01, green serving spoon into the anza medium on the table. Other objects on the table as distractors: plate large, plate small, fork big, fork small, spatula 13, spatula 14, spatula 15, pink spaghetti spoon, and 1 more

#### SpoonsInPotTask

- **File:** `robolab/tasks/benchmark/spoons_in_pot.py`
- **Instruction:** Put all of the serving spoons with no holes in the pot
- **Arena env prompt:** droid Put all of the serving spoons with no holes in the pot. Using maple table background: place ladle, ladle 01, red serving spoon into the anza medium on the table. Other objects on the table as distractors: plate large, plate small, fork big, fork small, spatula 13, spatula 14, spatula 15, pink spaghetti spoon, and 1 more

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

#### BlackItemsInBinTask

- **File:** `robolab/tasks/benchmark/black_items_in_bin.py`
- **Instruction:** Put the black items in the grey bin
- **Arena env prompt:** droid Put the black items in the grey bin. Using maple table background: place keyboard, remote control, computer mouse, smartphone, glasses into the grey bin on the table. Other objects on the table as distractors: ceramic mug, lizard figurine, marker, wooden bowl, spoon big, yogurt cup, granola bars

#### ElectronicsInBinTask

- **File:** `robolab/tasks/benchmark/electronics_in_bin_task.py`
- **Instruction:** Put the electronic devices in the grey bin
- **Arena env prompt:** droid Put the electronic devices in the grey bin. Using maple table background: place smartphone, remote control, computer mouse, keyboard into the grey bin on the table. Other objects on the table as distractors: ceramic mug, glasses, lizard figurine, marker, wooden bowl, spoon big, yogurt cup, granola bars

#### PhoneOrRemoteInBinTask

- **File:** `robolab/tasks/benchmark/phone_or_remote_in_bin_task.py`
- **Instruction:** Put the phone or the remote in the grey bin
- **Arena env prompt:** droid Put the phone or the remote in the grey bin. Using maple table background: place smartphone, remote control into the grey bin on the table. Other objects on the table as distractors: ceramic mug, glasses, keyboard, lizard figurine, marker, wooden bowl, spoon big, computer mouse, and 2 more

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

#### AppleAndYogurtInBowlTask

- **File:** `robolab/tasks/benchmark/apple_and_yogurt_in_bowl_task.py`
- **Instruction:** Put the apple and yogurt in the bowl
- **Arena env prompt:** droid Put the apple and yogurt in the bowl. Using maple table background: place apple 01, yogurt cup into the wooden bowl on the table. Other objects on the table as distractors: ceramic mug, glasses, keyboard, marker, remote control, smartphone, spoon big, computer mouse, and 2 more

#### ThrowAwaySnacksTask

- **File:** `robolab/tasks/benchmark/throw_away_snacks_task.py`
- **Instruction:** Put away the snacks in the bin
- **Arena env prompt:** droid Put away the snacks in the bin. Using maple table background: place apple 01, yogurt cup into the plasticpail a02 on the table. Other objects on the table as distractors: ceramic mug, glasses, keyboard, marker, remote control, smartphone, wooden bowl, spoon big, and 2 more

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

#### CookingClearPlateTask

- **File:** `robolab/tasks/benchmark/cooking_clear_plate_specific.py`
- **Instruction:** Put the two measuring cups outside of the plate
- **Arena env prompt:** droid Put the two measuring cups outside of the plate. Using maple table background: place spoon 1, measuring cups 1 on the table. Other objects on the table as distractors: redonion, serving bowl, clay plates, wooden spoons, spatula, storage box, tomato sauce can, pink spaghetti spoon, and 5 more

---

## fruits_out_of_basket.usda

![fruits_out_of_basket.usda](../_images/fruits_out_of_basket.png)

- **Objects:** 15
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
- `wooden_spoons` → `../objects/hot3d/wooden_spoons.usd`
- `spatula` → `../objects/hot3d/spatula.usd`
- `storage_box` → `../objects/hot3d/storage_box.usd`

### Benchmark tasks

#### FruitsGreenLimesOnPlateTask

- **File:** `robolab/tasks/benchmark/fruits_green_limes_on_plate.py`
- **Instruction:** Put all the green fruit on the plate
- **Arena env prompt:** droid Put all the green fruit on the plate. Using maple table background: place lime01, lime01 01 on the clay plates on the table. Other objects on the table as distractors: lemon 01, lemon 02, orange 01, orange 02, pomegranate01, pumpkinlarge, pumpkinsmall, redonion, and 4 more

#### FruitsOnPlate3Task

- **File:** `robolab/tasks/benchmark/fruits_to_plate_3.py`
- **Instruction:** Put three (3) fruits on the plate
- **Arena env prompt:** droid Put three (3) fruits on the plate. Using maple table background: place lemon 01, lemon 02, lime01, lime01 01, orange 01, orange 02, pomegranate01 on the clay plates on the table. Other objects on the table as distractors: pumpkinlarge, pumpkinsmall, redonion, serving bowl, wooden spoons, spatula, storage box

#### FruitsOnPlateTask

- **File:** `robolab/tasks/benchmark/fruits_to_plate.py`
- **Instruction:** Put all the fruits on the plate
- **Arena env prompt:** droid Put all the fruits on the plate. Using maple table background: place lemon 01, lemon 02, lime01, lime01 01, orange 01, orange 02, pomegranate01 on the clay plates on the table. Other objects on the table as distractors: pumpkinlarge, pumpkinsmall, redonion, serving bowl, wooden spoons, spatula, storage box

#### FruitsOrangesOnPlateTask

- **File:** `robolab/tasks/benchmark/fruits_oranges_on_plate.py`
- **Instruction:** Put all the oranges on the plate
- **Arena env prompt:** droid Put all the oranges on the plate. Using maple table background: place orange 01, orange 02 on the clay plates on the table. Other objects on the table as distractors: lemon 01, lemon 02, lime01, lime01 01, pomegranate01, pumpkinlarge, pumpkinsmall, redonion, and 4 more

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

#### FruitsMovingOrangeOrLimeTask

- **File:** `robolab/tasks/benchmark/fruits_move_orange_or_lime.py`
- **Instruction:** Move an orange or a lime to the wood bowl
- **Arena env prompt:** droid Move an orange or a lime to the wood bowl. Using maple table background: place orange 01, lime01, orange 02, lime01 01 into the wooden bowl on the table. Other objects on the table as distractors: lemon 01, lemon 02, pomegranate01, pumpkinlarge, pumpkinsmall, redonion, serving bowl, clay plates, and 3 more

#### FruitsMovingTask

- **File:** `robolab/tasks/benchmark/fruits_move_orange.py`
- **Instruction:** Move an orange to the white bowl
- **Arena env prompt:** droid Move an orange to the white bowl. Using maple table background: place orange 01, orange 02 into the serving bowl on the table. Other objects on the table as distractors: lemon 01, lemon 02, lime01, lime01 01, pomegranate01, pumpkinlarge, pumpkinsmall, redonion, and 5 more

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

#### ClearOrganicObjectsTask

- **File:** `robolab/tasks/benchmark/clutter_organic_objects_task.py`
- **Instruction:** Clear away the organic objects
- **Arena env prompt:** droid Clear away the organic objects. Using maple table background: place lemon 01, lemon 02, lime01, lime01 01, orange 01, orange 02, pomegranate01, pumpkinlarge, pumpkinsmall, red onion, avocado01 into the right bin on the table. Other objects on the table as distractors: whitepackerbottle a01, crabbypenholder, milkjug a01, serving bowl, utilityjug a03

#### ClutterPlasticTask

- **File:** `robolab/tasks/benchmark/clutter_plastic_task.py`
- **Instruction:** Put all plastic bottles away in the bin
- **Arena env prompt:** droid Put all plastic bottles away in the bin. Using maple table background: place whitepackerbottle a01, milkjug a01, utilityjug a03 into the right bin on the table. Other objects on the table as distractors: lemon 01, lemon 02, lime01, lime01 01, orange 01, orange 02, pomegranate01, pumpkinlarge, and 5 more

#### ClutterPumpkinTask

- **File:** `robolab/tasks/benchmark/clutter_pumpkin_task.py`
- **Instruction:** Put all the pumpkins away in the bin
- **Arena env prompt:** droid Put all the pumpkins away in the bin. Using maple table background: place pumpkinlarge, pumpkinsmall into the right bin on the table. Other objects on the table as distractors: lemon 01, lemon 02, lime01, lime01 01, orange 01, orange 02, pomegranate01, red onion, and 6 more

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

#### MoveBananaToBagelPlateTask

- **File:** `robolab/tasks/benchmark/move_banana_to_bagel_plate.py`
- **Instruction:** Move the bananas to the bagel plate
- **Arena env prompt:** droid Move the bananas to the bagel plate. Using maple table background: place banana, banana 01 on the plate small on the table. Other objects on the table as distractors: bowl, bagel 07, coffee can, yogurt cup, coffee pot, ceramic mug, pitcher, fork big, and 8 more

#### UtensilsInMugTask

- **File:** `robolab/tasks/benchmark/utensils_in_mug.py`
- **Instruction:** Put the fork and spoon in the ceramicmug
- **Arena env prompt:** droid Put the fork and spoon in the ceramicmug. Using maple table background: place fork big, spoon big into the ceramic mug on the table. Other objects on the table as distractors: bowl, banana, bagel 07, coffee can, banana 01, yogurt cup, coffee pot, pitcher, and 8 more
