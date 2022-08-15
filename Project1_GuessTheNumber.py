# Project 1 - Py Guess the Number
from art_works import num_guess, trophy
import random

print(num_guess)
print("Welcome to Py Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")


def Play_Game():
    secret = random.randint(1, 100)
    is_game_over = False
    LIFE = 0
    level = input("Choose a difficulty. Type 'e' for Easy mode or 'h' for Hard mode: ").lower()

    if level == 'e':
        LIFE = 10
        print(f"You have {LIFE} attempts remaining to guess the number.")
    elif level == "h":
        LIFE = 5
        print(f"You have {LIFE} attempts remaining to guess the number.")
    else:
        LIFE = 3
        print(f"Okay, so you want Extra Hard Mode. Life is set to {LIFE}.")

    while LIFE > 0 and is_game_over == False:
        Guess = int(input("Make a guess: "))

        if Guess == secret:
            print("WOW! YOU GOT THE SECRET NUMBER!")
            print(trophy)
            is_game_over = True

        elif Guess > secret:
            print("You Guess is more than the Secret Number.")
            LIFE -= 1
            print(f"You have {LIFE} attempts left.")
        elif Guess < secret:
            print("Your Guess is less than the Secret Number.")
            LIFE -= 1
            print(f"You have {LIFE} attempts left.")
        else:
            print("Invalid entry. Minus 1 life.")
            LIFE -= 1


if input("Do you want to play? Type 'y' for yes or 'n' for no: ") == "y":
    Play_Game()
