# error getting code
year = input("enter a year to ,check its leap year or not:")  # here error

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap yaer")
else:
    print("not a leap year")
# ------------------------------------------------------------------------------

# fixed code
year = int(input("enter a year to ,check its leap year or not:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap yaer")
else:
    print("not a leap year")
