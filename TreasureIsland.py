# Day 3 Output - Treasure Island Choose Your Own Adventure
import sys
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')
print("Welcome to Treasure Island. Your mission is to find the treasure.")
crossroad = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' \n").lower()

if crossroad == "left":
    print("You've come to a lake. There is an island in the middle of the lake. ")
    lake = input("Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    if lake == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. ")
        doors = input("red, yellow and blue. Which color do you choose? \n").lower()
        if doors == "yellow":
            print("YOU WON! Treasure found.")
        elif doors == "red":
            print("Red means blood. You were eaten by a beast.")
            sys.exit()
        elif doors == "blue":
            print("Vampire bit you. Game over!")
            sys.exit()
        else:
            print("Door trap. Game over")
            sys.exit()
    elif lake == "swim":
        print("You were eaten by piranhas.")
        sys.exit()
    else:
        print("Not following instructions. You were abducted by aliens.")
        sys.exit()
elif crossroad == "right":
    print("You fell into a hole. Game over.")
    sys.exit()
else:
    print("Not following instructions. You were abducted by aliens.")
    sys.exit()