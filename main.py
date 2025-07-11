from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker

from money_machine import MoneyMachine



money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
menuItem = MenuItem( 'cost','water', 'milk', 'coffee', 'cost')


def successful_order(drink):
    if coffee_maker.is_resource_sufficient(drink):
        print(f"That will be ${drink.cost}")
        money_machine.make_payment(drink.cost)
        coffee_maker.make_coffee(drink)



is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")


    if choice == "off":
        is_on = False
    elif choice in options:
        drink = menu.find_drink(choice)
        successful_order(drink)
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    
    else:
        print(f"Your Choice of {choice} is not one of the Items avalible please try again")
        is_on = False

    
    
        

     
    
  
        
        

    
        





