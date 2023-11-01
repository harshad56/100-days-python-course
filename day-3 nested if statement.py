print("welcome to the rollercoster")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoster")
    age = int(input("what is your age?: "))
    if age < 12:
        print("you pay $5")
    elif age >= 18:
        print("please pay $8")

    elif age > 22:
        print("you can pay 78$")

    else:
        print("please pay $50")

else:
    print("sorry,yopu have to grow taller before you can ride.")
