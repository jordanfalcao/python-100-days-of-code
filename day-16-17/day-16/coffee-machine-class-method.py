from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee = CoffeeMaker()
my_money = MoneyMachine()
my_menu = Menu()


should_continue = True
while should_continue:
    choice = input(f"What would you like to? ({my_menu.get_items()}): ")
    if choice == "report":
        my_coffee.report()
        my_money.report()
    elif choice == "off":
        should_continue = False
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee.is_resource_sufficient(drink):
            if my_money.make_payment(drink.cost):
                my_coffee.make_coffee(drink)
