from random import randint
from number_logo import logo

EASY_LEVEL_TURNS = 10  # USED AS GLOBAL VARIABLE IN A FUNCTION
HARD_LEVEL_TURNS = 5  # USED AS GLOBAL VARIABLE IN A FUNCTION
#-------------------------------------------------------------------------#

# function to check a user guess against actual answer.


def check_answer(guess, answer, turns):
    """ cnecks anser against guess returns the number4 of turns reamining"""
    if guess > answer:
        print("To high.")
        return turns - 1
    elif guess < answer:
        print("To low.")
        return turns - 1
    else:
        print(f"you got the answer,the answer was:{answer}")

# make function  to set difficulty


def set_difficuilty():
    level = input("choose a difficulty.type a 'easy' or'hard':")
    if level == 'easy':
        return EASY_LEVEL_TURNS  # global variable
    else:
        return HARD_LEVEL_TURNS  # global variable
#----------------------------------------------------------------------------#


def game():
    print(logo)
    # chossing a random number between 1 and 100
    print("welcome to the number guessing game!")
    print("i'am thinking of a number between 1 and 100")
    answer = randint(1, 100)  # global variable

    # for set difficulty
    turns = set_difficuilty()  # global variable

    # repeat  the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f" you have{turns} attempts reamining to guess the number.")

        # let the user guesss a number.
        guess = int(input("make a guess:"))  # global variable

        # calling check_answer()
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f" you've run out og guess you lose")
            return
        elif guess != answer:
            print("guess again")


# track the number of turns and reduce  by 1 if they get it wrong.

game()
