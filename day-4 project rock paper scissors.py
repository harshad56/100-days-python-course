import random
# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_image = [rock, paper, scissors]

user_choice = int(input(
    "what do you choose type 0 for rock ,type 1 for paper and 2 for scissors.\n"))
print("your choice:-")

if user_choice >= 3 or user_choice < 0:
    print("invalid number")
else:
    print(game_image[user_choice])

    computer_choice = random.randint(0, 2)
    print("computer choice is:-")
    print(game_image[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("you wins")

    elif user_choice == 2 and computer_choice == 0:
        print("you lose")

    elif user_choice == 1 and computer_choice == 2:
        print("you lose")

    elif user_choice == 2 and computer_choice == 1:
        print("you win")

    elif user_choice == 1 and computer_choice == 0:
        print("you win")

    elif user_choice == 0 and computer_choice == 1:
        print("you lose")

    elif user_choice == computer_choice:
        print("draw")
