import pandas as pd

import matplotlib.pyplot as plt


# Sample data (replace with your actual dataset)

data = {

    'Year': [1957, 1961, 1969, 1981, 2001, 2011, 2021],

    'Country': ['Soviet Union', 'USA', 'USA', 'USA', 'China', 'USA', 'SpaceX'],

    'Mission_Type': ['Satellite Launch', 'Human Spaceflight', 'Moon Landing', 'Space Shuttle', 'Satellite Launch', 'Space Shuttle', 'Satellite Launch'],

    'Success': [True, True, True, True, True, True, True],

}


# Create a DataFrame

df = pd.DataFrame(data)


# Data Cleaning and Processing (if needed)

# Example: Convert 'Year' to datetime, set it as the index

df['Year'] = pd.to_datetime(df['Year'], format='%Y')

df.set_index('Year', inplace=True)


# Exploratory Data Analysis (EDA)

print("Summary Statistics:")

print(df.describe())


# Data Visualization

plt.figure(figsize=(10, 6))


# Plot the number of missions each year

plt.subplot(2, 1, 1)

df.resample('Y').size().plot(kind='bar', color='skyblue')

plt.title('Number of Space Missions Each Year')

plt.xlabel('Year')

plt.ylabel('Number of Missions')


# Plot the success rate each year

plt.subplot(2, 1, 2)

df.groupby(df.index.year)['Success'].mean().plot(
    kind='bar', color='lightgreen')

plt.title('Success Rate of Space Missions Each Year')

plt.xlabel('Year')

plt.ylabel('Success Rate')


plt.tight_layout()

plt.show()
