# Day 7 - Exercise 1
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []

for _ in range(word_length):
    display += "_"

lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if letter != guess:
        lives -= 1
        print(f"You have {lives} lives left.")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("YOU WIN")
    if lives == 0:
        end_of_game = True
        print("YOU LOSE.")