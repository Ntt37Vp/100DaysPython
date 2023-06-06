# Day 73 Goals: what you will make by the end of the day

# Import
    # import pandas as pd

# Data Exploration
    # df = pd.read_csv("data/colors.csv")
    # colors_df.head()
    # colors_df['name'].nunique()
    # colors_df.groupby('is_trans').count()
    # colors_df.is_trans.value_counts()

    # Challenge: Read the sets.csv data and take a look at the first and last couple of rows.
        # sets = pd.read_csv('data/sets.csv')
        # sets.head()
        # sets.tail()

    # Challenge: In which year were the first LEGO sets released and what were these sets called?
        # sets.sort_values('year').head()

    # Challenge: How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the year the company started?
        # sets[sets['year'] == 1949]
    # Challenge: Find the top 5 LEGO sets with the most number of parts
        # sets.sort_values('num_parts', ascending=False).head()
    # Challenge: Use .groupby() and .count() to show the number of LEGO sets released year-on-year. How do the number of sets released in 1955 compare to the number of sets released in 2019?
        # sets_by_year = sets.groupby('year').count()
        # sets_by_year['set_num'].head()
        # sets_by_year['set_num'].tail()

    # Challenge: Show the number of LEGO releases on a line chart using Matplotlib.

# The Pandas .agg() function
    # Format: DataFrame.agg(func=None, axis=0, *args, **kwargs)
    # themes_per_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})