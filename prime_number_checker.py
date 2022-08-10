# Day 8 - Exercise 2 (Prime Number Checker)
# Write your code below this line
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's NOT a prime number.")

# Write your code above this line (My initial code below is wrong. ex: 45 is NOT a prime number)
#     if number == 1:
#         print("The number one is neither a prime nor a composite.")
#     elif number % 2 == 1 or number == 2:
#         print(f"{number} is a prime number")
#     else:
#         print("It is NOT a prime number.")
# Do NOT change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n)
