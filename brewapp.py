import os 
import sys
import csv
from src.menu.commands import GET_PEOPLE, GET_DRINKS, add_people, add_drinks, Set_fav, View_fav, order_drinks, exit_menu
from src.core.rounds import Drinks
from src.persistence.people_drinks import people, drinks, favourites, load_people, insert_people_db, drinks, insert_to_people_table, load_drinks, print_db_data, insert_to_drink_table, load_favs_from_db, print_db_favs
from src.persistence.favourites import set_drink_favs
from src.menu.table import print_table 
from src.menu.index_menu import MENU, APP_NAME, get_menu_input, get_selection, print_main_menu, clear_screen, select_from_menu, wait

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