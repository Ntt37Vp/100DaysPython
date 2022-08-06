# Day 4 Output - Rock Paper Scissors
import random
import sys
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
print("Welcome to Py Rock-Paper-Scissors Game.")
options = ["Rock", "Paper", "Scissors"]
player1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
player2 = random.choice(options)
if player1 == 0:
    print(f"You chose ROCK.\n{rock}")
    print(f"Computer chose {player2}")
    if player2 == "Rock":
        print(rock)
        print("It's a tie.")
    elif player2 == "Paper":
        print(paper)
        print("YOU LOOSE")
    elif player2 == "Scissors":
        print(scissors)
        print("YOU WON!")
elif player1 == 1:
    print(f"You chose PAPER.\n{paper}")
    print(f"Computer chose {player2}")
    if player2 == "Rock":
        print(rock)
        print("YOU WON!")
    elif player2 == "Paper":
        print(paper)
        print("It's a tie.")
    elif player2 == "Scissors":
        print(scissors)
        print("YOU LOOSE")
elif 2 == player1:
    print(f"You chose SCISSORS.\n{scissors}")
    print(f"Computer chose {player2}")
    if player2 == "Rock":
        print(rock)
        print("YOU LOOSE!")
    elif player2 == "Paper":
        print(paper)
        print("YOU WON")
    elif player2 == "Scissors":
        print(scissors)
        print("It's a tie.")
else:
    print("Not following instructions")
    sys.exit()