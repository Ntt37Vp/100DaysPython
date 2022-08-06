# Day 5 - Exercise 1
student_heights = input("Input the list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
for height in student_heights:
    total += height
# print(f"Sum of heights is {total}")

count = 0
for student in student_heights:
    count += 1
# print(f"Count of students is {count}")
average = round(total / count)
print(f"Average height is {average}")