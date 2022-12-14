import os
import unittest
from solution import *
from test_data import test_data_for_move_rope


class TestSolution(unittest.TestCase):

    def test_read_motions_from_file(self):
        current_directory = os.path.dirname(__file__)
        filenames = [
            os.path.join(current_directory, 'example1.txt'),
            os.path.join(current_directory, 'example2.txt'),
            os.path.join(current_directory, 'input.txt'),
        ]
        for filename in filenames:
            motions = read_motions_from_file(filename)
            self.assertIsInstance(motions, list)
            direction, steps = motions[0]
            self.assertIsInstance(direction, Direction)
            self.assertIsInstance(steps, int)


    def test_get_field_dimentions(self):
        cases = [
            ([[Mark.EMPTY] * 1] * 1, (1, 1)),
            ([[Mark.EMPTY] * 2] * 1, (1, 2)),
            ([[Mark.EMPTY] * 1] * 2, (2, 1)),
            ([[Mark.EMPTY] * 3] * 5, (5, 3)),
            ([[Mark.EMPTY] * 1] * 100, (100, 1)),
        ]
        for field, expected_dimentions in cases:
            self.assertEqual(get_field_dimentions(field), expected_dimentions)


    def test_expand_field(self):
        initial_field:Field = [[Mark.EMPTY] * 3] * 3
        cases = [
            (initial_field, Direction.LEFT, 2, (3, 5)),
            (initial_field, Direction.RIGHT, 3, (3, 6)),
            (initial_field, Direction.UP, 4, (7, 3)),
            (initial_field, Direction.DOWN, 5, (8, 3)),
        ]
        for field, direction, steps, expected_dimentions in cases:
            expanded_field = expand_field(field, direction, steps)
            expanded_height, _ = get_field_dimentions(expanded_field)
            expected_height, expected_width = expected_dimentions
            self.assertEqual(expanded_height, expected_height)
            for row in expanded_field:
                self.assertEqual(len(row), expected_width)


    def test_move_rope(self):
        for params, expected_result in test_data_for_move_rope:
            self.assertEqual(move_rope(*params), expected_result)


if __name__ == '__main__':
    unittest.main()
