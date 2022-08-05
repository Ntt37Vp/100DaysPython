# Day 3 Exercise - Pizza Delivery
print("Welcome to Python Pizza Delivery!")
size = str(input("What size of pizza do you want? S, M, L "))
add_pepperoni = str(input("Do you want pepperoni? Y or N "))
add_cheese = str(input("Do you want to add cheese? Y or N "))

price = 0

if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price += 25

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if add_cheese == "Y":
    price += 1

print(f"Your final bill is ${price}")