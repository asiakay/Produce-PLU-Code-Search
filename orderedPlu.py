import json

def sort_and_remove_duplicates(json_array):
    unique_plu_dict = {}
    
    # Iterate through the JSON array
    for item in json_array:
        plu = item['plu']
        
        # Convert PLU to string for consistent comparison
        plu = str(plu)
        
        # Check if the PLU is already present in the dictionary
        if plu not in unique_plu_dict:
            unique_plu_dict[plu] = item
        else:
            # If duplicate PLU is found, update the associated item value
            unique_plu_dict[plu]['item'] = item['item']
    
    # Sort the unique PLUs
    sorted_plu_list = sorted(unique_plu_dict.keys(), key=lambda x: int(x))
    
    # Create a new JSON array with sorted PLUs
    sorted_array = [unique_plu_dict[plu] for plu in sorted_plu_list]
    
    return sorted_array

# Example usage
json_data = '''
[
  {
    "item": "Onion Yellow",
    "plu": 4665
  },
  {
    "item": "Orange Fla Navel",
    "plu": 4385
  },
  {
    "item": "Orange Juice",
    "plu": 4382
  },
  {
    "item": "Orange Navel",
    "plu": 4012
  },
  {
    "item": "Orange Sour",
    "plu": 3109
  },
  {
    "item": "Organic Apple Pink Lady",
    "plu": 94128
  },
  {
    "item": "Organic Avocado",
    "plu": 94225
  },
  {
    "item": "Pepper Green",
    "plu": 4065
  },
  {
    "item": "Pepper Orange",
    "plu": 3121
  },
  {
    "item": "Pepper Poblano",
    "plu": 4705
  },
  {
    "item": "Pepper Red",
    "plu": 4688
  },
  {
    "item": "Pepper Red La Rouge",
    "plu": 94587
  },
  {
    "item": "Pepper Yellow",
    "plu": 4689
  },
  {
    "item": "Persimmon Fuyu",
    "plu": 4428
  },
  {
    "item": "Persimmon Hachiya",
    "plu": 94090
  },
  {
    "item": "Pie Pumpkin",
    "plu": 3134
  },
  {
    "item": "Pineapple Lg",
    "plu": 4430
  },
  {
    "item": "Plantains",
    "plu": 4235
  },
  {
    "item": "Plums Black",
    "plu": 4437
  },
  {
    "item": "Plums Green",
    "plu": 4435
  },
  {
    "item": "Plums Prune",
    "plu": 4436
  },
  {
    "item": "Plums Red",
    "plu": 4042
  },
  {
    "item": "Pomegranate",
    "plu": 3127
  },
  {
    "item": "Potato Red",
    "plu": 4073
  },
  {
    "item": "Potato Russet Loose",
    "plu": 4072
  },
  {
    "item": "Potato Sweet",
    "plu": 4091
  },
  {
    "item": "Potato White",
    "plu": 4083
  },
  {
    "item": "Potato Yellow",
    "plu": 4727
  },
  {
    "item": "Pumpkin Large",
    "plu": 4736
  },
  {
    "item": "Pumpkin Mini",
    "plu": 4734
  },
  {
    "item": "Pumpkin Pie",
    "plu": 3134
  },
  {
    "item": "Quenepas",
    "plu": 4483
  },
  {
    "item": "Quince",
    "plu": 4447
  },
  {
    "item": "Radicchio",
    "plu": 4738
  },
  {
    "item": "Radish Black",
    "plu": 4739
  },
  {
    "item": "Radish Breakfast",
    "plu": 2178
  },
  {
    "item": "Radish Daikon",
    "plu": 4598
  },
  {
    "item": "Radish Icicle",
    "plu": 2179
  },
  {
    "item": "Radish Organic",
    "plu": 94089
  },
  {
    "item": "Radish Red",
    "plu": 4089
  },
  {
    "item": "Rutabaga",
    "plu": 4095
  },
  {
    "item": "Salad Bar Family",
    "plu": 4688
  },
  {
    "item": "Salad Bar Large",
    "plu": 4689
  },
  {
    "item": "Salad Bar Small",
    "plu": 4428
  },
  {
    "item": "Salad Savoy",
    "plu": 4823
  },
  {
    "item": "Scallion Organic",
    "plu": 94068
  },
  {
    "item": "Shallots",
    "plu": 4662
  },
  {
    "item": "Spinach Organic",
    "plu": 94090
  },
  {
    "item": "Squash Acorn",
    "plu": 4750
  },
  {
    "item": "Squash Buttercup",
    "plu": 4758
  },
  {
    "item": "Squash Butternut",
    "plu": 4759
  },
  {
    "item": "Squash Carnival",
    "plu": 3142
  },
  {
    "item": "Squash Chayote",
    "plu": 4761
  },
  {
    "item": "Squash Delicata",
    "plu": 4763
  },
  {
    "item": "Squash Golden Acorn",
    "plu": 4751
  },
  {
    "item": "Squash Green",
    "plu": 4067
  },
  {
    "item": "Squash Spaghetti",
    "plu": 4776
  },
  {
    "item": "Squash Sweet Dumpling",
    "plu": 4764
  },
  {
    "item": "Squash Turks Turban",
    "plu": 4780
  },
  {
    "item": "Squash White Acorn",
    "plu": 4752
  },
  {
    "item": "Squash Yellow",
    "plu": 4086
  },
  {
    "item": "Star Fruit",
    "plu": 4256
  },
  {
    "item": "String Roll",
    "plu": 4510
  },
  {
    "item": "Sweet Onions",
    "plu": 4166
  },
  {
    "item": "Tangelo",
    "plu": 4383
  },
  {
    "item": "Tangerines",
    "plu": 4055
  },
  {
    "item": "Tomatillo",
    "plu": 4801
  },
  {
    "item": "Tomato Hothouse",
    "plu": 4799
  },
  {
    "item": "Tomato Plum",
    "plu": 4541
  },
  {
    "item": "Tomato Ugly Ripe",
    "plu": 3061
  },
  {
    "item": "Tomato Vine Ripe",
    "plu": 3151
  },
  {
    "item": "Tomato Yellow Green",
    "plu": 4778
  },
  {
    "item": "Tomato on Vine",
    "plu": 94539
  },
  {
    "item": "Turnip Greens",
    "plu": 4587
  },
  {
    "item": "Turnip Purple Top",
    "plu": 4811
  },
  {
    "item": "Turnip White",
    "plu": 4812
  },
  {
    "item": "Turnip Yellow",
    "plu": 4470
  },
  {
    "item": "Uniq Fruit",
    "plu": 4459
  },
  {
    "item": "Aloe Leaves",
    "plu": 3064
  },
  {
    "item": "Anise/Fennel",
    "plu": 4515
  },
  {
    "item": "Apple Braeburn",
    "plu": 4103
  },
  {
    "item": "Apple Cameo",
    "plu": 3066
  },
  {
    "item": "Apple Empire",
    "plu": 4124
  },
  {
    "item": "Apple Fuji",
    "plu": 4131
  },
  {
    "item": "Apple Fuji Organic",
    "plu": 94131
  },
  {
    "item": "Apple Gaia",
    "plu": 4134
  },
  {
    "item": "Apple Golden Delicious",
    "plu": 4020
  },
  {
    "item": "Apple Granny",
    "plu": 4017
  },
  {
    "item": "Apple Granny Organic",
    "plu": 94017
  },
  {
    "item": "Apple Honey Crisp",
    "plu": 3283
  },
  {
    "item": "Apple Jazz",
    "plu": 3294
  },
  {
    "item": "Apple MacIntosh",
    "plu": 4019
  },
  {
    "item": "Apple Pink Lady",
    "plu": 4128
  },
  {
    "item": "Apple Red Delicious",
    "plu": 4016
  },
  {
    "item": "Apple Red Delicious Organic",
    "plu": 94016
  },
  {
    "item": "Apple Rome",
    "plu": 4171
  },
  {
    "item": "Apricots",
    "plu": 4218
  },
  {
    "item": "Artichoke",
    "plu": 4084
  },
  {
    "item": "Arugula",
    "plu": 4884
  },
  {
    "item": "Asparagus",
    "plu": 4080
  },
  {
    "item": "Asparagus Organic",
    "plu": 94090
  },
  {
    "item": "Asparagus White",
    "plu": 4522
  },
  {
    "item": "Ataloufo Mango",
    "plu": 4312
  },
  {
    "item": "Avocado Green",
    "plu": 4223
  },
  {
    "item": "Avocado Hass",
    "plu": 4225
  },
  {
    "item": "Avocado Organic",
    "plu": 94225
  },
  {
    "item": "Baby Bok Choy",
    "plu": 4544
  },
  {
    "item": "Baby Fennel",
    "plu": 2158
  },
  {
    "item": "Baby Green Kohlrabi",
    "plu": 2173
  },
  {
    "item": "Baby Red Beets",
    "plu": 2174
  },
  {
    "item": "Baby Red Kohlrabi",
    "plu": 2176
  },
  {
    "item": "Baby Red Romaine",
    "plu": 2177
  },
  {
    "item": "Baby Watermelon",
    "plu": 3421
  },
  { "item": "banana", "plu": "4011" },
  { "item": "broccoli", "plu": "4567" },
  { "item": "cilantro", "plu": "4889" },
  { "item": "yellow onion", "plu": "4665" },
  { "item": "Avocado", "plu": "4225" },
  { "item": "Onion Shallots", "plu": "4662" },
  { "item": "Onions Sweet", "plu": "4166" },
  { "item": "Onion Vidalia", "plu": "4159" },
  { "item": "Onion White", "plu": "4663" },
  { "item": "Onion White Pearl", "plu": "4660" },
  { "item": "Onion Yellow", "plu": "4665" },
  { "item": "Orange Fla Navel", "plu": "4385" },
  { "item": "Orange Juice", "plu": "4382" },
  { "item": "Orange Navel", "plu": "4012" },
  { "item": "Orange Sour", "plu": "3109" },
  { "item": "Organic Apple Pink Lady", "plu": "94128" },
  { "item": "Organic Avocado", "plu": "94225" },
  { "item": "Organic Beets", "plu": "94539" },
  { "item": "Organic Boston Lett", "plu": "94632" },
  { "item": "Organic Braeburn App", "plu": "94103" },
  { "item": "Organic Broccoli", "plu": "94567" },
  { "item": "Organic Bunched Radish", "plu": "94089" },
  { "item": "Organic Carrots Bunch", "plu": "94094" },
  { "item": "Organic Cauliflower", "plu": "94079" },
  { "item": "Organic Collard", "plu": "94614" },
  {
    "item": "Onion Yellow",
    "plu": 4665
  },
  {
    "item": "Orange Fla Navel",
    "plu": 4385
  },
  {
    "item": "Orange Juice",
    "plu": 4382
  },
  {
    "item": "Orange Navel",
    "plu": 4012
  },
  {
    "item": "Orange Sour",
    "plu": 3109
  },
  {
    "item": "Organic Apple Pink Lady",
    "plu": 94128
  },
  {
    "item": "Organic Avocado",
    "plu": 94225
  },
  {
    "item": "Pepper Green",
    "plu": 4065
  },
  {
    "item": "Pepper Orange",
    "plu": 3121
  },
  {
    "item": "Pepper Poblano",
    "plu": 4705
  },
  {
    "item": "Pepper Red",
    "plu": 4688
  },
  {
    "item": "Pepper Red La Rouge",
    "plu": 94587
  },
  {
    "item": "Pepper Yellow",
    "plu": 4689
  },
  {
    "item": "Persimmon Fuyu",
    "plu": 4428
  },
  {
    "item": "Persimmon Hachiya",
    "plu": 94090
  },
  {
    "item": "Pie Pumpkin",
    "plu": 3134
  },
  {
    "item": "Pineapple Lg",
    "plu": 4430
  },
  {
    "item": "Plantains",
    "plu": 4235
  },
  {
    "item": "Plums Black",
    "plu": 4437
  },
  {
    "item": "Plums Green",
    "plu": 4435
  },
  {
    "item": "Plums Prune",
    "plu": 4436
  },
  {
    "item": "Plums Red",
    "plu": 4042
  },
  {
    "item": "Pomegranate",
    "plu": 3127
  },
  {
    "item": "Potato Red",
    "plu": 4073
  },
  {
    "item": "Potato Russet Loose",
    "plu": 4072
  },
  {
    "item": "Potato Sweet",
    "plu": 4091
  },
  {
    "item": "Potato White",
    "plu": 4083
  },
  {
    "item": "Potato Yellow",
    "plu": 4727
  },
  {
    "item": "Pumpkin Large",
    "plu": 4736
  },
  {
    "item": "Pumpkin Mini",
    "plu": 4734
  },
  {
    "item": "Pumpkin Pie",
    "plu": 3134
  },
  {
    "item": "Quenepas",
    "plu": 4483
  },
  {
    "item": "Quince",
    "plu": 4447
  },
  {
    "item": "Radicchio",
    "plu": 4738
  },
  {
    "item": "Radish Black",
    "plu": 4739
  },
  {
    "item": "Radish Breakfast",
    "plu": 2178
  },
  {
    "item": "Radish Daikon",
    "plu": 4598
  },
  {
    "item": "Radish Icicle",
    "plu": 2179
  },
  {
    "item": "Radish Organic",
    "plu": 94089
  },
  {
    "item": "Radish Red",
    "plu": 4089
  },
  {
    "item": "Rutabaga",
    "plu": 4095
  },
  {
    "item": "Salad Bar Family",
    "plu": 4688
  },
  {
    "item": "Salad Bar Large",
    "plu": 4689
  },
  {
    "item": "Salad Bar Small",
    "plu": 4428
  },
  {
    "item": "Salad Savoy",
    "plu": 4823
  },
  {
    "item": "Scallion Organic",
    "plu": 94068
  },
  {
    "item": "Shallots",
    "plu": 4662
  },
  {
    "item": "Spinach Organic",
    "plu": 94090
  },
  {
    "item": "Squash Acorn",
    "plu": 4750
  },
  {
    "item": "Squash Buttercup",
    "plu": 4758
  },
  {
    "item": "Squash Butternut",
    "plu": 4759
  },
  {
    "item": "Squash Carnival",
    "plu": 3142
  },
  {
    "item": "Squash Chayote",
    "plu": 4761
  },
  {
    "item": "Squash Delicata",
    "plu": 4763
  },
  {
    "item": "Squash Golden Acorn",
    "plu": 4751
  },
  {
    "item": "Squash Green",
    "plu": 4067
  },
  {
    "item": "Squash Spaghetti",
    "plu": 4776
  },
  {
    "item": "Squash Sweet Dumpling",
    "plu": 4764
  },
  {
    "item": "Squash Turks Turban",
    "plu": 4780
  },
  {
    "item": "Squash White Acorn",
    "plu": 4752
  },
  {
    "item": "Squash Yellow",
    "plu": 4086
  },
  {
    "item": "Star Fruit",
    "plu": 4256
  },
  {
    "item": "String Roll",
    "plu": 4510
  },
  {
    "item": "Sweet Onions",
    "plu": 4166
  },
  {
    "item": "Tangelo",
    "plu": 4383
  },
  {
    "item": "Tangerines",
    "plu": 4055
  },
  {
    "item": "Tomatillo",
    "plu": 4801
  },
  {
    "item": "Tomato Hothouse",
    "plu": 4799
  },
  {
    "item": "Tomato Plum",
    "plu": 4541
  },
  {
    "item": "Tomato Ugly Ripe",
    "plu": 3061
  },
  {
    "item": "Tomato Vine Ripe",
    "plu": 3151
  },
  {
    "item": "Tomato Yellow Green",
    "plu": 4778
  },
  {
    "item": "Tomato on Vine",
    "plu": 94539
  },
  {
    "item": "Turnip Greens",
    "plu": 4587
  },
  {
    "item": "Turnip Purple Top",
    "plu": 4811
  },
  {
    "item": "Turnip White",
    "plu": 4812
  },
  {
    "item": "Turnip Yellow",
    "plu": 4470
  },
  {
    "item": "Uniq Fruit",
    "plu": 4459
  },
  {
    "item": "Banana",
    "plu": 4011
  },
  {
    "item": "Bananas Baby",
    "plu": 4234
  },
  {
    "item": "Bananas Green",
    "plu": 4231
  },
  {
    "item": "Bananas Red",
    "plu": 4236
  },
  {
    "item": "Batata",
    "plu": 4546
  },
  {
    "item": "Beans Green",
    "plu": 4066
  },
  {
    "item": "Beans Sprout",
    "plu": 4536
  },
  {
    "item": "Beets Bunch",
    "plu": 4539
  },
  {
    "item": "Black Radish",
    "plu": 4739
  },
  {
    "item": "Bok Choy",
    "plu": 4545
  },
  {
    "item": "Boston Lettuce Organic",
    "plu": 94632
  },
  {
    "item": "Breadfruit",
    "plu": 4254
  },
  {
    "item": "Breakfast Radish",
    "plu": 2178
  },
  {
    "item": "Bright Light Chard",
    "plu": 4588
  },
  {
    "item": "Broccoli Bunch",
    "plu": 4060
  },
  {
    "item": "Broccoli Crowns",
    "plu": 3082
  },
  {
    "item": "Broccoli Organic",
    "plu": 94567
  },
  {
    "item": "Broccoli Raab",
    "plu": 4547
  },
  {
    "item": "Broccolini",
    "plu": 3277
  },
  {
    "item": "Brussel Sprouts",
    "plu": 4550
  },
  {
    "item": "Bulk Carrots",
    "plu": 896250
  },
  {
    "item": "Cabbage Green",
    "plu": 4069
  },
  {
    "item": "Cabbage Red",
    "plu": 4554
  },
  {
    "item": "Cabbage Savoy",
    "plu": 4555
  },
  {
    "item": "Cactus Leaves",
    "plu": 4558
  },
  {
    "item": "Cactus Pear",
    "plu": 4255
  },
  {
    "item": "Calabaza Squash",
    "plu": 4760
  },
  {
    "item": "Cantaloupe",
    "plu": 4050
  },
  {
    "item": "Cardoon/Cardoni",
    "plu": 4559
  },
  {
    "item": "Carrot Bunch",
    "plu": 4094
  },
  {
    "item": "Carrots Bulk",
    "plu": 838250
  },
  {
    "item": "Casaba Melon",
    "plu": 4330
  },
  {
    "item": "Cauliflower",
    "plu": 4079
  },
  {
    "item": "Cauliflower Organic",
    "plu": 94079
  },
  {
    "item": "Plantain",
    "plu": 4235
  },
  {
    "item": "Belgian Endive",
    "plu": 4543
  },
  {
    "item": "Celery",
    "plu": 4071
  },
  {
    "item": "Celery Root",
    "plu": 4585
  },
  {
    "item": "Chard Bright Light",
    "plu": 4588
  },
  {
    "item": "Chard Green Swiss",
    "plu": 4586
  },
  {
    "item": "Chayote Squash",
    "plu": 4761
  },
  {
    "item": "Cherries",
    "plu": 4045
  },
  {
    "item": "Cherry Ranier",
    "plu": 4258
  },
  {
    "item": "Chestnuts",
    "plu": 4927
  },
  {
    "item": "Chicory",
    "plu": 4604
  },
  {
    "item": "Cilantro",
    "plu": 489
  },
  {
    "item": "Coconuts",
    "plu": 4261
  },
  {
    "item": "Collards",
    "plu": 4614
  },
  {
    "item": "Collards Org",
    "plu": 94614
  },
  {
    "item": "Com White",
    "plu": 4077
  },
  {
    "item": "Corn All",
    "plu": 4078
  },
  {
    "item": "Cucumber",
    "plu": 4062
  },
  {
    "item": "Cucumber Hot House",
    "plu": 4593
  },
  {
    "item": "Cucumber Pickling/gherkin",
    "plu": 4596
  },
  {
    "item": "Culantro",
    "plu": 4508
  },
  {
    "item": "Daikon Radish",
    "plu": 4598
  },
  {
    "item": "Dasheen",
    "plu": 4795
  },
  {
    "item": "Dates",
    "plu": 4263
  },
  {
    "item": "Dill",
    "plu": 4891
  },
  {
    "item": "Donut Peach",
    "plu": 3113
  },
  {
    "item": "Dragon Fruit",
    "plu": 3040
  },
  {
    "item": "Eastern Peach",
    "plu": 4403
  },
  {
    "item": "Eddos (Taro)",
    "plu": 4794
  },
  {
    "item": "Eggplant",
    "plu": 4061
  },
  {
    "item": "Eggplant Baby",
    "plu": 4599
  },
  {
    "item": "Eggplant Graf",
    "plu": 4850
  },
  {
    "item": "Eggplant White",
    "plu": 4602
  },
  {
    "item": "Endive/Chicory",
    "plu": 4604
  },
  {
    "item": "Escarole",
    "plu": 4605
  },
  {
    "item": "Feijoa",
    "plu": 4265
  },
  {
    "item": "Fiddleheads",
    "plu": 4606
  },
  {
    "item": "Figs Black",
    "plu": 4266
  },
  {
    "item": "Figs White / Green",
    "plu": 4268
  },
  {
    "item": "Frisee",
    "plu": 3167
  },
  {
    "item": "Garlic",
    "plu": 4608
  },
  {
    "item": "Ginger Root",
    "plu": 4612
  },
  {
    "item": "Grapefruit Red",
    "plu": 4023
  },
  {
    "item": "Grapefruit Red Organic",
    "plu": 94027
  },
  {
    "item": "Grapes Black",
    "plu": 4056
  },
  {
    "item": "Grapes Green",
    "plu": 4022
  },
  {
    "item": "Grapes Red",
    "plu": 4023
  },
  {
    "item": "Green Asparagus Organic",
    "plu": 94080
  },
  {
    "item": "Green Swiss Chard",
    "plu": 4586
  },
  {
    "item": "Greens Creates",
    "plu": 4620
  },
  {
    "item": "Greens Mustard",
    "plu": 4616
  },
  {
    "item": "Guava",
    "plu": 4299
  },
  {
    "item": "Habanero Pepper",
    "plu": 3125
  },
  {
    "item": "Horse Radish",
    "plu": 4625
  },
  {
    "item": "Icicle Radish",
    "plu": 2179
  },
  {
    "item": "Italian Plum",
    "plu": 3145
  },
  {
    "item": "Jackfruit",
    "plu": 3456
  },
  {
    "item": "Jicama",
    "plu": 4626
  },
  {
    "item": "Kale Greens",
    "plu": 4627
  },
  {
    "item": "Kale Greens Organic",
    "plu": 94627
  },
  {
    "item": "Kiwi fruit",
    "plu": 4030
  },
  {
    "item": "Kohlrabi",
    "plu": 4628
  },
  {
    "item": "Kumquat",
    "plu": 4303
  },
  {
    "item": "Leeks",
    "plu": 4629
  },
  {
    "item": "Leeks Organic",
    "plu": 94629
  },
  {
    "item": "Lemons",
    "plu": 4053
  },
  {
    "item": "Lemons Organic",
    "plu": 94053
  },
  {
    "item": "Lettuce Frise",
    "plu": 3167
  },
  {
    "item": "Lettuce Greenleaf",
    "plu": 4076
  },
  {
    "item": "Lettuce Greenleaf Organic",
    "plu": 94076
  },
  {
    "item": "Lettuce Radichio",
    "plu": 4738
  },
  {
    "item": "Lettuce Red Leaf",
    "plu": 4075
  },
  {
    "item": "Lettuce lceburg",
    "plu": 4061
  },
  {
    "item": "Lettuce Boston",
    "plu": 4632
  },
  {
    "item": "Lettuce Red Leaf Organic",
    "plu": 94075
  },
  {
    "item": "Lettuce Romaine",
    "plu": 4640
  },
  {
    "item": "Lettuce Romaine Organic",
    "plu": 94640
  },
  {
    "item": "Limes",
    "plu": 4048
  },
  {
    "item": "Loose Red Beets",
    "plu": 4541
  },
  {
    "item": "Lychee Nut",
    "plu": 4309
  },
  {
    "item": "Malanga Coco",
    "plu": 4644
  },
  {
    "item": "Mandarin Satsuma",
    "plu": 2134
  },
  {
    "item": "Mango Ataloufo",
    "plu": 4312
  },
  {
    "item": "Mangos",
    "plu": 4051
  },
  {
    "item": "Melon Canary",
    "plu": 4317
  },
  {
    "item": "Melon Cantaloupes",
    "plu": 4050
  },
  {
    "item": "Melon Casaba",
    "plu": 4320
  },
  {
    "item": "Melon Crenshaw",
    "plu": 4322
  },
  {
    "item": "Melon Honeydew",
    "plu": 4329
  },
  {
    "item": "Melon Horned",
    "plu": 4302
  },
  {
    "item": "Melon Pepino",
    "plu": 4333
  },
  {
    "item": "Melon Santa Claus",
    "plu": 4336
  },
  {
    "item": "Mint Bunch",
    "plu": 4896
  },
  {
    "item": "Mushroom Cremini",
    "plu": 4648
  },
  {
    "item": "Mushroom Portabella",
    "plu": 4650
  },
  {
    "item": "Mushroom Portabella Organic",
    "plu": 94650
  },
  {
    "item": "Mushroom Shitake",
    "plu": 4651
  },
  {
    "item": "Mushrooms All",
    "plu": 4085
  },
  {
    "item": "Mustard Greens",
    "plu": 4616
  },
  {
    "item": "Name Costa Rican / Name White (Nyah-may)",
    "plu": 3276
  },
  {
    "item": "Name Root",
    "plu": 4836
  },
  {
    "item": "Name Yellow / Name White (Nyah-may)",
    "plu": 3275
  },
  {
    "item": "Nectarine",
    "plu": 4036
  },
  {
    "item": "Nuts Chestnut",
    "plu": 4927
  },
  {
    "item": "Okra",
    "plu": 4655
  },
  {
    "item": "Onion Boiling",
    "plu": 4658
  },
  {
    "item": "Onion Large Yellow",
    "plu": 4093
  },
  {
    "item": "Onion Red",
    "plu": 4082
  },
  {
    "item": "Onion Scallions",
    "plu": 4068
  },
  {
    "item": "Onion Sets",
    "plu": 4668
  },
  {
    "item": "Onion Shallots",
    "plu": 4662
  },
  {
    "item": "Onion Vidalia",
    "plu": 4159
  },
  {
    "item": "Onion White",
    "plu": 4663
  },
  {
    "item": "Onion White Pearl",
    "plu": 4660
  },
  {
    "item": "Onion Yellow",
    "plu": 4665
  },
  {
    "item": "Onions Sweet",
    "plu": 4166
  },
  {
    "item": "Orange Juice",
    "plu": 4382
  },
  {
    "item": "Orange Navel",
    "plu": 4012
  },
  {
    "item": "Orange Sour",
    "plu": 3109
  },
  {
    "item": "Organic Apple Pink Lady",
    "plu": 94128
  },
  {
    "item": "Organic Avocado",
    "plu": 94225
  },
  {
    "item": "Organic Beets",
    "plu": 94539
  },
  {
    "item": "Organic Boston Lettuce",
    "plu": 94632
  },
  {
    "item": "Organic Braeburn Apple",
    "plu": 94103
  },
  {
    "item": "Organic Broccoli",
    "plu": 94567
  },
  {
    "item": "Organic Bunched Radish",
    "plu": 94089
  },
  {
    "item": "Organic Carrots Bunch",
    "plu": 94094
  },
  {
    "item": "Organic Cauliflower",
    "plu": 94079
  },
  {
    "item": "Organic Collard",
    "plu": 94614
  },
  {
    "item": "Organic Cucumber Hot House",
    "plu": 94593
  },
  {
    "item": "Organic Dandelion Greens",
    "plu": 94615
  },
  {
    "item": "Organic Fuji Apple",
    "plu": 94131
  },
  {
    "item": "Organic Gold Beets",
    "plu": 93273
  },
  {
    "item": "Organic Gold Delicious Apple",
    "plu": 94020
  },
  {
    "item": "Organic Granny Apples",
    "plu": 94017
  },
  {
    "item": "Organic Green Asparagus",
    "plu": 94080
  },
  {
    "item": "Organic Green Grapes",
    "plu": 94022
  },
  {
    "item": "Organic Green Leaf Lettuce",
    "plu": 94076
  },
  {
    "item": "Organic Green Swiss Chard",
    "plu": 94586
  },
  {
    "item": "Organic Kale",
    "plu": 94627
  },
  {
    "item": "Organic Leeks",
    "plu": 94629
  },
  {
    "item": "Organic Lemons",
    "plu": 94053
  },
  {
    "item": "Organic Lettuce Iceburg",
    "plu": 94061
  },
  {
    "item": "Organic Oranges",
    "plu": 94012
  },
  {
    "item": "Organic Parsley",
    "plu": 94899
  },
  {
    "item": "Organic Parsley Curly",
    "plu": 94900
  },
  {
    "item": "Organic Port Mushroom",
    "plu": 94650
  },
  {
    "item": "Organic Radish Bunch",
    "plu": 94089
  },
  {
    "item": "Organic Red Delicious Apple",
    "plu": 94016
  },
  {
    "item": "Organic Red Grapefruit",
    "plu": 94027
  },
  {
    "item": "Organic Red Grapes",
    "plu": 94023
  },
  {
    "item": "Organic Red Leaf",
    "plu": 94075
  },
  {
    "item": "Organic Red Swiss Chard",
    "plu": 94587
  },
  {
    "item": "Organic Romaine",
    "plu": 94640
  },
  {
    "item": "Organic Scallion",
    "plu": 94068
  },
  {
    "item": "Organic Spinach",
    "plu": 94090
  },
  {
    "item": "Organic Tomato",
    "plu": 93151
  },
  {
    "item": "Organic Tomato on Vine",
    "plu": 94664
  },
  {
    "item": "Papaya",
    "plu": 4052
  },
  {
    "item": "Parsley Curly",
    "plu": 4900
  },
  {
    "item": "Parsley Curly Organic",
    "plu": 94900
  },
  {
    "item": "Parsley Italian",
    "plu": 4901
  },
  {
    "item": "Parsley Organic",
    "plu": 94899
  },
  {
    "item": "Parsley Root",
    "plu": 4671
  },
  {
    "item": "Parsnip Bulk",
    "plu": 4672
  },
  {
    "item": "Passion Fruit",
    "plu": 4397
  },
  {
    "item": "Pastel Paper",
    "plu": 4509
  },
  {
    "item": "Peach Donut",
    "plu": 3113
  },
  {
    "item": "Peach Eastern",
    "plu": 4403
  },
  {
    "item": "Peaches",
    "plu": 4038
  },
  {
    "item": "Pears Anjou",
    "plu": 4416
  },
  {
    "item": "Pears Asian",
    "plu": 4408
  },
  {
    "item": "Pears Bartlett",
    "plu": 4024
  },
  {
    "item": "Pears Bosc",
    "plu": 4413
  },
  {
    "item": "Pears Seckel",
    "plu": 4422
  },
  {
    "item": "Peas Snow",
    "plu": 4092
  },
  {
    "item": "Peas Sugar Snap",
    "plu": 4675
  },
  {
    "item": "Pepper Anaheim",
    "plu": 4677
  },
  {
    "item": "Pepper Cubanelle",
    "plu": 4687
  },
  {
    "item": "Pepper Dried",
    "plu": 4713
  },
  {
    "item": "Pepper Green",
    "plu": 4065
  },
  {
    "item": "Pepper Habanero",
    "plu": 3125
  },
  {
    "item": "Pepper Hot",
    "plu": 4691
  },
  {
    "item": "Pepper Orange",
    "plu": 3121
  },
  {
    "item": "Pepper Pablano",
    "plu": 4705
  },
  {
    "item": "Pepper Red",
    "plu": 4688
  },
  {
    "item": "Pepper Red LaRouge",
    "plu": 4088
  },
  {
    "item": "Pepper Yellow",
    "plu": 4689
  },
  {
    "item": "Persimmon Fuyu",
    "plu": 4428
  },
  {
    "item": "Persimmon Hachiya",
    "plu": 4427
  },
  {
    "item": "Pie Pumpkin",
    "plu": 3134
  },
  {
    "item": "Pineapple Lg",
    "plu": 4430
  },
  {
    "item": "Plantains",
    "plu": 4235
  },
  {
    "item": "Plums Black",
    "plu": 4437
  },
  {
    "item": "Plums Green",
    "plu": 4435
  },
  {
    "item": "Plums Prune",
    "plu": 4436
  },
  {
    "item": "Plums Red",
    "plu": 4042
  },
  {
    "item": "Pomegranate",
    "plu": 3127
  },
  {
    "item": "Potato Red",
    "plu": 4073
  },
  {
    "item": "Potato Russet Loose",
    "plu": 4072
  },
  {
    "item": "Potato Sweet",
    "plu": 4091
  },
  {
    "item": "Potato White",
    "plu": 4083
  },
  {
    "item": "Potato Yellow",
    "plu": 4727
  },
  {
    "item": "Pummelo",
    "plu": 3129
  },
  {
    "item": "Pumpkin Large",
    "plu": 4736
  },
  {
    "item": "Pumpkin Mini",
    "plu": 4734
  },
  {
    "item": "Pumpkin Pie",
    "plu": 3134
  },
  {
    "item": "Quenepas",
    "plu": 4483
  },
  {
    "item": "Quince",
    "plu": 4447
  },
  {
    "item": "Radiccho",
    "plu": 4738
  },
  {
    "item": "Radish Black",
    "plu": 4739
  },
  {
    "item": "Radish Breakfast",
    "plu": 2178
  },
  {
    "item": "Radish Daikon",
    "plu": 4598
  },
  {
    "item": "Radish Icicle",
    "plu": 2179
  },
  {
    "item": "Radish Organic",
    "plu": 94089
  },
  {
    "item": "Radish Red",
    "plu": 4089
  },
  {
    "item": "Recao",
    "plu": 4506
  },
  {
    "item": "Red Bananas",
    "plu": 4236
  },
  {
    "item": "Red Beets Loose",
    "plu": 4541
  },
  {
    "item": "Red Swiss Chard",
    "plu": 4587
  },
  {
    "item": "Rhubarb",
    "plu": 4745
  },
  {
    "item": "Rutabaga",
    "plu": 4095
  },
  {
    "item": "Salad Bar Family",
    "plu": 4506
  },
  {
    "item": "Salad Bar Large",
    "plu": 4470
  },
  {
    "item": "Salad Bar Small",
    "plu": 59931
  },
  {
    "item": "Salad Savoy",
    "plu": 4823
  },
  {
    "item": "Scallion Organic",
    "plu": 94068
  },
  {
    "item": "Shallots",
    "plu": 4662
  },
  {
    "item": "Spinach Organic",
    "plu": 94090
  },
  {
    "item": "Squash Acorn",
    "plu": 4750
  },
  {
    "item": "Squash Buttercup",
    "plu": 4758
  },
  {
    "item": "Squash Butternut",
    "plu": 4759
  },
  {
    "item": "Squash Carnival",
    "plu": 3142
  },
  {
    "item": "Squash Chayote",
    "plu": 4761
  },
  {
    "item": "Squash Delicata",
    "plu": 4763
  },
  {
    "item": "Squash Golden Acorn",
    "plu": 4751
  },
  {
    "item": "Squash Green",
    "plu": 4067
  },
  {
    "item": "Squash Spaghetti",
    "plu": 4776
  },
  {
    "item": "Squash Sweet Dumpling",
    "plu": 4764
  },
  {
    "item": "Squash Turks Turban",
    "plu": 4780
  },
  {
    "item": "Squash White Acorn",
    "plu": 4752
  },
  {
    "item": "Squash Yellow",
    "plu": 4086
  },
  {
    "item": "Star Fruit",
    "plu": 4256
  },
  {
    "item": "String Roll",
    "plu": 4510
  },
  {
    "item": "Sunchoke",
    "plu": 4791
  },
  {
    "item": "Sweet Onions",
    "plu": 4166
  },
  {
    "item": "Tangelo",
    "plu": 4383
  },
  {
    "item": "Tangerines",
    "plu": 4055
  },
  {
    "item": "Tomatillo",
    "plu": 4801
  },
  {
    "item": "Tomato HotHouse",
    "plu": 4799
  },
  {
    "item": "Tomato Ugly Ripe",
    "plu": 3061
  },
  {
    "item": "Tomato VineRipe",
    "plu": 3151
  },
  {
    "item": "Tomato Yellow Green",
    "plu": 4778
  },
  {
    "item": "Tomato on Vine",
    "plu": 4664
  },
  {
    "item": "Bagel / Cream Cheese",
    "plu": 424
  },
  {
    "item": "Bagels Each",
    "plu": 1655
  },
  {
    "item": "Condiment Cup",
    "plu": 437
  },
  {
    "item": "Danish/Pastry",
    "plu": 625
  },
  {
    "item": "Donuts Each",
    "plu": 620
  },
  {
    "item": "Hot Bar",
    "plu": 775
  },
  {
    "item": "Muffin Each",
    "plu": 402
  },
  {
    "item": "Olive Bar",
    "plu": 727
  },
  {
    "item": "Rolls Each",
    "plu": 426
  },
  {
    "item": "Tomato Plum",
    "plu": 4087
  },
  {
    "item": "Turnip Greens",
    "plu": 4619
  },
  {
    "item": "Turnip Purple",
    "plu": 4811
  },
  {
    "item": "Turnip White",
    "plu": 4812
  },
  {
    "item": "Turnip Yellow",
    "plu": 4095
  },
  {
    "item": "Uniq Fruit",
    "plu": 4459
  },
  {
    "item": "Water Coconuts",
    "plu": 4260
  },
  {
    "item": "Watermelon Baby",
    "plu": 3421
  },
  {
    "item": "Watermelon Seedless",
    "plu": 4032
  },
  {
    "item": "Watermelon Whole",
    "plu": 4031
  },
  {
    "item": "Wing Bar-Hot",
    "plu": 904
  },
  {
    "item": "Yams",
    "plu": 4074
  },
  {
    "item": "Yautia Red",
    "plu": 4834
  },
  {
    "item": "Yautia White",
    "plu": 4839
  },
  {
    "item": "Yellow Potato",
    "plu": 4727
  },
  {
    "item": "Yucca Root",
    "plu": 4819
  }
]

'''

# Parse the JSON data
data = json.loads(json_data)

# Sort and remove duplicates
sorted_data = sort_and_remove_duplicates(data)

# Print the sorted JSON array without duplicates
print(json.dumps(sorted_data, indent=2))
