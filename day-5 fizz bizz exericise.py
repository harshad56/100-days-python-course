for num in range(1, 20):

    if num % 3 == 0 and num % 5 == 0:
        print("fizzbizz")

    elif num % 3 == 0:
        print("fizz")

    elif num % 5 == 0:
        print("bizz")

    else:
        print(num)
