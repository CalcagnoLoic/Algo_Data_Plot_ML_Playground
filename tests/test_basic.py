import unittest
from unittest.mock import patch

from exercises.basic import (
    make_calculation,
    print_char,
    remove_chars,
    check_first_last_number,
    display_5_fold,
    is_palindrom,
    new_list,
    exponent,
)


class TestingBasic(unittest.TestCase):
    def test_make_calculation(self):
        self.assertEqual(make_calculation(20, 30), "The result is 600.")
        self.assertEqual(make_calculation(40, 30), "The result is 70.")

    @patch("builtins.input", return_value="pynative")
    def test_print_char(self, mock_input):
        expected_output = "p\nn\nt\nv\n"
        self.assertEqual(print_char(), expected_output)

    def test_remove_chars(self):
        self.assertEqual(remove_chars("pynative", 4), "tive")
        self.assertEqual(remove_chars("pynative", 2), "native")

    def test_check_first_last_number(self):
        self.assertEqual(check_first_last_number([10, 20, 30, 40, 10]), True)
        self.assertEqual(check_first_last_number([75, 65, 35, 75, 30]), False)

    def test_display_5_fold(self):
        self.assertEqual(display_5_fold([10, 20, 33, 46, 55]), [10, 20, 55])

    def test_is_palindrom(self):
        self.assertEqual(is_palindrom("545"), True)
        self.assertEqual(is_palindrom("145"), False)

    def test_new_list(self):
        self.assertEqual(
            new_list([10, 20, 25, 30, 35], [40, 45, 60, 75, 90]), [25, 35, 40, 60, 90]
        )

    def test_exponent(self):
        self.assertEqual(exponent(2, 2), 4)
        self.assertEqual(exponent(5, 2), 25)


if __name__ == "__main__":
    unittest.main()
