inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
#print(inventory)
#==============calculate the totalrevenue==================
# totalrevenue=0
# for i in inventory:
#     totalrevenue+=i[2]*i[3]
# print(totalrevenue)
#=================list the low stock element======================
# items=[]
# for i in inventory:
#     if(i[4]<5):
#         items.append(i[0])
# print(f'low stock items:{items}')
#=======================calculate the categorywise revenue==============
for i in inventory:
    if i=="fruits":
        fruit_revenue.append()