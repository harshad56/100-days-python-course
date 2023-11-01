print("welcome to love calculator")
name1 = input("what is your name? \n")
name2 = input("what is their name? \n")

combined_string = name1+name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l+o+v+e


love_score = int(str(true)+str(love))

if (love_score == 0) or (love_score < 10) or (love_score > 90):
    print(f" your love score is{love_score},love is like coke and melode")

elif (love_score >= 40) and (love_score <= 50):
    print(f"your love score is{love_score},your are always together.")

else:
    print(f"your love score is:{love_score}.")
