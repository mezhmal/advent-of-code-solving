import os
import unittest
from solution import *


class TestSolution(unittest.TestCase):

    def test_read_program_from_file(self):
        current_directory = os.path.dirname(__file__)
        filenames = [
            os.path.join(current_directory, 'example.txt'),
            os.path.join(current_directory, 'input.txt'),
        ]
        for filename in filenames:
            program = read_program_from_file(filename)
            self.assertIsInstance(program, list)


    def test_execute_program(self):
        program = [
            'noop',
            'add 3',
            'add -5',
            'noop',
            'noop',
            'add 7',
            'noop',
            'add -4',
            'noop'
        ]
        cases = [
            ([1], 1),
            ([2], 2),
            ([3], 3),
            ([4], 16),
            ([5], 20),
            ([1, 2], 1 + 2),
            ([1, 2, 3], 1 + 2 + 3),
            ([1, 2, 3, 4], 1 + 2 + 3 + 16),
            ([1, 2, 3, 4, 5], 1 + 2 + 3 + 16 + 20),
            ([1, 3, 5], 1 + 3 + 20),
            ([2, 4, 6], 2 + 16 - 6),
            ([3, 6, 9], 3 - 6 - 9),
            ([5, 10, 15], 20 - 60 + 120),
        ]

        for measurement_scale, expected_signal_strenght in cases:
            self.assertEqual(execute_program(program, measurement_scale), expected_signal_strenght)


if __name__ == '__main__':
    unittest.main()
