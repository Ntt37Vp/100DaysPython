# Day 8 - Exercise 1

# Write your code below this line
from math import ceil


def paint_calc(height, width, cover):
    print(f"You'll need {ceil((height * width) / cover)} of paint")


# Don't change the code below
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
