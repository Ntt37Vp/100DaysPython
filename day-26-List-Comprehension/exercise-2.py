numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Instruction: create new list called result. It should contain ONLY THE EVEN NUMBERS.
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
