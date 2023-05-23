


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