


# CHALLENGES
# Read the .csv file and store it in a Pandas DataFrame called df. Have a look at the read_csv() documentation and try to provide these column names: ['DATE', 'TAG', 'POSTS']
# Look at the first and last 5 rows of the DataFrame.
# How many rows and how many columns does it have?
# Count the number of entries in each column.

# Solutions
# import pandas as pd
# df = pd.read_csv("/content/QueryResults.csv")
# df.rename(
#           columns={"m": "DATE",
#                    "TagName": "TAG",
#                    'Unnamed: 2':"POSTS"})

# df.head()
# df.tail()
# To check the dimensions of the DataFrame, we use our old friend .shape. This tells us we have 1991 rows and 3 columns.
    # df.shape
# To count the number of entries in each column we can use .count(). Note that .count() will actually tell us the number of non-NaN values in each column.
    # df.count()
# In order to look at the number of entries and the number of posts by programming language, we need to make use of the .groupby() method. The key is combining .groupby() with the TAG column, which holds as our categories (the names of the programming languages).
    # df.groupby('TagName').sum()
# If we .count() the entries in each column, we can see how many months of entries exist per programming language.
    # df.groupby('TagName').count()

# Let's take a closer look at the 'DATE' column in our DataFrame. We can use the double square bracket notation to look at the second entry in the column:
    # df['DATE'][1]
# Alternatively, for column names no spaces, we can also use the dot-notation:
    # df.DATE[1]

# When we type check the contents of this cell, we see that we are not dealing with a date object, but rather with a string.
# type(df['m'][1])
# Let's use Pandas' to_datetime() to convert the entire df['DATE'] column.
    # df.m = pd.to_datetime(df.m)
    # df.head()

# The .pivot() method
# test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
#                         'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
#                         'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
# test_df
# pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# pivoted_df

# Mini-Challenge
# Can you pivot the df DataFrame so that each row is a date and each column is a programming language? Store the result under a variable called reshaped_df.

# Solution
    # reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
    # reshaped_df.shape
    # reshaped_df.columns
    # reshaped_df.head()
    # reshaped_df.count()

# Dealing with NaN Values
# In this case, we don't want to drop the rows that have a NaN value. Instead, we want to substitute the number 0 for each NaN value in the DataFrame. We can do this with the .fillna() method.

    # reshaped_df.fillna(0, inplace=True)
    # The inplace argument means that we are updating reshaped_df. Without this argument we would have to write something like this:
    # reshaped_df = reshaped_df.fillna(0)

# We can also check if there are any NaN values left in the entire DataFrame with this line:
    # reshaped_df.isna().values.any()

# Data Visualisation
    # reshaped_df = df_new.pivot(index='DATE', columns='TAG', values='POSTS')
    # plt.plot(reshaped_df.index, reshaped_df.java)
    # plt.show()