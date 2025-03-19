from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == 'off':
        print("Goodbye!")
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'latte' or choice == 'espresso' or choice == 'cappuccino':
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print(f"Please type one of the options provided. {menu.get_items()}")
