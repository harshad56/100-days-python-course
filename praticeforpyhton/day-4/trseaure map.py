import random

line1 = ["", "", ""]
line2 = ["", "", ""]
line3 = ["", "", ""]
map = [line1, line2, line3]
print("hiding your treasure (x marks the spot).")
print(f"{line1}\n{line2}\n{line3}\n")

postion = int(input("Where do you want to put the treasure? (0, 1, 2): "))

if postion == 0:
    map_choice = random.randint(0, 2)
    map[map_choice][0] = "x"
elif postion == 1:
    map_choice = random.randint(0, 2)
    map[map_choice][1] = "x"
elif postion == 2:
    map_choice = random.randint(0, 2)
    map[map_choice][2] = "x"

print(f"{line1}\n{line2}\n{line3}\n")
