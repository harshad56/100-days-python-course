height = float(input("height:"))
weight = int(input("weight:"))

if height > 3:
    raise ValueError("human height should not be over 3 meters")

bmi = weight/height**2

print(bmi)
