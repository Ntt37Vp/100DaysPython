# Day 5 - Exercise 4
# number is divisible by 3 it should print "Fizz", if number if divisible by 5 it should print "Buzz"
# if both print Fizz Buzz
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)