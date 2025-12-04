import unittest
from data import readFile
from solution import part1, part2

class TestPart1(unittest.TestCase):
  def test_example(self):
    answer = 357
    data = readFile('example.txt')
    self.assertEqual(part1(data), answer)

  def test_input(self):
    answer = 17155
    data = readFile('input.txt')
    self.assertEqual(part1(data), answer)


class TestPart2(unittest.TestCase):
  def test_example(self):
    answer = 3121910778619
    data = readFile('example.txt')
    self.assertEqual(part2(data), answer)

  def test_input(self):
    answer = 169685670469164
    data = readFile('input.txt')
    self.assertEqual(part2(data), answer)

if __name__ == '__main__':
    unittest.main()
