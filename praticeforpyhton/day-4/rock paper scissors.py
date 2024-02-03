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

game_images = [rock, paper, scissors]


user_choice = int(input(
    "what do you want? type 0 for 'rock' , type 1 for 'paper' and type 2 for 'scissors': "))

if user_choice > 2:
    print("invalid number")

else:

    print(game_images[user_choice])

    compurter_choice = random.randint(0, 2)
    print("computer choice is:-")
    print(game_images[compurter_choice])

    if user_choice == 0 and compurter_choice == 1:
        print("you lose")

    elif user_choice == 1 and compurter_choice == 0:
        print("you win")

    elif user_choice == 0 and compurter_choice == 2:
        print("you win")

    elif user_choice == 2 and compurter_choice == 1:
        print("you win")

    elif user_choice == 1 and compurter_choice == 2:
        print("you lose")

    elif user_choice == 2 and compurter_choice == 0:
        print("you loose")

    elif user_choice == 0 and compurter_choice == 0:
        print("draw")

    elif user_choice == 1 and compurter_choice == 1:
        print("draw")

    elif user_choice == 2 and compurter_choice == 2:
        print("draw")
