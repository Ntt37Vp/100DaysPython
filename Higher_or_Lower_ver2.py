# Day 14 Exercise 1 ver 1
from art_works import higher_lower, vs
from higher_or_lower_data import data
import random
import extra_functions


def format_data(account):
    """Format the account data into a printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the guess and follower counts and returns if correct"""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"


print(higher_lower)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Loop the game so long as guess is correct
while game_should_continue:

    # Get a random account from data source
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask for a guess from the user
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Check if the guess is right
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear space
    extra_functions.clearscreen()
    print(higher_lower)

    # Give feedback to the user
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")

