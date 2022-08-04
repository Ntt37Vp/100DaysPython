# Day 2 Output - Tip Calculator
print("Welcome to the tip calculator!")
Bill = int(input("What was the total bill? "))
People = int(input("How many people to split the bill? "))
Tip = int(input("How much tip would you give? "))
Share = round((Bill + Tip) / People, 2)
print(f"Each person should pay: {Share}")