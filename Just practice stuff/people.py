import csv

people = []
drinks = []



def files_open_close():
    with open('people.txt', 'r') as people_files, open('drinks.txt', 'r') as drink_files:
        for line in people_files:
            people.append(line.strip().split(","))
        for line in drink_files:
            drinks.append(line.strip().split(","))
    print(people, drinks)

def files_write_close():
    with open('people.txt', 'a') as people_files, open('drinks.txt', 'a') as drink_files:
        b = int(input("Number of people: "))
        for i in range(b):
            name = input("Enter name: ")
            people_files.write(name + "\n")
            drink = input("Enter drink: ")
            drink_files.write(drink + "\n")
            print()

def people_list():
    with open('people.txt', 'r') as people_files:
        for line in people_files:
            people.append(line.strip().split(","))

def load_favourites(people, drinks):
    for item in load_from_file(FAVOURITES_FILE_PATH):
        # Unpacking the items in the list to separate variables
        # https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
        # I know items.split will return a list with two items, because of the second argument
        # it will only split once even if there are more instances of ':' in the string
        name, drink = item.split(":", 1)
        if name in people and drink in drinks:
            favourite_drinks[name] = drink
        else:
            print('Unexpected data returned when loading favourites.')
            print(f'Drink is known: {drink in drinks}')
            print(f'Name is known: {name in people}')

        

files_open_close()
files_write_close()

