# list comprehension
# for numberrs
numbers = [1, 2, 3]

new_numbers = [n+1 for n in numbers]
print(new_numbers)

# ------------------------------------------------------------------
# for letters
name = "Harshad"

letters_list = [letter for letter in name]
print(letters_list)

# -----------------------------------------------------------------------
# for range function
range_list = [num*2 for num in range(1, 5)]
print(range_list)

# ----------------------------------------------------------------------------

# conditional list comprehension

# example:- new_list=[new item for item in list if test]

names = ["harshad", "devendra", "jay", "dishant", "rohit"]

short_name = [n for n in names if len(n) < 5]

capitilize_name = [n.upper() for n in names if len(n) >= 5]

print(short_name)
print(capitilize_name)
