# Using *args for multiple arguments (Unlimited Positional Arguments)
# *args is a tuple
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Using **args for multiple keyword args
# **kwargs is a dict

def calculate(n, **kwargs):
    # print(kwargs)
    # Traditional way of looping thru a dict
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# print(calculate(2, add=3, multiply=5))
# print(calculate(3, add=10))


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        # Using [] would produce an error if keyword is not found
        # Instead, it's better to use get() func
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)

my_other_car = Car(make="Honda")
print(my_other_car.make)
print(my_other_car.model)
