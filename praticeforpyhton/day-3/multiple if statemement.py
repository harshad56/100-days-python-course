print("welcome to the rollercoster.")

height = int(input("what is your height in cm: "))
bill = 0

if height >= 165:
    print("you can ride the rollercoster")

    age = int(input("what is your age : "))

    if age >= 18 and age <= 21:
        bill = 123
        print("rollercoster entry fee is $123 ")

    elif age >= 15 and age < 18:
        bill = 120
        print("rollercoster entry fee is $120 ")

    elif age >= 10 and age < 15:
        bill = 110
        print("rollercoster entry fee is $110")

    else:
        bill = 500
        print("you pay $500")

    wants_photo = input("want a photo? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"your bill is :{bill}")


else:
    print("you can't ride the rollercoster")
