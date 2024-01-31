print("welcome to the rollercoster.")

height = int(input("what is your height in cm: "))

if height >= 165:
    print("you can ride the rollercoster")

    age = int(input("what is your age : "))

    if age >= 18 and age <= 21:
        print("rollercoster entry fee is $123 ")

    elif age >= 15 and age < 18:
        print("rollercoster entry fee is $120 ")

    elif age >= 10 and age < 15:
        print("rollercoster entry fee is $110")

    else:
        print("you pay $500")

else:
    print("you can't ride the rollercoster")
