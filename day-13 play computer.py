# not executing code
year = int(input("what's your year of birth: "))
if year > 1980 and year < 1994:
    print(" you are old man.")

elif year > 1994:
    print("you are a gen z.")

# -----------------------------------------------------------------------------

# fixed code
year = int(input("what's your year of birth: "))
if year >= 1980 and year < 1994:
    print(" you are old man.")

elif year >= 1994:
    print("you are a gen z.")

else:
    print("your are very old man.")
