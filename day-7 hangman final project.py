from hangman_logo import logo, stages
import random

# Todo-1: update the word list to use the "word_list" fro  hangman_words.py

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Todo-2:import the logo from hangman_logo.py and print it at the start of the page
print(logo)


# create a blanks
Display = []
for _ in range(word_length):
    Display += "_"

while not end_of_game:
    guess = input("guess a letter: ").lower()

    # todo-3:if the user enterend a letter they we alerady guessed print the letter and let them know.
    if guess in Display:
        print(f"{guess}is  you already guessed")

        # checked a guees letter

    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"current position:{position}\n current letter:{letter}\n guessed letter:{guess}")
        if letter == guess:
            Display[position] = letter

    # check if user is wrong
    if guess not in chosen_word:
        # todo-4: if the letter is  not in the chosen_word print out the letter and let them know not in the  word.
        print(f"you guessed {guess},that not in the word.you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose.")

    # join all elements in the list and turn it into  string.
    print(f"{''.join(Display)}")

    # check if user has got all letter.
    if "_" not in Display:
        end_of_game = True
        print("you win.")

    # Todo-4:import the stages from hangman_logo.py and make this error go away.
    print(stages[lives])
