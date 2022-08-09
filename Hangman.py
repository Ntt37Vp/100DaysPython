# Day 7 Output - Hangman
import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False

display = []
# print(f'Pssst, the solution is {chosen_word}.') # TEST CODE
print(f"Welcome to Py Hangman!!!\n{logo}")
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You already guessed that letter.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not on the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"YOU LOSE. The word we are looking for is {chosen_word.upper()}")

    print(stages[lives])
    print(display)

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!!! You guessed the right word!")
