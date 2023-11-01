# bug and error getting
for num in range(1, 20):

    if num % 3 == 0 or num % 5 == 0:  # bug 'or'
        print("fizzbizz")

    if num % 3 == 0:  # bug "if"
        print("fizz")

    if num % 5 == 0:  # bug "if"
        print("bizz")

    else:
        print([num])  # error[]

print("------------------------------------------------------------")
# ------------------------------------------------------------------------------
# fixed code
for num in range(1, 101):

    if num % 3 == 0 and num % 5 == 0:
        print("fizzbizz")

    elif num % 3 == 0:
        print("fizz")

    elif num % 5 == 0:
        print("bizz")

    else:
        print(num)
