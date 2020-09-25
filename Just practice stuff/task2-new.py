people = ['Joe', 'John', 'Juan', 'Jack', 'Jill']
drinks = ['Pepsi', 'Vodka', 'Green Tea', 'Cola', 'Fanta']

GET_PEOPLE = 1
GET_DRINKS = 2
select_id = 3
exit_menu = 4

APP_NAME = "BrIW"

def print_table(title, data):
    for item in data:
        print(f'| {item}')

def menu():
    print("Welcome to {APP_NAME} v0.1!")
    print("Please, select an option by entering a number:\n\
    [1] Get all people\n\
    [2] Get all drinks\n\
    [3] Select people and drinks\n\
    [4] Exit\n")


menu()
option = int(input("Enter your selection"))

while option !=0:
    if option == GET_PEOPLE:
        print_table("People", people)
    elif option == GET_DRINKS:
        print_table("Drinks", drinks)
    elif option == select_id:
        print("select id(coming soon)")
    elif option == exit_menu:
        print("Thank you for using {APP_NAME}")
    else:
        print("Please make a selection from the options.")

print()
menu()
option = int(input("Enter your selection"))
