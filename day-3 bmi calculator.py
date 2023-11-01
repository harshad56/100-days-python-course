# height = float(input("enter your height in m:"))
# weight = float(input("enter your weight in m:"))

# BMI = round(weight/height**2)
BMI = 18
if BMI < 18.5:
    print(f"your bmi is{BMI},you are underweight.")
elif BMI < 25:
    print(f"your bmi is{BMI},you arr normal.")
elif BMI < 30:
    print(f"your bmi is{BMI},you are overweight.")

elif BMI < 35:
    print(f"yoiur bmi is{BMI},you are obese.")

else:
    print(f"your bmi is{BMI},you are cinically obese .")
