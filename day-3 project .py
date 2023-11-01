print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("welcome to the treasure island")
print("your mission to the find the treaure")

choice1 = input(
    'you are at a crossroad,where do you want to go "left" or "right":').lower()
if choice1 == "left":

    choice2 = input(
        'you a come to a lake,there is a island in the middle of the lake ,type"wait"to wait for a boat,type "swim" to swim across:').lower()
    if choice2 == "wait":

        choice3 = input(
            "you arrive at the island unharred, there is a 3 doors. one is red ,one yellow and one is blue: ")
        if choice3 == "red" or choice3 == "Red" or choice3 == "RED":
            print(" you choose wrong door.it's a room of fire, game over")

        elif choice3 == "yellow" or choice3 == "Yellow" or choice3 == "YELLOW":
            print(" you choose wrong door.in the room a hungry lion, game over")

        elif choice3 == "blue" or choice3 == "Blue" or choice3 == "BLUE":
            print("you chhose correct door .you found treaure,congruglaitons")

        else:
            print("you choose the door is the not exist,game over")

    else:
        print("you are attacked by angry tort,game over")

else:
    print("you fell in the hole,game over")
