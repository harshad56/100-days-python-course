print(" claculate your body mass index.")

height = float(input("what is your height in m:"))

weight = int(input(" write your weight:"))

bmi = weight/height**2


if bmi <= 18.5:
    print(f" your bmi is {bmi} you are underweight ")

elif bmi > 18.5 and bmi <= 25:
    print(f"your bmi is {bmi} you are Normal weight ")

elif bmi > 25 and bmi <= 30:
    print(f"your bmi is {bmi} you are slightly over weight")

elif bmi > 30 and bmi <= 35:
    print(f"your bmi is {bmi} you are obese")

else:
    print(f"your bmi is {bmi} you cliniclally obese")
