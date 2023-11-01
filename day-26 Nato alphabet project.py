import pandas
data = pandas.read_csv("nato_alphabet_.csv")
# print(data.to_dict())

# Todo-1: Create a dictionary in this foramt

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(phonetic_dict)

# Todo-2: Create a list of the phoetic code words from a word that the user inputs

word = input("Enter a word:").upper()

output_list = [phonetic_dict[letters] for letters in word]

print(output_list)
