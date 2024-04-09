import unittest

from exercises.string import *


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


if __name__ == "__main__":
    unittest.main()
