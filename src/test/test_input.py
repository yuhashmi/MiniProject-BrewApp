import unittest
from unittest.mock import Mock, patch
from src.menu.menu import select_from_menu


# def select_from_menu(message, data):
#     print_menu(message, data)
#     index = get_menu_input('Enter your selection:')
#     if not validate_menu_input(index, data):
#         return False
#     return data[index]


class Test_Select_From_Menu(unittest.TestCase):
    # When a function/class is imported using `from X import Y` the resolution path to the
    # target being patched is actually in the namespace where the import occurs instead of
    # where the target is defined.
    #
    # This means that if module z.py import Y using `from X import Y` syntax the patch target
    # path tto patch Y is z.Y instead of X.Y
    @patch("src.menu.menu.select_from_menu")
    @patch("src.menu.menu.print_menu")
    @patch("src.menu.menu.get_menu_input")
    @patch("src.menu.menu.validate_menu_input")
    def test_when_number_is_returned_from_select_return_the_person_at_that_position(self, mock_select_from_menu, mock_print_menu, mock_get_menu_input, mock_validate_menu_input):
        # Arrange
        message = "Yousef"
        data = ["Water", "Coffee", "Tea"]
        select_from_menu.return_value = 2
        expect = 'Coffee'
        # Act
        actual = select_from_menu(message, data)
        # Assert
        self.assertEqual(actual, expect)
# provides a command-line interface to the test script
if __name__ == "__main__":
    unittest.main()

# class Test_Add_Person_From_Menu(unittest.TestCase):
# @patch("builtins.print")
#     def test_people_drinks_addition(self, mock_add_people_drinks):
#         # Arrange 
#         input_mock.return_value = "Yousef"

#         expected = ["Yousef"]
#         # Act
#         print_divider(30)

#         # Assert 
#         mock_add_people_drinks.assert_called_once_with('+==============================+')

# def add_people_drinks():
#     # with open(PEOPLE_FILE_PATH, 'w', newline="") as people_files, open(DRINKS_FILE_PATH, 'w', newline="") as drink_files:
#     #     people_writer = csv.writer(people_files, quoting=csv.QUOTE_ALL)
#     #     drink_writer = csv.writer(drink_files, quoting=csv.QUOTE_ALL)
#     b = int(input("Number of people: "))
#     for _ in range(b):
#         # This for loop looks at the amount entered in Number of people and repeats the process below that many times.
#         name = input("Please enter the name of the person: ")
#         # people_writer.writerow([name])
#         drink = input("Please enter drink name: ")
#         # drink_writer.writerow([drink])
#         # do_the_file_stuff(PEOPLE_FILE_PATH, DRINKS_FILE_PATH, name, drink)
#         add_drink_person_to_csv_file(PEOPLE_FILE_PATH, [name])
#         add_drink_person_to_csv_file(DRINKS_FILE_PATH, [drink])
#         print("Name and drink has been added.")
#         return name, drink