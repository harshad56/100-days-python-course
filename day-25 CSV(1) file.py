with open('weather .csv')as f:
    data = f.readlines()
    print(data)
# --------------------------------------------------------------------------
import csv

with open('weather .csv')as f:
    data = csv.reader(f)
    teamperature = []
    for row in data:
        # print(row)
        # print(row[1])

        if row[1] != "temp":
            teamperature.append(row[1])
    print(teamperature)

# @---------------------------------------------------------------------------

import pandas

data = pandas.read_csv('weather .csv')
print(data)
print(data["temp"])
