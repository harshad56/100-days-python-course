# who pay the bill?
import random
name_string = input("give me everbody's name,seprated by comma.")
name_seprater = name_string.split(",")
# get the totla number of items in list
num_items = len(name_seprater)

random_choice = random.randint(0, num_items-1)

person_who_willpay = name_seprater[random_choice]
print(person_who_willpay+" is going to buy the meal today.")
