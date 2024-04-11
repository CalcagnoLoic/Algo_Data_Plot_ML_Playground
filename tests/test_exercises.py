import unittest
from unittest.mock import patch

from exercises.basic import *
from exercises.input_output import *
from exercises.function import *
from exercises.string import *
from exercises.data_structure import *
from exercises.list import *
from exercises.dictionary import *


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


class TestingString(unittest.TestCase):
    def test_blend_string(self):
        self.assertEqual(blend_string("hello", "world"), "heworldllo")
        self.assertEqual(blend_string("Ault", "Kelly"), "AuKellylt")

    def test_blend_string_v2(self):
        self.assertEqual(blend_string_v2("Hello", "World"), "HWlrod")
        self.assertEqual(blend_string_v2("America", "Japan"), "AJrpan")

    def test_first_lowercase(self):
        self.assertEqual(first_lowercase("PyNaTive"), "yaivePNT")

    def test_count_sum_avg(self):
        self.assertEqual(
            count_sum_avg("PYnative29@#8496"), "Sum: 38 Average: 6.333333333333333"
        )

    def test_remove_empty_s(self):
        self.assertEqual(
            remove_empty_s(["Emma", "Jon", "", "Kelly", None, "Eric", ""]),
            ["Emma", "Jon", "Kelly", "Eric"],
        )

    def test_remove_special_chars(self):
        self.assertEqual(
            remove_special_chars("/*Jon is @developer & musician"),
            "Jon is developer  musician",
        )

    def test_remove_all_letters(self):
        self.assertEqual(remove_all_letters("I am 25 years and 10 months old"), "2510")

    def test_remove_special_chars(self):
        self.assertEqual(
            replace_special_chars("/*Jon is @developer & musician!!"),
            "##Jon is #developer # musician##",
        )


class TestingDataStructure(unittest.TestCase):
    def test_create_new_list(self):
        self.assertEqual(
            create_new_list([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28]),
            [6, 12, 18, 4, 12, 20, 28],
        )

    def test_remove_add_into_list(self):
        self.assertEqual(
            remove_add_into_list([34, 54, 67, 89, 11, 43, 94]),
            [34, 54, 11, 67, 89, 43, 94, 11],
        )

    def test_count_occurs(self):
        self.assertEqual(
            count_occurs([11, 45, 8, 11, 23, 45, 23, 45, 89]),
            {11: 2, 45: 3, 8: 1, 23: 2, 89: 1},
        )

    def test_zip_set(self):
        self.assertEqual(
            zip_set([2, 3, 4, 5, 6, 7, 8], [4, 9, 16, 25, 36, 49, 64]),
            {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)},
        )

    def test_exist_dict_list(self):
        self.assertEqual(
            exist_dict_list(
                [47, 64, 69, 37, 76, 83, 95, 97],
                {"Jhon": 47, "Emma": 69, "Kelly": 76, "Jason": 97},
            ),
            [47, 69, 76, 97],
        )

    def test_find_min_max(self):
        self.assertEqual(
            find_min_max([87, 45, 41, 65, 94, 41, 99, 94]), "Min: 41 Max: 99"
        )


class TestingList(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(
            reverse_list([100, 200, 300, 400, 500]), [500, 400, 300, 200, 100]
        )

    def test_concat_list(self):
        self.assertEqual(
            concat_list(["M", "na", "i", "Ke"], ["y", "me", "s", "lly"]),
            ["My", "name", "is", "Kelly"],
        )

    def test_square_list(self):
        self.assertEqual(square_list([1, 2, 3, 4, 5, 6, 7]), [1, 4, 9, 16, 25, 36, 49])

    def test_concat_list_v2(self):
        self.assertEqual(
            concat_list_v2(["Hello ", "take "], ["Dear", "Sir"]),
            ["Hello Dear", "Hello Sir", "take Dear", "take Sir"],
        )

    def test_iterate_simultaneously(self):
        self.assertEqual(
            iterate_simultaneously([10, 20, 30, 40], [100, 200, 300, 400]),
            [(10, 400), (20, 300), (30, 200), (40, 100)],
        )

    def test_add_specific_item(self):
        self.assertEqual(
            add_specific_item([10, 20, [300, 400, [5000, 6000], 500], 30, 40]),
            [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40],
        )

    def test_nested_list(self):
        self.assertEqual(
            extend_nested_list(
                ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"],
                ["h", "i", "j"],
            ),
            [
                "a",
                "b",
                ["c", ["d", "e", ["f", "g", "h", "i", "j"], "k"], "l"],
                "m",
                "n",
            ],
        )


class TestingDictionary(unittest.TestCase):
    def test_transform_list_into_dict(self):
        self.assertEqual(
            transform_list_into_dict(["Ten", "Twenty", "Thirty"], [10, 20, 30]),
            {"Ten": 10, "Twenty": 20, "Thirty": 30},
        )

    def test_merge_dict(self):
        self.assertEqual(
            merge_dict(
                {"Ten": 10, "Twenty": 20, "Thirty": 30},
                {"Thirty": 30, "Fourty": 40, "Fifty": 50},
            ),
            {"Ten": 10, "Twenty": 20, "Thirty": 30, "Fourty": 40, "Fifty": 50},
        )

    def test_nested_dict(self):
        sampleDict = {
            "class": {
                "student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}
            }
        }
        self.assertEqual(nested_dict(sampleDict), 80)

    def test_initialize_dist(self):
        self.assertEqual(
            initialize_dict(
                ["Kelly", "Emma"], {"designation": "Developer", "salary": 8000}
            ),
            {
                "Kelly": {"designation": "Developer", "salary": 8000},
                "Emma": {"designation": "Developer", "salary": 8000},
            },
        )

    def test_extract_keys(self):
        sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
        keys = ["name", "salary"]

        self.assertEqual(
            extract_keys(sampleDict, keys), {"name": "Kelly", "salary": 8000}
        )

    def test_delete_keys(self):
        sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
        keys = ["name", "salary"]

        self.assertEqual(delete_keys(sampleDict, keys), {"city": "New york", "age": 25})

    def test_check_values(self):
        self.assertEqual(
            check_values({"a": 100, "b": 200, "c": 300}, 200),
            "La valeur '200' est bien présente",
        )
        self.assertEqual(check_values({"a": 100, "b": 200, "c": 300}, 20), None)

    def test_min_key(self):
        sample_dict = {"Physics": 82, "Math": 65, "history": 75}

        self.assertEqual(min_key(sample_dict), "Math")

    def test_update_nested_dictionary(self):
        sample_dict = {
            "emp1": {"name": "Jhon", "salary": 7500},
            "emp2": {"name": "Emma", "salary": 8000},
            "emp3": {"name": "Brad", "salary": 500},
        }

        new_dict = {
            "emp1": {"name": "Jhon", "salary": 7500},
            "emp2": {"name": "Emma", "salary": 8000},
            "emp3": {"name": "Brad", "salary": 8500},
        }

        self.assertEqual(update_nested_dictionary(sample_dict), new_dict)


if __name__ == "__main__":
    unittest.main()
