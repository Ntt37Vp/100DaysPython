# Day 10 Output
from art_works import calculator

print(calculator)
print("Welcome to Py Calculator!")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation to do: ")
num2 = int(input("What's the second number: "))
function = operations[operation_symbol]
answer = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
