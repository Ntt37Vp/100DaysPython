# Day 5 - Exercise 2
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# print(student_scores)
# type(student_scores)
highest = 0
for score in student_scores:
    if score > highest:
        highest = score
print(f"The highest score is {highest}")