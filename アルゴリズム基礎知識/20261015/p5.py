import random
items=[None]*12
def a():
    for i in range(12):
        items[i]=random.randint(0,1)
        print(items[i])
a()    