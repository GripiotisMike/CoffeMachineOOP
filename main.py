from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_make = CoffeeMaker()
money = MoneyMachine()
a = True
while a:
    request = input(f"What would you like? {coffee_menu.get_items()}:")
    if request == "off":
        a = False
    elif request == "report":
        coffee_make.report()
        money.report()
    else:
        item = coffee_menu.find_drink(request)
        if item:
            item_cost = item.cost
            if coffee_make.is_resource_sufficient(item):
                if money.make_payment(item_cost):
                    coffee_make.make_coffee(item)
        else:
            print("Wrong input, please check for spelling mistakes!")

