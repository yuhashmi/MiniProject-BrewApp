import os 
import sys
import csv
from table import print_table 

# Define data
# Expected commands

GET_PEOPLE = 1
GET_DRINKS = 2
select_id = 3
Set_fav = 4
View_fav = 5
order_drinks = 6
exit_menu = 7

people = []
drinks = []
fav_drinks = []

APP_NAME = "BrIW"

MENU = f'''
Welcome to {APP_NAME} v0.1!
Please, select an option by entering a number:
    [1] Get all people
    [2] Get all drinks
    [3] Add People and Drinks 
    [4] Set a favourite drink
    [5] View favourites
    [6] Order drink(s)
    [7] Exit
'''
# Data sources

PEOPLE_FILE_PATH = './data/people.csv'
DRINKS_FILE_PATH = './data/drinks.csv'

# Functions

def people_list():
    with open(PEOPLE_FILE_PATH, 'r') as people_files:
        people_reader = csv.reader(people_files)
        for line in people_reader:
            people.append(str(line))

def drink_list():
    with open(DRINKS_FILE_PATH, 'r') as drinks_files:
        drink_reader = csv.reader(drinks_files)
        for line in drink_reader:
            drinks.append(str(line))

def print_favourites(data):
    items = []
    for name, drink in data.items():
        items.append(f'{name}: {drink}')
    print_table('Favourites', items)

def get_menu_input(message):
    try:
        return int(input(f'{message} '))
    except ValueError:
        output("Menu items - numbers are the only input I understand")
        wait()
        return False

# Round class for ordering drinks

class Drinks:
    def __init__(self):
        self.menu_items = ['coke', 'coffee', 'tea', 'fanta', 'lemonade', 'pepsi', \
        'tango', 'ice tea', 'green tea', 'strawberry milkshake']
 
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
 
drink = Drinks()

# Functions for user input
       
def id_selection():
    with open(PEOPLE_FILE_PATH, 'w', newline = "") as people_files, open(DRINKS_FILE_PATH, 'w', newline = "") as drink_files:
        people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
        drink_writer = csv.writer(drink_files, quoting=csv.QUOTE_ALL)
        b = int(input("Number of people: "))
        for i in range(b):
            name = input("Please enter the name of the person: ")
            people_writer.writerow([name])
            drink = input("Please enter drink name: ")
            drink_writer.writerow([drink])
            print("Name and drink has been added.")

def clear_screen():
    os.system('cls')

def print_main_menu():
    clear_screen()
    print(MENU)

def print_menu(title, data):
    items = []
    for i, item in enumerate(data, start=1):
        items.append(f'[{i}] {item}')
    clear_screen()
    print(f'{title}\n')
    print('\n'.join(items), '\n')

def get_selection(message):
    try:
        return int(input(f'{message} \n'))
    except ValueError:
        print("Please enter a valid command ranging from 1 to 6")
    
def wait():
    input('Press ENTER to return to the menu') 

def validate_menu_input(index, data):
    if index < 0 or index >= len(data):
        print(f'"{index}" is not a valid option from that menu\n')
        wait()
        return False
    return True

def select_from_menu(message, data):
    print_menu(message, data)
    index = get_menu_input('Enter your selection:')
    if not validate_menu_input(index, data):
        return False
    return data[index]

def output(text):
    print(f'\n{text}')

# While loop that prints menu and repeats till there is a correct selection

while True:
    print_main_menu()
    command = get_menu_input('Enter your selection:')

# if conditions instructing the menu

    if command == GET_PEOPLE:
        people_list()
        print_table("People", people)
        wait()
    elif command == GET_DRINKS:
        drink_list()
        print_table("Drinks", drinks)
        wait()
    elif command == select_id:
        id_selection()
        wait()
    elif command == Set_fav:
        person = select_from_menu('Choose a person', people)
        if not person:
            output(f'{person} is mo')
            wait()
            drink = select_from_menu(f'Choose a drink for {person}', drinks)
        if not drink:
            wait()
            fav_drinks[person] = drink
    elif command == View_fav:
        print_favourites(fav_drinks)
        wait()
    elif command == order_drinks:
        drink.order()
        wait()
    elif command == exit_menu:
        print(f'Thank you for using {APP_NAME}')
        exit()
    else:
        print(f'"{command}" is not a command that I recognise.')
        wait()

    
