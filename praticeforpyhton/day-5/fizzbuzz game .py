userinput = int(input("write  an number 1 to whatever you want to:"))


for i in range(0, userinput+1):
    if i % 3 == 0 and i % 5 == 0:

        print("fizzbuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
