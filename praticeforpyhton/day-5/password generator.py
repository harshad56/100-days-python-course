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


genrate_password_inlist = []

for char in range(1, type_letters+1):
    genrate_password_inlist.append(random.choice(letters))

for char in range(1, type_numbers+1):
    genrate_password_inlist.append(random.choice(numbers))

for char in range(1, type_symbols+1):
    genrate_password_inlist.append(random.choice(symbols))

print(genrate_password_inlist)

# -----------------------------------------------------------------
random.shuffle(genrate_password_inlist)
print(genrate_password_inlist)

# -----------------------------------------------------------------
converatelist_into_char_password = ""  # convert list into char password

for i in genrate_password_inlist:
    converatelist_into_char_password += i

print(converatelist_into_char_password)
