# program requirements
# 1.print report.
# 2. check resource sufficient?
# 3. process coins.
# 4. check transaction sucessful?
# 5.make coffee.
# -----------------------------------------------------------------------

from coffee_menu import MENU, resoureces
# -----------------------------------------------------------------------


def is_resoureces_sufficient(order_ingredients):
    """ Returns true when oredr can made ,False is ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resoureces[item]:
            print(f"sorry there is not enough{item}.")
            return False
    return True
# ---------------------------------------------------------------------------


def process_coins():
    """ returns  the total calculated from coins inserted"""
    
    
    print("please insdert coins")
    total = int(input("how many quarters?:"))*0.25
    total += int(input("how many dimes?:"))*0.1
    total += int(input("how many nickles?:"))*0.05
    total += int(input("how many pennis?:"))*0.01
    return total
# ------------------------------------------------------------------------------


def is_transaction_sucessful(money_received, cost_drink):
    """ Return true  when the payment is accepted,or false  if money is insuffient"""
    if money_received >= cost_drink:

        change = round(money_received-cost_drink, 2)
        print(f"here is {change} in change.")
        #-----------------------------------------#
        global profit
        profit += cost_drink
        return True

    else:
        print("soory! thats not enough money, money refunded")
        return False
# ------------------------------------------------------------------------------


def make_coffee(drink_name, order_ingredients):
    """ Deduct the Requires ingredients from the resources ."""
    for item in order_ingredients:
        resoureces[item] -= order_ingredients[item]
    print(f"here is your {drink_name}☕")


# ------------------------------------------------------------------------------
# taking a input from user what he want
profit = 0

is_on = True
while is_on:
    
    choice = input(
        "what would you like ?(espresso/iced coffee/caffe americano/chai tea latte/flat white/irish coffee):")
    
    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f" water:{resoureces['water']}ml")
        print(f"milk:{resoureces['milk']}ml")
        print(f"coffee:{resoureces['coffee']}g")
        print(f"money:${profit}")
    else:
        drink = MENU[choice]
        if is_resoureces_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    
