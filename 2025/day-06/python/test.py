import unittest
from data import readFile
from solution import part1, part2

class TestPart1(unittest.TestCase):
  def test_example(self):
    answer = 4277556
    data = readFile('example.txt')
    self.assertEqual(part1(data), answer)

  def test_input(self):
    answer = 5060053676136
    data = readFile('input.txt')
    self.assertEqual(part1(data), answer)


class TestPart2(unittest.TestCase):
  def test_example(self):
    answer = 3263827
    data = readFile('example.txt')
    self.assertEqual(part2(data), answer)

  def test_input(self):
    answer = 9695042567249
    data = readFile('input.txt')
    self.assertEqual(part2(data), answer)

if __name__ == '__main__':
    unittest.main()
