
import pandas as pd

import matplotlib.pyplot as plt

# Replace the URL with the actual dataset URL

data_url = 'https://raw.githubusercontent.com/fatalencounters/API/master/us-states/2019-07-16%20DOJ%20Death%20in%20Custody%20Report%20Victim%20list.csv'

# Load the dataset

df = pd.read_csv(data_url)

# Display basic information about the dataset

print("Dataset Info:")

print(df.info())

# Display the first few rows of the dataset

print("\nFirst few rows of the dataset:")

print(df.head())

# Data cleaning and preprocessing (you may need to customize this based on your dataset)

# For example, converting date columns to datetime format df['Date of Injury Resulting in Death'] = pd.to_datetime(df['Date of Injury Resulting in Death'], errors='coerce')

# Analyze and visualize the data (you may need to customize this based on your analysis goals)

# For example, visualizing the number of deaths over time

deaths_by_year = df.groupby(df['Date of Injury Resulting in Death'].dt.year)[
    'Unique ID'].count()

plt.figure(figsize=(10, 6))

deaths_by_year.plot(kind='bar', color='salmon')

plt.title('Number of Police-Involved Deaths Over the Years')

plt.xlabel('Year')

plt.ylabel('Number of Deaths')

plt.show()
