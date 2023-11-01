# step1

# picking a random words and checking answers
import random
word_list = ["apple", "bannna", "cat"]


# Todo-1-randomaly choose a word from the word_list and assign to the variable  called chosen_word

chosen_word = random.choice(word_list)

# Todo-2 ask the user to guess a letter and assign their answer to variable called guess. make guess lowercase.

guess = input("guess a letter:").lower()

# Todo-3 check if the letter the  user guested(guess )is one of the letter in the choosen_word.

for letter in word_list:
    if letter == guess:
        print("true")
    else:
        print("false")
