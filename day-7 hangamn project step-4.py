import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

end_of_game = False
word_list = ["apple", "bannana", "carrot"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Todo-1:create  a variable called "lives" to keep track of the number of lives left
# set "lives" to equal 6.
lives = 6

# testing a cose
print(f"passat,the solution is {chosen_word}.")

# create a blanks
Display = []
for _ in range(word_length):
    Display += "_"


while not end_of_game:
    guess = input("guess a letter: ").lower()

    # checked a guees letter

    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"current position:{position}\n current letter:{letter}\n guessed letter:{guess}")
        if letter == guess:
            Display[position] = letter

    # Todo-2:if guess is not a letter in the chosen_word,
    # then reduce "lives"by 1.
    # if lives goes down to ) then the game should stop and it should print "you lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose.")
    # join all elements in the list and turn it into  string.
    print(f"{''.join(Display)}")

    # check if user has got all letters.
    if "_" not in Display:
        end_of_game = True
        print("you win.")

    # Todo-3:print the ascii art from "stages" that corresponding to the current number of lives the user has remaining .
    print(stages[lives])
