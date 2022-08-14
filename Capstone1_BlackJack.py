# Capstone Project 1 - Black Jack Game
from art_works import blackjack
import random
import extra_functions


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over 21. You lose."

    if user_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "You lose. Computer has BlackJack!"
    elif user_score == 0:
        return "You WIN! BLACKJACK!"
    elif user_score > 21:
        return "You lose. Over 21."
    elif computer_score > 21:
        return "You WIN! Computer went over 21."
    elif user_score > computer_score:
        return f"YOU WIN!. Your score:{user_score} Computer score:{computer_score}"
    else:
        return f"YOU LOSE. Computer score:{computer_score} Your score:{user_score}"


def play_game():
    print(blackjack)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" Your cards: {user_cards} current score: {user_score} ")
        print(f" Computer 1st card: {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score > 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n'. ") == 'y':
    extra_functions.clearscreen()
    play_game()
