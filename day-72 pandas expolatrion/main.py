import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
print(df.head())
print(df.shape)
print(df.columns)
print(df.isna)
print(df.tail)
