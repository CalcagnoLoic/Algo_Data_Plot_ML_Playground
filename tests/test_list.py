import unittest

from exercises.list import *


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


if __name__ == "__main__":
    unittest.main()
