from data import readFile
from solution import part1, part2

data = readFile('example.txt')
limit = 1000
# print('answer to the first part:', part1(data, limit))
print('answer to the second part:', part2(data))
