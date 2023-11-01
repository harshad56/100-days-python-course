enemies = 1  # global varible


def increase_enemies():
    print(f" enemies inside function:{enemies}")  # use global varible
    return enemies+1


enemies = increase_enemies()

print(f" enemies ontside function:{enemies}")
