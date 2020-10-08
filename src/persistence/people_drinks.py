import csv
import pymysql
from menu.table import print_table
from core.people_class import People
from core.drink_class import Drink


# Reads people list

PEOPLE_FILE_PATH = 'src/data/people.csv'

people = []

def people_list():
    with open(PEOPLE_FILE_PATH, 'r') as people_files:
        people_reader = csv.reader(people_files)
        for line in people_reader:
            people.append(str(line))

# Reads drink list

DRINKS_FILE_PATH = 'src/data/drinks.csv'

drinks = []

def drink_list():
    with open(DRINKS_FILE_PATH, 'r') as drinks_files:
        drink_reader = csv.reader(drinks_files)
        for line in drink_reader:
            drinks.append(str(line))

### Writes to people and drink list
# Getting user input
def add_people_drinks():
    # with open(PEOPLE_FILE_PATH, 'w', newline="") as people_files, open(DRINKS_FILE_PATH, 'w', newline="") as drink_files:
    #     people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
    #     drink_writer = csv.writer(drink_files, quoting=csv.QUOTE_ALL)
    b = int(input("Number of people: "))
    for _ in range(b):
        # This for loop looks at the amount entered in Number of people and repeats the process below that many times.
        people = input("Please enter the name of the person: ")
        # people_writer.writerow([name])
        drink = input("Please enter drink name: ")
        # drink_writer.writerow([drink])
        # do_the_file_stuff(PEOPLE_FILE_PATH, DRINKS_FILE_PATH, name, drink)
        add_drink_person_to_csv_file(PEOPLE_FILE_PATH, [people])
        add_drink_person_to_csv_file(DRINKS_FILE_PATH, [drink])
        print("Name and drink has been added.")

def add_drink_person_to_csv_file(path, data):
    with open(path, 'w', newline="") as file:
        # people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # people_writer.writerow([name])
        writer.writerow(data)


def load_people():
    data = []
    print("Starting SQL")
    connection = pymysql.connect(host="localhost", port=33066, user="root", password="password", database="brewapp")
    with connection.cursor() as cursor:
        sql = f'SELECT * FROM People'
        cursor.execute(sql)
    try:
        while True:
            people_data = cursor.fetchone()
            if not people_data:
                break
            data.append(People(
                        people_data[0],
                        people_data[1],
                        ))
            connection.commit()
    finally:
            connection.close()
    return data

def insert_people_db(People):
    connection = pymysql.connect(host="localhost", port=33066, user="root", password="password", database="brewapp")
    try:
        with connection.cursor() as cursor:
            data = [str(People.id), People.name, People.age]
            sql = 'INSERT INTO People (ID, Name, Age) VALUES (%s, %s, %s)'
            cursor.execute(sql, data)
            connection.commit()
        cursor.close()
    finally:
        connection.close()

def insert_people_sql_func():
    ppl_name = input("Please enter first name: ")
    age = input("Please enter age: ")
    people_1 = People(ppl_name, age)
    insert_people_db(people_1)
    print(f'{ppl_name} has been added') 

def insert_drink(self, drink):
        connection = pymysql.connect(host="localhost", port=33066, user="root", password="password", database="brewapp")
        print('Connection made')
        try:
            with connection.cursor() as cursor:
                data = [str(Drink.drinkid), Drink.drink, Drink.price]
                sql = 'INSERT INTO Drinks (DrinkID, Drink, Price) VALUES (%s, %s, %s)'
                cursor.execute(sql, data)
                connection.commit()
        finally:
            connection.close()

def load_drinks(self):
        data = []
        connection = pymysql.connect(host="localhost", port=33066, user="root", password="password", database="brewapp")
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * from drink'
                cursor.execute(sql)
                while True:
                    drink_data = cursor.fetchone()
                    if not drink_data:
                        break
                    data.append(Drink(drink_data[0], drink_data[1], drink_data[2]))
                connection.commit()
        finally:
            connection.close()
        return data




# # Using files - writing to files
# def do_the_file_stuff(people_file_path, drink_file_path, name, drink):
#     # Opening two files and adding data to them
#     # with open(people_file_path, 'w', newline="") as people_files, open(drink_file_path, 'w', newline="") as drink_files:
#     #     people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
#     #     drink_writer = csv.writer(drink_files, quoting=csv.QUOTE_ALL)
#     #     people_writer.writerow([name])
#     #     drink_writer.writerow([drink])
#     add_drink_person_to_csv_file(people_file_path, [name])
#     add_drink_person_to_csv_file(drink_file_path, [drink])