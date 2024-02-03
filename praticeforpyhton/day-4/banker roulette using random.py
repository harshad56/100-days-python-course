import random
names = input("give me everbody's name,seprated by comma.")

name_sperator = names.split(",")
name_items = len(name_sperator)

random_choice = random.randint(0, name_items)

person_who_paybill = name_sperator[random_choice]

print(f"{person_who_paybill} he  will pay the bill")
