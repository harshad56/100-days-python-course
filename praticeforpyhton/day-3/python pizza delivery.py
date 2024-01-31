print("thank for chosing the python delivery.")

size = input("what size of pizza you want? S,M,L :").capitalize()
bill = 0
if size == "S":
    bill += 15
    add_peperoni = input(
        "do you want to add pepperoni ? Y or N :").capitalize()
    if add_peperoni == "Y":
        bill += 2

    elif add_peperoni == "N":
        print("check for cheese option")

    extra_cheese = input("do you want extra cheese? Y or N:").capitalize()
    if extra_cheese == "Y":
        bill += 1
        print(f"your bill is ${bill}")
        print("thanks for ordering")

    elif extra_cheese == "N":
        print(f"thanks for ordering{bill}")


elif size == "M":
    bill += 20
    add_peperoni = input(
        "do you want to add pepperoni ? Y or N :").capitalize()
    if add_peperoni == "Y":
        bill += 3

    elif add_peperoni == "N":
        print("check for cheese option ")

    extra_cheese = input("do you want extra cheese? Y or N:").capitalize()
    if extra_cheese == "Y":
        bill += 1
        print(f"your bill is ${bill}")
        print("thanks for ordering")

    elif extra_cheese == "N":
        print(f"thanks for ordering{bill}")


elif size == "L":
    bill += 25
    add_peperoni = input(
        "do you want to add pepperoni ? Y or N :").capitalize()
    if add_peperoni == "Y":
        bill += 3

    elif add_peperoni == "N":
        print("check for cheese option ")

    extra_cheese = input("do you want extra cheese? Y or N:").capitalize()
    if extra_cheese == "Y":
        bill += 1
        print(f"your bill is ${bill}")
        print("thanks for ordering")

    elif extra_cheese == "N":
        print(f"thanks for ordering{bill}")
