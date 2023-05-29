import re
import json

text = """
Pepper Green 4065
Onion Yellow 4665
Pepper Orange 3121
Orange Fla Navel 4385
Pepper Poblano 4705
Orange Juice 4382
Pepper Red La Rouge 94587
Orange Navel 4012
Pepper Red 4688
Orange Sour 3109
Pepper Yellow 4689
Organic Apple Pink Lady 9e4128
Persimmon Fuyu 4428
Organic Avocado 94225
Persimmon Hachiya 94090
Pie Pumpkin 3134
Pineapple Lg 4430
Plums Black 4437
Plums Green 4435
Plums Prune 4436
Plums Red 4042
Pomegranate 3127
Potato Red 4073
Potato Russet Loose 4072
Potato Sweet 4091
Potato White 4083
Potato Yellow 4727
Plantains 4235
Pumpkin Large 4736
Pumpkin Mini 4734
Pumpkin Pie 3134
Quince 4447
Quenepas 4483
Radish Black 4739
Radish Breakfast 2178
Radish Daikon 4598
Radish Icicle 2179
Radish Red 4089
Radish Organic 94089
Radicchio 4738
Rutabaga 4095
Salad Bar Family 4688
Salad Bar Large 4689
Salad Bar Small 4428
Salad Savoy 4823
Scallion Organic 94068
Shallots 4662
Spinach Organic 94090
Squash Acorn 4750
Squash Buttercup 4758
Squash Butternut 4759
Squash Carnival 3142
Squash Chayote 4761
Squash Delicata 4763
Squash Golden Acorn 4751
Squash Green 4067
Squash Spaghetti 4776
Squash Sweet Dumpling 4764
Squash Turks Turban 4780
Squash White Acorn 4752
Squash Yellow 4086
Star Fruit 4256
String Roll 4510
Sweet Onions 4166
Tangelo 4383
Tangerines 4055
Tomato Hothouse 4799
Tomato Plum 4541
Tomato on Vine 94539
Tomato Ugly Ripe 3061
Tomato Yellow Green 4778
Tomatillo 4801
Tomato Vine Ripe 3151
Turnip Greens 4587
Turnip Purple Top 4811
Turnip White 4812
Turnip Yellow 4470
Uniq Fruit 4459
Aloe Leaves 3064 
Anise/Fennel 4515 
Apple Braeburn 4103
Apple Braeburn Organic
Apple Cameo 3066
Apple Empire 4124 
Apple Fuji 4131
Apple Fuji Organic 94131
Apple Gaia 4134 
Apple Golden Delicious 4020
Apple Golden Delicious Organic
Apple Granny 4017
Apple Granny Organic 94017
Apple Honey Crisp 3283
Apple Jazz 3294
Apple MacIntosh 4019
Apple Pink Lady 4128
Apple Red Delicious 4016
Apple Red Delicious Organic 94016
Apple Rome 4171
Apricots  4218
Arugula 4884
Artichoke 4084 
Asparagus  4080
Asparagus Organic 94090
Asparagus White 4522
Ataloufo Mango 4312
Avocado Green 4223
Avocado Hass 4225
Avocado Organic 94225
Baby Watermelon 3421
Baby Bok Choy 4544
Baby Green Kohlrabi 2173
Baby Fennel 2158
Baby Red Beets 2174
Baby Red Kohlrabi 2176
Baby Red Romaine 2177
Banana 4011
Bananas Baby 4234
Bananas Green 4231
Bananas Red 4236
Batata 4546
Beans Green 4066
Beans Sprout 4536
Beets Bunch 4539
Black Radish 4739
Plantain 4235
Bok Choy 4545
Boston Lettuce Organic 94632
Breadfruit 4254 
Breakfast Radish 2178
Bright Light Chard 4588
Broccoli Bunch 4060
Broccoli Crowns 3082
Broccoli Organic 94567
Broccoli Raab 4547
Broccolini 3277 
Brussel Sprouts 4550
Bulk Carrots 896250
Cabbage Green 4069
Cabbage Nappa 
Cabbage Red 4554
Cabbage Savoy 4555
Cactus Leaves 4558
Cactus Pear 4255
Calabaza Squash 4760
Cantaloupe 4050 
Cardoon/Cardoni 4559
Carrots Bulk 838250
Carrot Bunch 4094
Casaba Melon 4330
Cauliflower 4079 
Cauliflower Organic 94079 
Celery 4071
Celery Root 4585 
Chard Bright Light 4588e
Chard Green Swiss 4586
Chard Red Swiss
Chayote Squash 4761
Cherries 4045
Cherry Ranier 4258
Chestnuts 4927
Chicory 4604 
Cilantro 489
Coconuts 4261
Collards 4614
Collards Org 94614
Corn All 4078
Corn White 4077
Cucumber 4062
Cucumber Hot House 4593
Cucumber Pickling/gherkin 4596 
Culantro 4508
Daikon Radish 4598
Dandelion Greens
Dasheen 4795
Dates 4263
Dill 4891
Donut Peach 3113
Dragon Fruit 3040
Eastern Peach 4403
Eddos (Taro) 4794
Eggplant 4061 
Eggplant Baby 4599
Eggplant Graf 4850ee
Eggplant White 4602
Belgian Endive 4543
Endive/Chicory 4604
Escarole 4605 
Feijoa 4265
Fiddleheads 4606 
Figs Black 4266 
Figs White / Green 4268
Frisee 3167
Garlic 4608 
Ginger Root 4612
Grapefruit Red 4023
Grapes Black 4056
Grapes Green 4022 
Grapes Red 4023
Grapefruit Red Organic 94027
Green Asparagus Organic 94080
Green Swiss Chard 4586
Greens Creates 4620
Greens Mustard 4616
Guava 4299
Habanero Pepper 3125
Horse Radish 4625
Icicle Radish 2179
Italian Plum 3145
Jackfruit 3456
Jicama 4626
Kale Greens 4627
Kale Greens Organic 94627
Kiwi fruit 4030
Kohlrabi 4628
Kumquat 4303
Leeks 4629
Leeks Organic 94629
Lemons 4053
Lemons Organic 94053
Lettuce Frise 3167
Lettuce Greenleaf Organic 94076
Lettuce Greenleaf 4076
Lettuce lceburg 4061
Lettuce Radichio 4738
Lettuce Red Leaf 4075 
Lettuce Red Leaf Organic 94075
Lettuce Romaine 4640
Lettuce Romaine Organic 94640
Lettuce Boston 4632
Limes 4048
Loose Red Beets 4541
Lychee Nut 4309
Malanga Coco 4644
Mandarin Satsuma 2134
Mango Ataloufo 4312
Mangos 4051
Melon Canary 4317
Melon Cantaloupes 4050
Melon Casaba 4320
Melon Crenshaw 4322
Melon Honeydew 4329
Melon Horned 4302
Melon Pepino 4333
Melon Santa Claus 4336
Mint Bunch 4896
Mushrooms All 4085
Mushroom Cremini 4648
Mushroom Portabella Organic 94650
Mushroom Portabella 4650
Mushroom Shitake 4651
Mustard Greens 4616
Name Costa Rican / Name White (Nyah-may) 3276
Name Yellow / Name White (Nyah-may) 3275
Name Root 4836
Nectarine 4036
Nuts Chestnut 4927
Okra 4655
Onion Boiling 4658
Onion Large Yellow 4093
Onion Red 4082
Onion Scallions 4068
Onion Sets 4668 
Onion Shallots 4662
Onions Sweet 4166
Onion Vidalia 4159
Onion White 4663
Onion White Pearl 4660
Onion Yellow 4665
Orange Juice 4382
Orange Navel 4012
Orange Sour 3109
Organic Apple Pink Lady 94128 
Organic Avocado 94225
Organic Beets 94539
Organic Boston Lettuce 94632 
Organic Braeburn Apple 94103 
Organic Broccoli 94567
Organic Bunched Radish 94089 
Organic Carrots Bunch 94094 
Organic Cauliflower 94079 
Organic Collard 94614
Organic Cucumber Hot House 94593 
Organic Dandelion Greens 94615
Organic Fuji Apple 94131
Organic Gold Beets 93273 
Organic Gold Delicious Apple 94020 
Organic Granny Apples 94017 
Organic Green Asparagus 94080 
Organic Green Grapes 94022 
Organic Green Leaf Lettuce 94076
Organic Green Swiss Chard 94586
Organic Kale 94627
Organic Leeks 94629
Organic Lemons 94053
Organic Lettuce Iceburg 94061
Organic Oranges 94012
Organic Parsley 94899
Organic Parsley Curly 94900 
Organic Portobella Mushroom 94650
Organic Radish Bunch 94089
Organic Red Delicious Apple 94016
Organic Red Grapefruit 94027
Organic Red Grapes 94023
Organic Red Swiss Chard 94587
Organic Red Leaf 94075
Organic Romaine 94640
Organic Scallion 94068
Organic Spinach 94090
Organic Tomato 93151
Organic Tomato on Vine 94664
Papaya 4052
Parsley Curly 4900
Parsley Curly Organic 94900
Parsley Italian 4901
Parsley Organic 94899
Parsley Root 4671
Parsnip Bulk 4672
Passion Fruit 4397
Pastel Paper 4509
Peaches 4038
Peach Donut 3113
Peach Eastern 4403
Pears Anjou 4416
Pears Asian 4408
Pears Bartlett 4024
Pears Bosc 4413
Pears Seckel 4422
Peas Sugar Snap 4675
Peas Snow 4092
Pepper Anaheim 4677
Pepper Cubanelle 4687
Pepper Dried 4713
Pepper Green 4065
Pepper Habanero 3125 
Pepper Hot 4691
Pepper Jalapeno4693
Pepper Orange 3121
Pepper Pablano 4705
Pepper Red LaRouge 4088
Pepper Red 4688
Pepper Yellow 4689
Persimmon Fuyu 4428
Persimmon Hachiya 4427
Pie Pumpkin 3134
Pineapple Lg 4430
Plantains 4235
Plums Black 4437
Plums Green 4435
Plums Prune 4436
Plums Red 4042
Pomegranate 3127
Potato Red 4073
Potato Russet Loose 4072
Potato Sweet 4091
Potato White 4083
Potato Yellow 4727
Pummelo 3129
Pumpkin Large 4736
Pumpkin Mini 4734
Pumpkin Pie 3134
Quince 4447
Quenepas 4483
Radiccho 4738
Radish Black 4739
Radish Breakfast 2178
Radish Daikon 4598
Radish Icicle 2179
Radish Organic 94089
Radish Red 4089
Recao 4506
Red Bananas 4236 
Red Beets Loose 4541
Red Swiss Chard 4587
Rhubarb 4745
Rutabaga 4095
Salad Bar Family 4506
Salad Bar Large 4470
Salad Bar Small 59931
Salad Savoy 4823
Scallion Organic 94068
Shallots 4662
Spinach Organic 94090
Squash Acorn 4750
Squash Buttercup 4758
Squash Butternut 4759
Squash Carnival 3142
Squash Chayote 4761
Squash Delicata 4763
Squash Golden Acorn 4751
Squash Green 4067
Squash Spaghetti 4776 
Squash Sweet Dumpling 4764 
Squash Turks Turban 4780 
Squash White Acorn 4752 
Squash Yellow 4086
Star Fruit 4256
String Roll 4510
Sunchoke 4791
Sweet Onions 4166
Tangelo 4383
Tangerines 4055
Tomato HotHouse 4799
Tomato on Vine 4664
Tomato Ugly Ripe 3061
Tomato VineRipe 3151
Tomato Yellow Green 4778
Tomatillo 4801
Tomato Plum 4087
Turnip Greens 4619
Turnip Purple 4811
Turnip White 4812
Turnip Yellow 4095
Uniq Fruit 4459
Water Coconuts 4260
Watermelon Baby 3421
Watermelon Seedless 4032
Watermelon Whole 4031
Yams 4074
Yautia Red 4834
Yautia White 4839
Yellow Potato 4727
Yucca Root 4819
Bagels Each 1655
Bagel / Cream Cheese 424
Condiment Cup 437
Danish/Pastry 625
Donuts Each 620
Muffin Each 402
Rolls Each 426
Olive Bar 727
Wing Bar-Hot 904
Hot Bar 775
"""

rows = re.findall(r'(.+)\s+(\d+)', text)

data = []
for row in rows:
    item = row[0].strip()
    plu = int(row[1]) if row[1].isdigit() else None
    data.append({"item": item, "plu": plu})

data = sorted(data, key=lambda x: x["item"])

json_data = json.dumps(data, indent=2)

# Write JSON data to a file
with open("output.json", "w") as file:
    file.write(json_data)

print("JSON data has been written to output.json.")






