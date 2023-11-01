def my_function(a, b, c):  # pareameter
    print(f"do this with {a}\n")
    print(f"do this with {b}\n")
    print(f"do this with {c}")


my_function("k", "g", "k")  # argument

print("--------------------------------------------------------------------")

# functions with more than 1 input


def my_function2(name, location):
    print(f"hi!{name}")
    print(f"location is {location}")


my_function2("harshad", "thane")
print("--------------------------------------------------------------------")

# to understand

# we use argument with sigh asign parameter

# we assign parameter with argument when we change position of argument we write like this


def my_function2(name, location):
    print(f"hi!{name}\n")
    print(f"location is {location}\n")


my_function2(location="thane", name="harshad")
