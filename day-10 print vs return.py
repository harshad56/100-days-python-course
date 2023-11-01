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
num1 = int(input("what is your first number?:"))
num2 = int(input("waht is your second number?:"))

for symbol in operations:
    print(symbol)
opeartion_symbol = input("pick an operation from the line above:")

calculation_function = operations[opeartion_symbol]

fisrt_time_answer = calculation_function(num1, num2)

print(f"{num1} {opeartion_symbol} {num2} = {fisrt_time_answer}")
# ------------------------------------------------------------------------------

opeartion_symbol = input("pick an another operation :")
num3 = int(input("waht is your next number?:"))
calculation_function = operations[opeartion_symbol]
second_time_answer = calculation_function(fisrt_time_answer, num3)

print(f"{fisrt_time_answer} {opeartion_symbol} {num3} = {second_time_answer}")
