import random
print('''
   _______
  /\ o o o\
 /o \ o o o\_______
<    >------>   o /|
 \ o/  o   /_____/o|
  \/______/     |oo|
        |   o   |o/
        |_______|/
''')
print("Welcome to Py Dice.")
roll = int(input("Which dice would you like to roll? Type '1' for D6, or '2' for D20 or '3' for both. " ))
D6 = random.randint(1, 6)
D20 = random.randint(1, 20)
if roll == 1:
    print(f"D6 dice rolled a {D6}")
elif roll == 2:
    print(f"D20 dice rolled a {D20}")
elif roll == 3:
    print(f"D6 dice rolled a {D6}")
    print(f"D20 dice rolled a {D20}")
else:
    print("Invalid input.")