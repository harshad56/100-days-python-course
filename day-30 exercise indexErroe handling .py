fruits = ["Apple", "pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except:
        print("fruit pie")
    else:
        print(fruit+"pie")


make_pie(4)
