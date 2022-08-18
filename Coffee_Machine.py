MENU = {
    "E": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "L": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "C": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Track variables
Machine_On = True
Coin_bank = 0


# TODO Ask user
def get_choice():
    """get user choice and return the cost"""
    choice = input("What would you like? 'E' for espresso, 'L' for latte or 'C' for cappuccino) ").upper()
    print(MENU[choice])


get_choice()

# TODO print report


# Turn off machine to exit
# if choice == "off":
#     Machine_On = False

# TODO check resources


# TODO process coin payment


# TODO check transaction


# TODO make coffee


# TODO deduct resources


