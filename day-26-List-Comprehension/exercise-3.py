# My solution:
file1 = open("file1.txt")
file2 = open("file2.txt")

file1_data = file1.readlines()
file2_data = file2.readlines()
result = [int(num) for num in file1_data if num in file2_data]

# Write your code above 👆
# INSTRUCTION: Take a look inside file1.txt and file2.txt.
# They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# IMPORTANT: The result should be a list that contains Integers, not Strings.
# Try to use List Comprehension instead of a Loop.
# Sample output: [3, 6, 5, 33, 12, 7, 42, 13]

# Angela's solution
# with open("file1.txt") as file1:
#     file1_data = file1.readlines()
# with open("file2.txt") as file2:
#     file2_data = file2.readlines()
# result = [int(num) for num in file1_data if num in file2_data]

print(result)
