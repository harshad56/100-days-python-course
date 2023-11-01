#### balckjack project ####

# difficulty normal:use all hints below to complete the project>
# difficulty hard: use only hints 1,2,3 to complte the project.
# difficulty extra hard : only use hints 1&2 to complte the project.
# difficulty Expert: only use hint 1 to complte the project.
#--------------------------------------------------------------------#

########### blackjack house rules ###########

# the deck is unlimited in size.
# there are not jokers.
# the jack/queen/king all count as 19.
# the ace can count as 11 or 1.
# use the following list as the deck of cards.
import random
logo = {'''
___.    .__                    __         __                  __           ____                            
\_ |__  |  |  _____     ____  |  | __    |__|_____     ____  |  | __      / ___\ _____     _____    ____   
 | __ \ |  |  \__  \  _/ ___\ |  |/ /    |  |\__  \  _/ ___\ |  |/ /     / /_/  >\__  \   /     \ _/ __ \  
 | \_\ \|  |__ / __ \_\  \___ |    <     |  | / __ \_\  \___ |    <      \___  /  / __ \_|  Y Y  \\  ___/  
 |___  /|____/(____  / \___  >|__|_ \/\__|  |(____  / \___  >|__|_ \    /_____/  (____  /|__|_|  / \___  > 
     \/            \/      \/      \/\______|     \/      \/      \/                  \/       \/      \/  
                                                                                                           
'''}
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# the cards in the the list have equal probabilty of being drawn.
# cards are not removed from the deck as they are drawn.

#-----------------------------------------------------------------------------#

####### --------hints---------- #######

# hint1
# hint2
# hint3
# all there hint are in video

# hint 4 : create a deal_card() function that uses  the list below to * return*  a random card .
# 11 is Ace.


def deal_card():
    """return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# hint 6: create a function called calculate_score()take a list of cards  as input  and returns the scrore
# look up  sum() function to help you do this


def calculate_score(cards):
    """ take a list of cards and return the score calculated from the cards"""
    # hint 7: inside calculate_score()the check for blackjack (a hand with only 2 cards: ace+10) and return 0 instead of the actual score. 0 will represent a  blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # hint8: inside calculate_score ()check for an 11(ace).if the score is alredy over 23 remove the 11 and replace it with a 1. you might need to look up append() and remove.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# hint 13: create a function callde comapare() and pass in user_score and computer _score .if the computer and user both have the same score, then its draw. if the computer has a balckjack (0),then the user loses , if the  user has a blackjack(0),then user wins. if the user_score is over 21, then the user loses, if the computer_score is over is 21,then the computer loses if none of the above then the player with highest score wins .


def comapare(user_score, computer_score):
    if user_score == computer_score:
        return "draw😒"  # uses window + . key for emoji
    elif computer_score == 0:
        return "loses,oppnent has balckjack😱"
    elif user_score == 0:
        return "win with a blackjack😎"
    elif user_score > 21:
        return "you went over.your loss😭"
    elif computer_score > 21:
        return "opponent went over. you win😁👍"
    elif user_score > computer_score:
        return "you win😊"
    else:
        return "you lose😭😤😨🫠"


def play_game():
    # hint 5:deal the user and computer 1 cards each using deal_cards()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # hint 11: the score will need to be rechecked with every new card drawn and the check is hint9 need to be repeated until the game ends.
    while not is_game_over:

        # hint 9: call calculate_score().if the computer or the user has a balckjack (0)or if the user score is over 21 then the game ends
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" your cards:{user_cards},current score:{user_score}")
        print(f"computer first card:{computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score == 21:
            is_game_over = True
        else:
            # hint 10: if the  game has not ended, ask the user if they want to draw another card if yes , then use the deal_card() function to add another card to user_cards list. if no then the game has ended
            user_should_deal = input(
                "type 'y'to get another card,type'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # hint 12: once the user is done, its  time to let the computer play the computer should keep drawing cards as long as it has  a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"your final hand:{user_cards},final score:{user_score}")
    print(f"computer final hand:{computer_cards},final score:{computer_score}")
    print(comapare(user_score, computer_score))


# hint 14: ask the user if they want to restart the game. if they answer  yes clear the console and start a new game of blackjack and show the logo from art.py.
while input("do you want play a game of blackjack?type'y' or'n'") == "y":
    play_game()
