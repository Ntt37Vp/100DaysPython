# Day 5 - Exercise 3
# Program that calculates the sum of all the even numbers from 1 to 100
total = 0
for x in range(2, 101, 2):
    total += x
print(total)
# Alternate solution
# sum = 0
# for x in range(0, 101):
#     if x % 2 == 0:
#         total += x
# print(sum)
