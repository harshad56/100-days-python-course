age = input("what is your age")

age_as_int = int(age)
years_reaming = 90-age_as_int
days_reaming = years_reaming*365
weeks_reaming = years_reaming*52
months_reaming = years_reaming*12

print(
    f"you have days:{days_reaming},weeks:{weeks_reaming} and month:{months_reaming}reamining")
