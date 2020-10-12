import csv
import pymysql
# from prettytable import from_cursor
from menu.table import print_table


# Reads people list

# PEOPLE_FILE_PATH = 'src/data/people.csv'

# def people_list():
#     with open(PEOPLE_FILE_PATH, 'r') as people_files:
#         people_reader = csv.reader(people_files)
#         for line in people_reader:
#             people.append(str(line))

# # Reads drink list

# DRINKS_FILE_PATH = 'src/data/drinks.csv'

# def drink_list():
#     with open(DRINKS_FILE_PATH, 'r') as drinks_files:
#         drink_reader = csv.reader(drinks_files)
#         for line in drink_reader:
#             drinks.append(str(line))

# ### Writes to people and drink list
# # Getting user input
# def add_people_drinks():
#     # with open(PEOPLE_FILE_PATH, 'w', newline="") as people_files, open(DRINKS_FILE_PATH, 'w', newline="") as drink_files:
#     #     people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
#     #     drink_writer = csv.writer(drink_files, quoting=csv.QUOTE_ALL)
#     b = int(input("Number of people: "))
#     for _ in range(b):
#         # This for loop looks at the amount entered in Number of people and repeats the process below that many times.
#         people = input("Please enter the name of the person: ")
#         # people_writer.writerow([name])
#         drink = input("Please enter drink name: ")
#         # drink_writer.writerow([drink])
#         # do_the_file_stuff(PEOPLE_FILE_PATH, DRINKS_FILE_PATH, name, drink)
#         add_drink_person_to_csv_file(PEOPLE_FILE_PATH, [people])
#         add_drink_person_to_csv_file(DRINKS_FILE_PATH, [drink])
#         print("Name and drink has been added.")

# def add_drink_person_to_csv_file(path, data):
#     with open(path, 'w', newline="") as file:
#         # people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
#         writer = csv.writer(file, quoting=csv.QUOTE_ALL)
#         # people_writer.writerow([name])
#         writer.writerow(data)
people = {}
drinks = {}
favourites = {}

def string_exist(string):
    if string:
        return True
    elif string == "" or " ":
        return False
    else:
        return False

def print_db_data(data):
    data_list = []
    for id, name in data.items():
        data_list.append(f"{id} | {name}")
    return data_list

def print_db_favs(data): 
    favs_list = []

    for name, id in data.items():
        favs_list.append(f"{name} | {id}")
    return favs_list

def connect():
    return pymysql.connect(host="localhost", 
                            port=33066,
                            db="brewapp",
                            user="root",
                            password="password",
                            autocommit=True
                            )

def load_people():
    people 
    print("Starting SQL")
    connection = connect()
    with connection.cursor() as cursor:
        sql = f'SELECT * FROM People'
        cursor.execute(sql)
        # mytable = from_cursor(cursor)
        try:
            people_data = cursor.fetchall()

        except Exception as err:
            print(f"ERROR with:\n{err}")
    
        finally:
                connection.close()
                cursor.close()
        
        for id, name, age in people_data:
            people[id] = name, age

def insert_people_db(name, age):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            value = name, age
            sql = 'INSERT INTO People (Name, Age) VALUES (%s, %s)'
            cursor.execute(sql, value)
        cursor.close()
    finally:
        connection.close()

def insert_to_people_table():
    print("Please enter the customer's name")
    try:
        name = input("\nName: ").strip()
        age = input("\nAge: ").strip()

        if string_exist(name):
            pass
        else:
            print("Please add data for it to proceed.")
            return 

        if name in people:
            print(f"\n'{name}' is already on the list, please insert a different names.")
            return

        else:
            insert_people_db(name, age)
            return  

    except Exception as e:
        print(f"ERROR:\n{e}")
        pass

    finally:
        return

def load_drinks():
    global drinks
    print("Starting SQL")
    connection = connect()
    with connection.cursor() as cursor:
        sql = f'SELECT * FROM Drinks'
        cursor.execute(sql)
        # mytable = from_cursor(cursor)
        try:
            drink_data = cursor.fetchall()

        except Exception as err:
            print(f"ERROR with:\n{err}")
    
        finally:
                connection.close()
                cursor.close()
        
        for id, drink, price in drink_data:
            drinks[id] = drink, price

def insert_drink_db(drink, price):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            value = drink, price
            sql = 'INSERT INTO Drinks (Drink, Price) VALUES (%s, %s)'
            cursor.execute(sql, value)
        cursor.close()
    finally:
        connection.close()

def insert_to_drink_table():
    print("Please enter the drink's name")
    try:
        drink = input("\nDrink: ").strip()
        price = input("\nPrice: ").strip()

        if string_exist(drink):
            pass
        else:
            print("Please add data for it to proceed.")
            return 

        if drink in drinks:
            print(f"\n'{drink}' is already on the list, please insert a different drink.")
            return

        else:
            insert_drink_db(drink, price)
            return  

    except Exception as e:
        print(f"ERROR:\n{e}")
        pass

    finally:
        return

def load_favs_from_db():
    global favourites
    connection = connect()

    with connection.cursor() as cursor:
        try:    
            sql = 'SELECT DrinkID, PersonID FROM FavouriteDrinks'
            cursor.execute(sql)
            favs_data = cursor.fetchall()
            
            for drinkid, personid in favs_data:
                drinkname = drinks.get(drinkid)
                peoplename = people.get(personid)
                favourites[peoplename] = drinkname

        except Exception as err:
            print(f"ERROR with:\n{err}")

        finally:
            cursor.close()
            connection.close()
        
    

def write_fave_to_db(id, drinkid):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            user_id = int(id)
            user_pref = int(drinkid)
            sql = 'INSERT INTO FavouriteDrinks (DrinkID, PersonID) VALUES (%s, %s)'
            cursor.execute(sql, [user_pref, user_id])

    except Exception as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        connection.close()




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