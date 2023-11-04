import pandas as pd
df=pd.read_csv('salaries_by_college_major.csv')
#Now take a look at the Pandas dataframe we've just created with head(). 
#This will show us the first 5 rows of our dataframe.
df.head()

#We've already used the .head() method to peek at the top 5 rows of our dataframe. To see the number of rows and columns we can use the shape attribute:
df.shape
df.columns

#Missing Values and Junk Data
# Before we can proceed with our analysis we should try and figure out if there are any missing or junk data in our dataframe.
# That way we can avoid problems later on. In this case,
# we're going to look for NaN (Not A Number) values in our dataframe.
#  NAN values are blank cells or cells that contain strings instead of numbers.
#   Use the .isna() method and see if you can spot if there's a problem somewhere.
df.isna

#Did you find anything? Check the last couple of rows in the dataframe:
df.tail

#Delete the Last Row
# We don't want this row in our dataframe.
# There's two ways you can go about removing this row.
# the first way is to manually remove the row at index 50. The second way is to simply use the .dropna() method from pandas.
# Let's create a new dataframe without the last row and examine the last 5 rows to make sure we removed the last row:

clean_df=df.dropna()
clean_df.tail

#Accessing Columns and Individual Cells in a Dataframe
#Find College Major with Highest Starting Salaries
#To access a particular column from a data frame we can use the square bracket notation, like so:
clean_df['Starting Median Salary']

#To find the highest starting salary we can simply chain the .max() method.
clean_df['Starting Median Salary'].max()

#The highest starting salary is $74,300. But which college major earns this much on average?
# For this, we need to know the row number or index so that we can look up the name of the major.
#Lucky for us, the .idxmax() method will give us index for the row with the largest value.
clean_df['Starting Median Salary'].idxmax()

#which is 43. To see the name of the major that corresponds to that particular row, we can use the .loc (location) property.
clean_df['Undergraduate Major'].loc[43]

#Here we are selecting both a column ('Undergraduate Major') and a row at index 43, so we are retrieving the value of a particular cell.
#You might see people using the double square brackets notation to achieve exactly the same thing: 
clean_df['Undergraduate Major'][43]
clean_df.loc[43]

#Solution: Highest and Lowest Earning Degrees
# I hope you gave the last challenge a good go before checking the solution below.
# The Highest Mid-Career Salary
print(clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
clean_df['Undergraduate Major'][8]

#The Lowest Starting and Mid-Career Salary
print(clean_df['Starting Median Salary'].min())
clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]

#Here I've nested the code that we've seen in the previous lesson in the same line.
# We can also use the .loc property to access an entire row.
# Below I've accessed the row at the index of the smallest mid-career salary:
clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

# Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk
# Lowest Risk Majors

# A low-risk major is a degree where there is a small difference between the lowest and highest salaries.
# In other words, if the difference between the 10th percentile and the 90th percentile earnings of your major is small,
#  then you can be more certain about your salary after you graduate.
# How would we calculate the difference between the earnings of the 10th and 90th percentile? Well,
#  Pandas allows us to do simple arithmetic with entire columns, so all we need to do is take the difference between the two columns:
clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

#Alternatively, you can also use the .subtract() method.
clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

#The output of this computation will be another Pandas dataframe column. 
#We can add this to our existing dataframe with the .insert() method:
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

#Sorting by the Lowest Spread

# To see which degrees have the smallest spread, we can use the .sort_values() method.
#  And since we are interested in only seeing the name of the degree and the major,
#   we can pass a list of these two column names to look at the .head() of these two columns exclusively.

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()
#Does .sort_values() sort in ascending or descending order? To find out, check out the Pandas

#Solution: Degrees with the Highest Potential
# Here's the solution to the challenge from the previous lesson:

# Majors with the Highest Potential

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

#Majors with the Greatest Spread in Salaries

highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

#Notice how 3 of the top 5 are present in both.
# This means that there are some very high earning Economics degree holders out there, but also some who are not earning as much.
#It's actually quite interesting to compare these two rankings versus the degrees where the median salary is very high.

# Grouping and Pivoting Data with Pandas
# Often times you will want to sum rows that belong to a particular category. For example, which category of degrees has the highest average salary? Is it STEM, Business or HASS (Humanities, Arts, and Social Science)? 

# To answer this question we need to learn to use the .groupby() method. This allows us to manipulate data similar to a Microsoft Excel Pivot Table.

# We have three categories in the 'Group' column: STEM, HASS and Business. Let's count how many majors we have in each category:

clean_df.groupby('Group').count()

#Number formats in the Output

#The above is a little hard to read, isn't it? We can tell Pandas to print the numbers in our notebook to look like 1,012.45 with the following line:

pd.options.display.float_format = '{:,.2f}'.format 


# rather than doing print we use google colabartor for pandas expolration in google drive
