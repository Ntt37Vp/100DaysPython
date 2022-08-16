# Day 14 Exercise 1
from art_works import higher_lower, vs
from higher_or_lower_data import data
from random import randint

print(higher_lower)


def Item_A():
    """Gets a random item from data dictionary"""
    value1 = data[randint(0, 49)]
    name1 = value1["name"]
    description1 = value1["description"]
    country1 = value1["country"]
    follower1 = value1["follower_count"]
    print(f"Compare A: {name1}, a {description1}, from {country1} ")


def Item_B():
    """Gets another item from data dictionary"""
    value2 = data[randint(0, 49)]
    name2 = value2["name"]
    description2 = value2["description"]
    country2 = value2["country"]
    follower2 = value2["follower_count"]
    print(f"Compare B: {name2}, a {description2}, from {country2} ")


Item_A()
print(vs)
Item_B()


# Ask for a user guess
# guess = input("Who has more followers? Type 'A' or 'B' : ").upper()

# def comparison of Compare A & B
def compare(A, B):
    winner = 0
    if A > B:
        winner = A
    elif A < B:
        winner = B
    print(winner)


compare(Item_A(), Item_B())


# Track user score

# Loop
