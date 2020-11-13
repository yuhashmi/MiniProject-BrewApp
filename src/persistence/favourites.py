import csv
from src.menu.table import print_table
from src.persistence.people_drinks import people, drinks, load_people, load_drinks, print_db_data, load_favs_from_db, write_fave_to_db

# sql database setting favourites

def check_person_id_valid(id):
    if id not in people.keys():
        id = input("ID does not exist, please enter a valid ID: ")
    return id

def check_drink_id_valid(drinkid):
    if drinkid not in drinks.keys():
        drinkid = input("ID does not exist, please enter a valid ID: ")
    return drinkid

def set_drink_favs():
    load_people()
    load_drinks()

    try:
        print_table("people", print_db_data(people))
        id = input("Please enter the user ID to set Favourite drink to: ")
        check_person_id_valid(int(id))

        print_table("drinks", print_db_data(drinks))
        drinkid = input("Please enter your Favourite drink's ID: ")
        check_drink_id_valid(int(drinkid))
        
        write_fave_to_db(id, drinkid)

    except Exception as e:
        print(f"ERROR:\n{e}")
    
    finally:
        pass

