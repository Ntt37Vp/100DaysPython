# Day 5 - Password Gen ver 2
import random

print("Welcome to Py Password Generator ver 2")
char = int(input("How many characters do you want in your password? "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
mixed = letters + numbers + symbols

while True:
    password = []
    for ch in range(1, char + 1):
        password += random.choice(mixed)

    random.shuffle(password)

    hard_password = ""
    for ch in password:
        hard_password += ch

    print(hard_password)

    option = input("Do you want another password? Y or N ")


