# Round class for ordering drinks
import sys
from src.persistence.people_drinks import load_drinks, load_people

class Drinks:
    def __init__(self):
        self.menu_items = menu_items
        # ['coke', 'coffee', 'tea', 'fanta', 'lemonade', 'pepsi', \
        # 'tango', 'ice tea', 'green tea', 'strawberry milkshake']
 
    

    def menu(self):
        return f'Menu: {", ".join(self.menu_items).title()}'
 
    def order(self):
        on_menu = []
        not_on_menu = []
        return_values = []
 
        string = (f'\n Our Menu: {", ".join(self.menu_items)}')
        print(f'{string}\n')
        self.order_items = \
        input('Can I take your order?\nSeperate multiple items with a comma.\n: ').split(',')
 
        for item in self.order_items:
            if not item.strip():
                print(f'\n You did not order anything.')
                sys.exit()
            if item.strip() in '\n'.join(self.menu_items):
                on_menu.append(item.strip())
 
            else:
                not_on_menu.append(item.strip())
 
        if on_menu:
            string = (f'\n Your Order: {", ".join(on_menu).title()}')
            print(f'{string}')
 
        if not_on_menu:
            string = \
            (f'\n Sorry, {", ".join(not_on_menu).title()} is not on the menu.')
            print(f'{string}\n')
 
        print()
 

