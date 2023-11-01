from higher_lower import art, logo
from game_data import data
import random
import os
# ---------------------------------------------------------------------------------------------------------
# format  the account data into printable format


def edit_data(account):
    """format  the account data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    acount_country = account["country"]
    return (f"{account_name},a {account_description},from {acount_country}")


# -------------------------------------------------------------------------------------------------------------
# take the user guess and follower counts and returns if they got it right


def check_answer(guess, a_follower, b_follower):
    """ake the user guess and follower counts and returns if they got it right"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


# -------------------------------------------------------------------------------------------------
# display art
print(art)
score = 0
# -------------------------------------------------------------------------------------------------------
# make a game repatable
game_shold_continue = True
while game_shold_continue:
    # genrate  a random account from the game data
    account_a = random .choice(data)
    account_b = random .choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A:{edit_data(account_a)}")
    print(logo)
    print(f"against B:{edit_data(account_b)}")

    # -----------------------------------------------------------------------------------------------------------

    # ask user for a guess

    guess = input("who has more folllwer? A or B:").lower()

    # -----------------------------------------------------------------------------------------------------------

    # get follower count of each account

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # -----------------------------------------------------------------------------------------------------------
    # clear the screen between rounds

    os.system('cls')
    print(art)
    # ------------------------------------------------------------------------------------------------
    # score  keeping

    if is_correct:
        score += 1
        print(f"you're right! current score is: {score}.\n")

    else:
        game_shold_continue = False
        print(f"sorry,that's  wrong .final score is :{score}\n")
