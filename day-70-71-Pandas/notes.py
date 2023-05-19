# Use Google Collabotary
# https://colab.research.google.com/
# https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

# import pandas as pd
# df = pd.read_csv('path of salaries_by_college_major.csv')

# df.head()
# df.tail()
# df.shape
# df.columns
# Index(['Undergraduate Major', 'Starting Median Salary',
#        'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary',
#        'Mid-Career 90th Percentile Salary', 'Group'],
#       dtype='object')

# df.isna()
# clean_df = df.dropna()
# clean_df.tail()


# clean_df['Starting Median Salary']
# clean_df['Starting Median Salary'].max()
# clean_df['Starting Median Salary'].idxmax()
# clean_df['Undergraduate Major'].loc[43]
# clean_df['Undergraduate Major'][43]
#  clean_df.loc[43]

# CODE CHALLENGE
# What college major has the highest mid-career salary? How much do graduates with this major earn?
# Which college major has the lowest starting salary and how much do graduates earn after university?
# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?

# SOLUTION
# print(clean_df['Mid-Career Median Salary'].max())
# print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
# clean_df['Undergraduate Major'][8]

# print(clean_df['Starting Median Salary'].min())
# clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]
# clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

# Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk
# clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# OR USE subtract()
# clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

# spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# clean_df.insert(1, 'Spread', spread_col)
# clean_df.head()

# Sorting by the Lowest Spread
# low_risk = clean_df.sort_values('Spread')
# low_risk[['Undergraduate Major', 'Spread']].head()


# CODING CHALLENGE
# Using the .sort_values() method, can you find the degrees with the highest potential? Find the top 5 degrees with the highest values in the 90th percentile.
# Also, find the degrees with the greatest spread in salaries. Which majors have the largest difference between high and low earners after graduation.

# SOLUTION
# Majors with the Highest Potential
# highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
# highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()
# Majors with the Greatest Spread in Salaries
# highest_spread = clean_df.sort_values('Spread', ascending=False)
# highest_spread[['Undergraduate Major', 'Spread']].head()


# Grouping and Pivoting Data with Pandas (like MS Excel PIVOT!)
# Use the .groupby() method

# Learning Points & Summary
# Use .head(), .tail(), .shape and .columns to explore your DataFrame
# Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.
# You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]
# You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]
# The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()
# You can sort the DataFrame with .sort_values() and add new columns with .insert()
# To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method
