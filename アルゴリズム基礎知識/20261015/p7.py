import random
items=[]
for y in range(3):
    row=[]
    for x in range(3):
        num=random.randint(0,1)
        row.append(num)
    items.append(row)
print(items)
