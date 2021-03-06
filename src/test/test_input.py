import unittest
from unittest.mock import Mock, patch
from src.menu.index_menu import select_from_menu


# def select_from_menu(message, data):
#     print_menu(message, data)
#     index = get_menu_input('Enter your selection:')
#     if not validate_menu_input(index, data):
#         return False
#     return data[index]

# def select_from_menu(message, data):
#     print_menu(message, data)
#     index = get_menu_input(f'{message}')
#     return validate_menu_input(index, data)


class Test_Select_From_Menu(unittest.TestCase):
    # When a function/class is imported using `from X import Y` the resolution path to the
    # target being patched is actually in the namespace where the import occurs instead of
    # where the target is defined.
    #
    # This means that if module z.py import Y using `from X import Y` syntax the patch target
    # path tto patch Y is z.Y instead of X.Y
    @patch("src.menu.index_menu.validate_menu_input")
    @patch("src.menu.index_menu.get_menu_input")
    @patch("src.menu.index_menu.print_menu")
    @patch("src.menu.index_menu.select_from_menu")
    def test_when_number_is_returned_from_select_return_the_person_at_that_position(self, mock_select_from_menu, mock_print_menu, mock_get_menu_input, mock_validate_menu_input):
        # Arrange
        title = "Drinks"
        message = "1"
        data = ["Water", "Coffee", "Tea"]
        mock_select_from_menu.return_value = "Coffee"
        expect = 'Coffee'
        expect1 = '1'
        # Act
        actual = select_from_menu(message, data)
        actual1 = mock_get_menu_input('Enter your selection: ')
        # Assert
        self.assertEqual(actual, expect)
        mock_print_menu.assert_called_once_with(message, data)
        mock_get_menu_input.assert_called_once_with(message)
        mock_validate_menu_input.assert_called_once_with(1, data)

# provides a command-line interface to the test script
if __name__ == "__main__":
    unittest.main()
