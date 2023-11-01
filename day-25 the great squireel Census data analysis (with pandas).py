import pandas

data = pandas.read_csv("squireel central park usa.csv")

grey_squireel_count = len(data[data["Primary Fur Color"] == "Grey"])

red_squireel = data[data["Primary Fur Color"] == "Cinnamon"]
red_squireel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squireel = data[data["Primary Fur Color"] == "Black"]
black_squireel_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squireel_count)

print("-----------------------------------------------------------------")

print(red_squireel)

print("------------------------------------------------------------")

print(red_squireel_count)

print("-----------------------------------------------------------------")

print(black_squireel)

print("-----------------------------------------------------------------")

print(black_squireel_count)

# create a dataframe

data_dict = {
    "fun color": ["Grey", "Cinnamon", "Black"],
    "squireel_count": [grey_squireel_count, red_squireel_count, black_squireel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squireel_count.csv")
