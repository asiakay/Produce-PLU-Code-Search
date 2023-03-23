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
Organic Apple Pink Lady
94128
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
"""

rows = re.findall(r'(.+)\s+(\d+)', text)

data = []
for row in rows:
    item = row[0].strip()
    plu = int(row[1]) if row[1].isdigit() else None
    data.append({"item": item, "plu": plu})

data = sorted(data, key=lambda x: x["item"])

json_data = json.dumps(data, indent=2)
print(json_data)