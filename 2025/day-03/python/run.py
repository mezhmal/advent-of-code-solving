from data import readFile
from solution import part1, part2

data = readFile('input.txt')
print('answer to the first part:', part1(data))
print('answer to the second part:', part2(data))
