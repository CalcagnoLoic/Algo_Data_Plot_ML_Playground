import unittest

from exercises.data_structure import *


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


if __name__ == "__main__":
    unittest.main()
