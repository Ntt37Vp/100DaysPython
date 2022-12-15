# DICTIONARY COMPREHENSION
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

student_scores = {
    "alex": 70,
    "beth": 80,
    "caroline": 75,
    "dave": 85,
    "eleanor": 90,
    "freddie": 74
}
passed_students = {student:score for (student, score) in student_scores.items() if score > 75}
print(passed_students)
