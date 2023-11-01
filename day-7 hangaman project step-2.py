# step-2
import random
word_list = ["apple", "bannana", "carrot"]
chosen_word = random.choice(word_list)

# testing a cose
print(f"passat,the solution is {chosen_word}.")


# Todo-1:- Create An Empty List Caled Display.
# For each  Letter In The  Chosen_word ,add a"_"to "dispaly"
# so if the chosen_word was "apple",display should be ["_" , "_", "_", "_","_"]with 5 "_" representing each letter to guess
Display = []
word_lenght = len(chosen_word)
for letter in range(word_lenght):
    Display += "_"
print(Display)

# Display = []
# for letter in chosen_word:
#     Display += "_"
# print(Display)

guess = input("guess a letter: ").lower()

# Todo-2 :- loop through eah position in the chosen_word;
# if the letter at that position matches "guess" then reveal that letter in the display at that position.
# e,g if the user guessed "p" and the chosen word was "apple" then display Should be ["_", "p", "p" ,"_" , "_"].

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        Display[position] = letter


# Todo-3:- print "display"and you should see the guessed letter in the correct position and every other letter replace with "_"

print(Display)
