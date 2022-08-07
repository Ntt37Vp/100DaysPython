# Day 5 Output - Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
mixed = [letters, symbols, numbers]
print("Welcome to Py Password Generator")
nr_letters = int(input("How many letters? "))
nr_numbers = int(input("How many numbers? "))
nr_symbols = int(input("How many symbols? "))

# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# for char in range(1, nr_symbols):
#     password += random.choice(symbols)
# print(password)

# Hard Level

password_list = [] # Bracket to indicate you wanted a list
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
for char in range(1, nr_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)

hard_password = ""
for char in password_list:
    hard_password += char
print(hard_password)
