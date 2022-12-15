# List Comprehension formula
# new_list = [new_item for item in list]
numbers = [1, 2, 3, 4, 5]
new_numbers = [(n * 2) for n in numbers]
print(new_numbers)

# Conditional List Comprehension
# new_list = [new_item for item in list if Test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Gab"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)
# upper_names = [name.upper() for name in names]
# print(upper_names)
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)
