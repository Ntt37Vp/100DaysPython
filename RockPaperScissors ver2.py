# Day 4 Output - Rock Paper Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
options = ["Rock", "Paper", "Scissors"]

print("Welcome to Py Rock-Paper-Scissors Game.")
Games = int(input("How many games would you like to play? "))
player1_score = 0
player2_score = 0

while Games > 0:
    player2 = random.randint(0, 2)
    player1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    if player1 > 2:
        print("Invalid entry")
        break
    print(f"You chose {options[player1]}{game_images[player1]}")
    print(f"Computer chose {options[player2]}{game_images[player2]}")

    if player1 == player2:
        print("It's a tie.")
    elif player1 == 0 and player2 == 2:
        print("YOU WON.")
        player1_score += 1
    elif player1 == 0 and player2 == 1:
        print("YOU LOSE.")
        player2_score += 1
    elif player1 == 1 and player2 == 0:
        print("YOU WIN.")
        player1_score += 1
    elif player1 == 1 and player1 == 2:
        print("YOU LOSE.")
        player2_score += 1
    elif player1 == 2 and player2 == 1:
        print("YOU WIN.")
        player1_score += 1
    elif player1 == 2 and player2 == 0:
        print("YOU LOSE.")
        player2_score += 1
    # else:
    #     print("Invalid entry. YOU LOSE.")
    #     sys.exit()
    print(f"You score: {player1_score}\nComputer score:{player2_score}")
    Games -= 1
print(f"HERE IS THE FINAL SCORE:\nYour score:{player1_score}\nComputer score:{player2_score}")
if player1_score > player2_score:
    print("You are the NEW ROCK-PAPER-SCISSORS CHAMPION of the WORLD!")
    print('''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
    ''')
else:
    print("Computer is STILL the Defending ROCK-PAPER-SCISSORS CHAMPION of the WORLD!!")
