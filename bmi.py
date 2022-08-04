# Day 2 Exercise - BMI calculator.
print("Welcome to the BMI calculator.")
weight = float(input("Pls enter your weight (in KG):"))
height = float(input("Pls enter your height (in CM):"))
BMI = round(weight / (height / 100) ** 2)
if BMI > 30:
    print(f"Your BMI is {BMI}.\nYou are Obese.")
elif BMI > 25:
    print(f"Your BMI is {BMI}.\nYou are Overweight.")
elif BMI > 18.5:
    print(f"Your BMI is {BMI}.\nYou are Normal.")
else:
    print(f"Your BMI is {BMI}.\nYou are Underweight.")