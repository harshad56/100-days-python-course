programming_dictionary = {
    "Bug": "An errror in a program that prevents the program from running as expected",
    "Function": " A piece of code you can easily call over and over agian"
}
# reterving items from dictionary
# print(programming_dictionary["bug"])

# ----------------------------------------------------------------------------

# adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over  and over again"
# print(programming_dictionary)

# ---------------------------------------------------------------------------

# creating a empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary={}
# print(programming_dictionary)

# ----------------------------------------------------------------------------

# edit an iteam in a dictionary
programming_dictionary["Bug"] = "a moth in your computer"
# print(programming_dictionary)

# ----------------------------------------------------------------------------

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
