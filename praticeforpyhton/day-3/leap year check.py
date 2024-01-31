print("leap year checker.")

year = int(input("write a year you want to check: "))

if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:
            print("it is a leap year")
        else:
            print("it is not a leap year")

    else:
        print("it is  a leap year")
else:
    print("it is not a leap year")
