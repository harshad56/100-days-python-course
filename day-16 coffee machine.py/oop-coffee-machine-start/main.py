from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
Coffee_Maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f" what would you like?({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        Coffee_Maker.report()

    else:
        drink = menu.find_drink(choice)
        if Coffee_Maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            Coffee_Maker.make_coffee(drink)
