# DICTIONARY COMPREHENSION
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# student_scores = {
#     "alex": 70,
#     "beth": 80,
#     "caroline": 75,
#     "dave": 85,
#     "eleanor": 90,
#     "freddie": 74
# }
# passed_students = {student:score for (student, score) in student_scores.items() if score > 75}
# print(passed_students)

# Reminder on FOR loops in dictionary
# for (key, value) in dict.item()
#   print(value)

# Sample dict
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a Data Frame
for (key, value) in student_data_frame.items():
    print(value)

# Using pandas ITERROWS()
for (index, row) in student_data_frame.iterrows():
    # print(row)
    print(row.student)
    print(row.score)

