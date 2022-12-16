import os
import unittest
from solution import *


class TestSolution(unittest.TestCase):

    def test_read_map_from_file(self):
        current_directory = os.path.dirname(__file__)
        filenames = [
            os.path.join(current_directory, 'example.txt'),
            os.path.join(current_directory, 'input.txt'),
        ]
        for filename in filenames:
            map = read_map_from_file(filename)
            self.assertIsInstance(map, list)
            self.assertIsInstance(map[0], list)
            self.assertIsInstance(map[0][0], str)


if __name__ == '__main__':
    unittest.main()
