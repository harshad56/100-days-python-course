#####---scope---#####
enemies = 1  # outside function


def increase_enemies():
    enemies = 2  # inside function
    print(f" enemies inside function:{enemies}")  # inside function


increase_enemies()

print(f" enemies outside function:{enemies}")  # outside function

#---------------------------------------------------------------------------#

# local scope


def drink_portion():
    portion_string = 2  # variable declared in inside function

    # it run because the varaible is already decalred inside function
    print(portion_string)


drink_portion()

# when you try print variable it gets error because it not decarle outside the function

# print(portion_string)

#---------------------------------------------------------------------------#

#global scope
player_health = 10  # global varible


def drink_juice():
    portion_strenght = 3
    # global varible you can used inside the function also,outside the function also
    print(player_health)


drink_juice()
