from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

isOn = True

while isOn:
    options = menu.get_items()
    choice = input(f"What do you want? ({options}) 'off', 'report': ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None and coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)