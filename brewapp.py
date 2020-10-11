import os 
import sys
import csv
from src.menu.commands import GET_PEOPLE, GET_DRINKS, add_people, add_drinks, Set_fav, View_fav, order_drinks, exit_menu
from src.core.rounds import Drinks
from src.persistence.people_drinks import people, drinks, favourites, load_people, insert_people_db, drinks, insert_to_people_table, load_drinks, print_db_data, insert_to_drink_table, load_favs_from_db, print_db_favs
from src.persistence.favourites import set_drink_favs
from src.menu.table import print_table 
from src.menu.index_menu import MENU, APP_NAME, get_menu_input, get_selection, print_main_menu, clear_screen, select_from_menu, wait

# Define data
# Expected commands

# GET_PEOPLE = 1
# GET_DRINKS = 2
# people_drinks = 3
# Set_fav = 4
# View_fav = 5
# order_drinks = 6
# exit_menu = 7

# APP_NAME = "BrIW"

# MENU = f'''
# Welcome to {APP_NAME} v0.1!
# Please, select an option by entering a number:
#     [1] Get all people
#     [2] Get all drinks
#     [3] Add People and Drinks 
#     [4] Set a favourite drink
#     [5] View favourites
#     [6] Order drink(s)
#     [7] Exit
# '''
# Data sources

# PEOPLE_FILE_PATH = './data/people.csv'
# DRINKS_FILE_PATH = './data/drinks.csv'
# FAVOURITES_FILE_PATH = './data/favourites.csv'

# Functions

# def people_list():
#     with open(PEOPLE_FILE_PATH, 'r') as people_files:
#         people_reader = csv.reader(people_files)
#         for line in people_reader:
#             people.append(str(line))

# def drink_list():
#     with open(DRINKS_FILE_PATH, 'r') as drinks_files:
#         drink_reader = csv.reader(drinks_files)
#         for line in drink_reader:
#             drinks.append(str(line))

# def print_favourites(data):
#     items = []
#     for name, drink in data.items():
#         items.append(f'{name}: {drink}')
#     print_table('Favourites', items)

# def get_menu_input(message: str):
#     try:
#         return int(input(f'{message} '))
#     except ValueError:
#         output("Menu items - numbers are the only input I understand")
#         return False

# # Round class for ordering drinks

# class Drinks:
#     def __init__(self):
#         self.menu_items = ['coke', 'coffee', 'tea', 'fanta', 'lemonade', 'pepsi', \
#         'tango', 'ice tea', 'green tea', 'strawberry milkshake']
 
#     def menu(self):
#         return f'Menu: {", ".join(self.menu_items).title()}'
 
#     def order(self):
#         on_menu = []
#         not_on_menu = []
#         return_values = []
 
#         string = (f'\n Our Menu: {", ".join(self.menu_items)}')
#         print(f'{string}\n')
#         self.order_items = \
#         input('Can I take your order?\nSeperate multiple items with a comma.\n: ').split(',')
 
#         for item in self.order_items:
#             if not item.strip():
#                 print(f'\n You did not order anything.')
#                 sys.exit()
#             if item.strip() in '\n'.join(self.menu_items):
#                 on_menu.append(item.strip())
 
#             else:
#                 not_on_menu.append(item.strip())
 
#         if on_menu:
#             string = (f'\n Your Order: {", ".join(on_menu).title()}')
#             print(f'{string}')
 
#         if not_on_menu:
#             string = \
#             (f'\n Sorry, {", ".join(not_on_menu).title()} is not on the menu.')
#             print(f'{string}\n')
 
#         print()
 
# drink = Drinks()

# Functions for user input
       
# def add_people_drinks():
#     with open(PEOPLE_FILE_PATH, 'w', newline = "") as people_files, open(DRINKS_FILE_PATH, 'w', newline = "") as drink_files:
#         people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
#         drink_writer = csv.writer(drink_files, quoting=csv.QUOTE_ALL)
#         b = int(input("Number of people: "))
#         for i in range(b):
#             name = input("Please enter the name of the person: ")
#             people_writer.writerow([name])
#             drink = input("Please enter drink name: ")
#             drink_writer.writerow([drink])
#             print("Name and drink has been added.")

# def exit_with_error(e, msg=None):
#     msg = msg if msg else 'Something went wrong'
#     print(f'{msg} with error: {str(e)} - exiting')
#     exit()

# def fav_path(path):
#     data = []
#     try:
#         with open(path, 'r') as file:
#             for line in file.readlines():
#                 if line == '':
#                     continue
#                 data.append(line.strip())
#     except FileNotFoundError as e:
#         exit_with_error(e, f'File "{path}" cannot be found')
#     except Exception as e:
#         exit_with_error(e, f'Unable to open file "{path}"')
#     return data

# def load_favourites(people, drinks):
#     for item in fav_path(FAVOURITES_FILE_PATH):
#         name, drink = item.split(":", 1)
#         if name in people and drink in drinks:
#             fav_drinks[name] = drink
#         else:
#             print('Unexpected data returned when loading favourites.')
#             print(f'Drink is known: {drink in drinks}')
#             print(f'Name is known: {name in people}')

# def save_favourites(data):
#     items = []
#     for item in data.items():
#         name, drink = item
#         items.append(f'{name}:{drink}')
#     try:
#         with open(FAVOURITES_FILE_PATH, 'w') as file:
#             file.writelines([f'{item}\n' for item in data])
#     except FileNotFoundError as e:
#         exit_with_error(e, f'File "{FAVOURITES_FILE_PATH}" cannot be found')
#     except Exception as e:
#         exit_with_error(e, f'Unable to open file "{FAVOURITES_FILE_PATH}"')


# def clear_screen():
#     os.system('clear')

# def print_main_menu():
#     clear_screen()
#     print(MENU)

# def print_menu(title, data):
#     items = []
#     for i, item in enumerate(data, start=1):
#         items.append(f'[{i}] {item}')
#     clear_screen()
#     print(f'{title}\n')
#     print('\n'.join(items), '\n')

# def get_selection(message):
#     try:
#         return int(input(f'{message} \n'))
#     except ValueError:
#         print("Please enter a valid command ranging from 1 to 7")
    
# def wait():
#     input('Press ENTER to return to the menu') 

# def validate_menu_input(index, data):
#     if index < 0 or index >= len(data):
#         print(f'"{index}" is not a valid option from that menu\n')
#         wait()
#         return False
#     return True

# def select_from_menu(message, data):
#     print_menu(message, data)
#     index = get_menu_input('Enter your selection:')
#     if not validate_menu_input(index, data):
#         return False
#     return data[index]

# def output(text):
#     print(f'\n{text}')


def run():
    print_main_menu()
    command = get_menu_input('Enter your selection:')
    if command is False:
        print("Please choose a number from the menu")
        wait()

# if conditions instructing the menu
 
    if command == GET_PEOPLE:
        load_people()
        print_table("People", print_db_data(people))
        wait()
        run()
    elif command == GET_DRINKS:
        load_drinks()
        print_table("Drinks", print_db_data(drinks))
        wait()
        run()
    elif command == add_people:
        insert_to_people_table()
        wait()
        run()
    elif command == add_drinks:
        insert_to_drink_table()
        wait()
        run()
    elif command == Set_fav:
        set_drink_favs()
        wait()
    elif command == View_fav:
        load_favs_from_db()
        print_table("Favourite Drinks", print_db_favs(favourites))
        wait()
        run()
    elif command == order_drinks:
        drink = Drinks()
        drink.order()
        wait()
        run()
    elif command == exit_menu:
        print(f'Thank you for using {APP_NAME}')
        exit()
    else:
        print(f'"{command}" is not a command that I recognise.')
        wait()
        run()

def start():
    load_people()
    load_drinks()
    load_favs_from_db()
    run()

if __name__ == '__main__':
    start()