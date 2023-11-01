# step 3

import random
word_list = ["apple", "bannana", "carrot"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# testing a cose
print(f"passat,the solution is {chosen_word}.")

# create a blanks
Display = []
for letter in range(word_length):
    Display += "_"

# todo-1:- use a while  loop  to let the user guess again.the loop should only step once the user has guessed all the letters in the chosen_word and Display has no more balnks("_") mthen you can tell the user they won
end_of_game = False

while not end_of_game:
    guess = input("guess a letter: ").lower()

    # checked a guees letter

    for position in range(word_length):
        leter = chosen_word[position]
        print(
            f"current position:{position}\n current letter:{letter}\n guessed letter:{guess}")
        if letter == guess:
            Display[position] = letter

    print(Display)

    if "_" not in Display:
        end_of_game = True
        print("you win.")
