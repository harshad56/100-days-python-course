number = int(input("enter the number to check is prime number or not:"))


def prime_checker(prime_number):
    print("using if-else")
    if(number % 2 == 0):
        print(F"{prime_number} is not prime number")
    else:
        # prime number means thats are number not divisible by 2 and remainder not get 0
        print(F"{prime_number} is prime number")


prime_checker(prime_number=number)

print("-------------------------------------------------------")


def prime_check(prime_number1):
    print("using for loop")
    is_prime = True
    for i in range(2, number):
        if number % 2 == 0:
            is_prime = False
    if is_prime:
        print(f"{prime_number1} is prime number")

    else:
        print(f"{prime_number1} is not prime number")


prime_check(prime_number1=number)
