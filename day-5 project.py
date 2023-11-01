# password generator

import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

print("welcome to the password generator")

type_letters = int(
    input("how many letters would you like in your password?\n"))

type_numbers = int(
    input("how many numbers would you like in your password?\n"))
type_symbols = int(
    input("how many symbols would you like in your password?\n"))

# easy version
# 1234fgh#$ example:- contain first letters second numbers then symbils

# password = ""

# for char in range(1, type_letters+1):
#     password += random.choice(letters)

# for char in range(1, type_numbers+1):
#     password += random.choice(numbers)

# for char in range(1, type_symbols+1):
#     password += random.choice(symbols)

# print(password)
# ------------------------------------------------------------------------------

# hard version
# hard password type means all lettters num and symbols are suffle randomly

password_list = []

for char in range(1, type_letters+1):
    password_list.append(random.choice(letters))

for char in range(1, type_numbers+1):
    password_list.append(random.choice(numbers))

for char in range(1, type_symbols+1):
    password_list.append(random.choice(symbols))

print(password_list)  # only list output get before suffle


random.shuffle(password_list)
print(password_list)  # only list output get after suffle

password = ""
for char in password_list:
    password += char

print(f" your password is:{password}")
