# error getting code
# age=input("how old are you:")# not write int for getting numbers only
# if age >18:
# print("tou can drive car ")# indentaion error

# -----------------------------------------------------------------------
# fixed code
age = int(input("how old are you:"))  # int
if age >= 18:
    print(f"you can drive the car👍 at age:{age} ")

elif age < 18:  # some extra code for free from errors
    print(f"you can't drive bro at age:{age}🫠")
