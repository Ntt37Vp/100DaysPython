# Simple functions can have input/func/output:
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiple(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# Functions are first-class objects, meaning they can be passed around as objects like strings
def calculate(calc_func, n1, n2):
    return calc_func(n1, n2)

result = calculate(add, 2, 3)
print(result)


# Functions can be NESTED in other func
def outer_func():
    print("I'm outer")
    def inner_func():
        print("I'm inner")

    inner_func()
outer_func()


# Functions can be returned from other func
def outer_function():
    print("I'm outer")
    def nested_func():
        print("I'm nested")
    return nested_func

inner_function = outer_function()
inner_function


# Simple Python Decorator Functions
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
    return wrapper_function
@delay_decorator
def say_hello():
    print("Hello")

# With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

# Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()
