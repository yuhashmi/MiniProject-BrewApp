import csv
from menu.table import print_table

FAVOURITES_FILE_PATH = './data/favourites.csv'

fav_drinks = {}

def print_favourites(data):
    items = []
    for name, drink in data.items():
        items.append(f'{name}: {drink}')
    print_table('Favourites', items)

def exit_with_error(e, msg=None):
    msg = msg if msg else 'Something went wrong'
    print(f'{msg} with error: {str(e)} - exiting')
    exit()

def load_path(path):
    data = []
    try:
        with open(path, 'r') as file:
            fav_reader = csv.DictReader(file)
            for line in fav_reader:
                data.append(str(line))
    except FileNotFoundError as e:
        exit_with_error(e, f'File "{path}" cannot be found')
    except Exception as e:
        exit_with_error(e, f'Unable to open file "{path}"')
    return data

def load_favourites(people, drinks):
    for item in load_path(FAVOURITES_FILE_PATH):
        name, drink = item.split(":", 1)
        if name in people and drink in drinks:
            fav_drinks[name] = drink
        else:
            print('Unexpected data returned when loading favourites.')
            print(f'Drink is known: {drink in drinks}')
            print(f'Name is known: {name in people}')

def save_favourites(data):
    items = []
    for item in data.items():
        name, drink = item
        items.append(f'{name}:{drink}')
        write_to_file(FAVOURITES_FILE_PATH, fav_drinks)
    
def write_to_file(path, data):
    with open(path, 'w', newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow({data})