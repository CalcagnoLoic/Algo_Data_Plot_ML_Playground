import unittest

from exercises.function import *


class TestingFunction(unittest.TestCase):
    def test_presentation(self):
        self.assertEqual(
            presentation("Loïc", 31), "My name is Loïc and I'm 31 years old."
        )

    def test_func1(self):
        self.assertEqual(func1("20", "20"), "20\n20\n")
        self.assertEqual(func1("20", "30", "40"), "20\n30\n40\n")

    def test_calculation(self):
        self.assertEqual(calculation(40, 10), [50, 30])

    def test_show_employee(self):
        self.assertEqual(show_employee("Loïc", 10500), "Name: Loïc Salary: 10500")
        self.assertEqual(show_employee("John"), "Name: John Salary: 9000")

    def test_outer_function(self):
        self.assertEqual(outer_function(5, 10), 20)

    def test_recursiv(self):
        self.assertEqual(recursiv(10), 55)

    def test_display_student(self):
        self.assertEqual(
            show_student("Loïc", 31), "My name is Loïc and I'm 31 years old."
        )

    def test_even_list(self):
        self.assertEqual(even_list(), [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_largest_item(self):
        self.assertEqual(largest_item([4, 6, 8, 24, 12, 2]), 24)


if __name__ == "__main__":
    unittest.main()
