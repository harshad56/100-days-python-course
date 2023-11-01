import pandas

data = pandas.read_csv('weather .csv')
# print(type(data))
# print(data)
# ---------------------------------------------------------------------------

# here we see pandas different functions
# like to_dict and to_list

# # convert data into dict by using pandas

# data_dict = data.to_dict()
# print(data_dict)

# print("----------------------------------------------------------------------------")

# # convert data into list by using pandas

# temp_list = data["temp"].to_list()
# # print(temp_list)
# print(len(temp_list))

# print("----------------------------------------------------------------------------")

# average = sum(temp_list)/len(temp_list)
# print(average)
# # either we use pandas func

# # doing addiation respective  by using pandas
# print(data['temp'].mean())

# print("----------------------------------------------------------------------------")

# # finding maximum number by using pandas in the list

# print(data["temp"].max())

# print("----------------------------------------------------------------------------")

# # Get data in columns
# print(data.condition)

# print("----------------------------------------------------------------------------")

# # get data in rows

# print(data[data.day == "monday"])
# print(data[data.temp == data.temp.max()])

# print("----------------------------------------------------------------------------")

# monday = data[data.day == "monday"]
# print(monday.condition)

# print("----------------------------------------------------------------------------")

# # convert the degree into ferniate

# monday = data[data.day == "monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5+32
# print(monday_temp_F)

# create a database from scratch
data_dict = {
    "students": ["amy", "james", "Harshad"],
    "marks": [34, 56, 87]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
