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
            notes = read_notes_from_file(filename)
            self.assertIsInstance(notes, list)


if __name__ == '__main__':
    unittest.main()
