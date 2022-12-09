import os
import unittest
from solution import *


class TestSolution(unittest.TestCase):

    def test_read_field_from_file(self):
        current_directory = os.path.dirname(__file__)
        filenames = [
            os.path.join(current_directory, 'example.txt'),
            os.path.join(current_directory, 'input.txt'),
        ]
        for filename in filenames:
            field = read_field_from_file(filename)
            self.assertIsInstance(field, list)
            self.assertIsInstance(field[0], list)
            self.assertIsInstance(field[0][0], int)


    def test_is_row_visible(self):
        positive_cases = [
            [5, 4, 3, 2, 1],
            [2, 1],
        ]
        negative_cases = [
            [2, 4, 3, 2, 1],
            [4, 4, 3, 2, 1],
        ]
        for row in positive_cases:
            self.assertTrue(is_row_visible(row))
        for row in negative_cases:
            self.assertFalse(is_row_visible(row))


    def test_is_tree_visible(self):
        field = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        cases = [
            ((1,1), True),
            ((1,2), True),
            ((1,3), False),
            ((2,1), True),
            ((2,2), False),
            ((2,3), True),
            ((3,1), False),
            ((3,2), True),
            ((3,3), False),
        ]
        for position, expected in cases:
            self.assertEqual(is_tree_visible(field, position), expected)


    def test_get_row(self):
        field = [
            [1, 2, 3, 4, 5],
            [2, 6, 7, 8, 4],
            [3, 7, 9, 7, 3],
            [4, 8, 7, 6, 2],
            [5, 4, 3, 2, 1],
        ]
        positive_cases = [
            ((1, 1), Direction.DOWN, [6, 7, 8, 4]),
            ((1, 1), Direction.RIGHT, [6, 7, 8, 4]),
            ((1, 1), Direction.LEFT, [6, 2]),
            ((1, 2), Direction.LEFT, [7, 6, 2]),
            ((1, 2), Direction.RIGHT, [7, 8, 4]),
            ((2, 2), Direction.RIGHT, [9, 7, 3]),
            ((2, 2), Direction.DOWN, [9, 7, 3]),
            ((2, 2), Direction.LEFT, [9, 7, 3]),
            ((2, 2), Direction.UP, [9, 7, 3]),
        ]
        negative_cases = [
            ((1, 1), Direction.DOWN, [2, 6, 7, 8, 4]),
            ((1, 1), Direction.DOWN, [7, 8, 4]),
            ((1, 1), Direction.RIGHT, [2, 6, 7, 8, 4]),
            ((1, 1), Direction.RIGHT, [7, 8, 4]),
            ((1, 1), Direction.LEFT, [2, 6]),
            ((1, 1), Direction.LEFT, [2]),
        ]

        for position, direction, expected_row in positive_cases:
            self.assertEqual(get_row(field, position, direction), expected_row)
        for position, direction, expected_row in negative_cases:
            self.assertNotEqual(get_row(field, position, direction), expected_row)


    def test_get_perimeter_length(self):
        cases = [
            ([[0] * 1] * 1, 1),
            ([[0] * 1] * 2, 2),
            ([[0] * 2] * 2, 4),
            ([[0] * 2] * 3, 6),
            ([[0] * 3] * 3, 8),
            ([[0] * 3] * 4, 10),
            ([[0] * 4] * 4, 12),
            ([[0] * 1] * 5, 5),
            ([[0] * 2] * 5, 10),
            ([[0] * 3] * 5, 12),
            ([[0] * 4] * 5, 14),
            ([[0] * 5] * 5, 16),
        ]
        for field, expected_perimeter in cases:
            self.assertEqual(get_perimeter_length(field), expected_perimeter)


    def test_get_inner_visible_count(self):
        field = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(get_inner_visible_count(field), 5)


    def test_get_scenic_score(self):
        field = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        cases = [
            ((1,1), 1),
            ((1,2), 4),
            ((1,3), 1),
            ((2,1), 6),
            ((2,2), 1),
            ((2,3), 2),
            ((3,1), 1),
            ((3,2), 8),
            ((3,3), 3),
        ]
        for position, expected_score in cases:
            self.assertEqual(get_scenic_score(field, position), expected_score)


    def test_get_highest_scenic_score(self):
        field = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
        self.assertEqual(get_highest_scenic_score(field), 8)


if __name__ == '__main__':
    unittest.main()
