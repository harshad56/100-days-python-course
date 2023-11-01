import calculator
print(calculator.calculator)
# add


def add(n1, n2):
    """ they add two numbers"""
    return n1+n2

# subtract


def sub(n1, n2):
    """ they subtract two numbers"""
    return n1-n2

# multiply


def mul(n1, n2):
    """ they multiply two numbers"""
    return n1*n2

# divide


def div(n1, n2):
    """ they divide two numbers"""
    return n1/n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calcualtor():  # recursion step-1
    num1 = float(input("what is your first number?:"))
    num2 = float(input("waht is your next  number?:"))

    for symbol in operations:
        print(symbol)
    should_continue = True  # flags

    while should_continue:
        opeartion_symbol = input("pick an operation :")

        calculation_function = operations[opeartion_symbol]

        answer = calculation_function(num1, num2)

        print(f"{num1} {opeartion_symbol} {num2} = {answer}")

        if input(f"type 'y' to continue calculating with{answer},or type'n' to star a new calculation :").lower() == "y":
            num1 = answer
        else:
            should_continue = False  # flags
            calcualtor()  # recursion step-3


calcualtor()  # recursion step-2
