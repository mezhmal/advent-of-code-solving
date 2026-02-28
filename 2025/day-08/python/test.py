import unittest
from data import readFile
from solution import part1, part2

class TestPart1(unittest.TestCase):
  def test_example(self):
    answer = 40
    data = readFile('example.txt')
    limit = 10
    self.assertEqual(part1(data, limit), answer)

  def test_input(self):
    answer = 84968
    data = readFile('input.txt')
    limit = 1000
    self.assertEqual(part1(data, limit), answer)


class TestPart2(unittest.TestCase):
  @unittest.SkipTest
  def test_example(self):
    answer = 25272
    data = readFile('example.txt')
    self.assertEqual(part2(data), answer)

  @unittest.SkipTest
  def test_input(self):
    answer = 15811946526915
    data = readFile('input.txt')
    self.assertEqual(part2(data), answer)

if __name__ == '__main__':
    unittest.main()
