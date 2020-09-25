import os

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

def get_menu_input(message: str):
    try:
        return int(input(f'{message} '))
    except ValueError:
        output("Menu items - numbers are the only input I understand")
        return False

def clear_screen():
    os.system('clear')

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
        print("Please enter a valid command ranging from 1 to 7")
    
def wait():
    input('Press ENTER to return to the menu') 

def validate_menu_input(index, data):
    if index < 0 or index >= len(data):
        print(f'"{index}" is not a valid option from that menu\n')
        wait()
        return False
    return data[index]

def select_from_menu(message, data):
    print_menu(message, data)
    index = get_menu_input(f'{message}')
    return validate_menu_input(index, data)

def output(text):
    print(f'\n{text}')