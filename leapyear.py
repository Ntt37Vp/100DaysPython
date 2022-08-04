# Day 3 Exercise - Leap year checker
# The year is a multiple of 400.
# The year is a multiple of 4 but not 100.
Year = int(input("Enter the year: "))
if Year % 400 == 0 or Year % 4 == 0 and Year % 100 != 0:
    print("Leap Year!")
else:
    print("Not a leap year.")