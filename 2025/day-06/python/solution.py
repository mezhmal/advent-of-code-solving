import math

def part1(data:list[str]) -> int:
  accumulator = 0
  *numbers, operations = [line.split() for line in data]
  for j in range(len(operations)):
    values:list[int] = [int(numbers[i][j]) for i in range(len(numbers))]
    if operations[j] == '+':
      accumulator += sum(values)
    else:
      accumulator += math.prod(values)

  return accumulator

def part2(data:list[str]) -> int:
  accumulator = 0
  *numbers, operations = data
  numbers_max_length = max([len(line) for line in numbers])
  # align operations to the longest line of numbers
  operations = f'{operations.strip():<{numbers_max_length}}'
  for k in range(len(operations)):
    # seek to next operation
    if operations[k] == ' ':
      continue

    # measure the length of the column
    column_length = 1
    while k+column_length < len(operations) and operations[k+column_length] == ' ':
      column_length += 1
    column_length -= 1 # gap between columns

    numbers_in_column:list[str] = [numbers[i][k:k+column_length][::-1] for i in range(len(numbers))]
    values:list[int] = []
    for i in range(column_length)[::-1]:
      column_slice:list[str] = [value[i] for value in numbers_in_column]
      values.append(int(''.join(column_slice)))

    if operations[k] == '+':
      accumulator += sum(values)
    else:
      accumulator += math.prod(values)

  return accumulator
