import unittest
from unittest.mock import patch

from exercises.input_output import *


class TestingInputAndOutput(unittest.TestCase):
    @patch("builtins.input", side_effect=["2", "3"])
    def test_make_user_calculation(self, mock_input):
        self.assertEqual(make_user_calculation(), 6)

    @patch("builtins.input", side_effect=["8", "3"])
    def test_make_user_calculation(self, mock_input):
        self.assertEqual(make_user_calculation(), 24)

    def test_display_string(self):
        self.assertEqual(
            display_string("Hello", "world,", "Loïc"), "Hello**world,**Loïc"
        )

    def test_display_octal(self):
        self.assertEqual(display_octal(650), 1212)
        self.assertEqual(display_octal(550), 1046)
        self.assertEqual(display_octal(1550), 3016)

    def test_display_float(self):
        self.assertEqual(display_float(3.141516), 3.14)
        self.assertEqual(display_float(458.541315), 458.54)

    @patch("builtins.input", return_value=("1.2 1.5 1.6"))
    def test_display_list(self, mock_input):
        self.assertEqual(display_list(), [1.2, 1.5, 1.6])


if __name__ == "__main__":
    unittest.main()
