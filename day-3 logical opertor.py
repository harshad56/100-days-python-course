print("welcome to the rollercoster")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
    print("you can ride the rollercoster")
    age = int(input("what is your age?: "))
    if age < 12:
        bill = 5
        print("you pay $5")

    elif age >= 18 and age <= 19:
        bill = 7
        print("child pay $7")

    elif age >= 22 and age <= 25:
        bill = 8
        print("youth pay 8$")

    elif age >= 45 and age <= 55:
        print("you ride free from us")

    else:
        bill = 10
        print("adult pay $10")

    wants_photo = input("do you want a photo taken? yes or no. ")
    if wants_photo == "yes":
        # add$3 to their bill
        bill += 3

        print(f"your final bill{bill}")

    else:
        print("thanks you")


else:
    print("sorry,yopu have to grow taller before")
