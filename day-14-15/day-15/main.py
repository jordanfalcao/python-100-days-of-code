MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
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

profit = 0


def print_resources():
    """Print the remaining amount of resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_ingredients(ingredients):
    """Check the ingredients quantity and return True if they are or False if
    they are not"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coin(price):
    """When order can be made, calculates total amount paid, print the change
     and returns True. If money is insufficient, returns False."""
    change = 0
    global profit
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

    if total >= price:
        profit += price
        change = round(total - price, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


should_continue = True
while should_continue:
    user_input = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        should_continue = False
    elif user_input == "report":
        print_resources()
    else:
        choice = MENU[user_input]
        if check_ingredients(choice["ingredients"]):
            if process_coin(choice["cost"]):
                for item in choice["ingredients"]:
                    resources[item] -= choice["ingredients"][item]
                print(f"Here is your {user_input} ☕️. Enjoy!")
