print("welocome to our site pizza hut")

want_pizza = input("do you want a pizza? Y or N:")

if want_pizza == "Y" or "yes" or "y":

    bill = 0
    size = input("what size of pizza you want? S,M orL:")
    if size == "S":
        bill += 10

        add_peoproni = input("want a peoproni on pizza ? Y or N:")
        if add_peoproni == "Y":
            bill += 3

        elif add_peoproni == "N":
            print("check the cheese option")

        add_cheese = input("do you want a extra cheese? Y or N:")
        if add_cheese == "Y":
            bill += 4
            print(f"bill is:{bill}")
            print("thanks for ordering")

        elif add_cheese == "N":
            print("thanks for ordering")

# ------------------------------------------------------------------------------

    elif size == "M":
        bill += 20
    add_peoproni = input("want a peoproni on pizza ? Y or N:")
    if add_peoproni == "Y":
        bill += 3

    elif add_peoproni == "N":
        print("check the cheese option")

    add_cheese = input("do you want a extra cheese? Y or N:")
    if add_cheese == "Y":
        bill += 4
        print(f"bill is:{bill}")
        print("thanks for ordering")

    elif add_cheese == "N":
        print("thanks for ordering")


# ------------------------------------------------------------------------------

    elif size == "L":
        bill += 30
    add_peoproni = input("want a peoproni on pizza ? Y or N:")
    if add_peoproni == "Y":
        bill += 3

    elif add_peoproni == "N":
        print("check the cheese option")

    add_cheese = input("do you want a extra cheese? Y or N:")
    if add_cheese == "Y":
        bill += 4
        print(f"bill is:{bill}")
        print("thanks for ordering")

    elif add_cheese == "N":
        print("thanks for ordering")


else:
    print("thanks for coming on website")
