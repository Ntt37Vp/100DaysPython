# Day 4 Exercise - Who's Paying the Dinner Roulette
import random
# Split string method
names_string = input("Give me the participant names separated by comma: ")
names = names_string.split(", ") # Comma then Space
rand = random.randint(0, len(names)-1) # The minus 1 is important since we count starting 0
dinner = names[rand]
washer = random.choice(names) # The choice function against the random module automatically picks a list item
print(f"{dinner} is buying dinner.")
print(f"{washer} is washing the dishes.")