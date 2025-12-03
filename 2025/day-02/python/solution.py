def part1(data):
  accumulator = 0
  ranges = data[0].strip().split(',')
  ranges = [item.split('-') for item in ranges]
  # exclude ranges with only odd numbers
  ranges = [[int(start), int(stop)] for [start, stop] in ranges if not(len(start) % 2 and len(start) == len(stop))]

  for [start, stop] in ranges:
    for value in range(start, stop+1):
      str_value = str(value)
      value_size = len(str_value)
      length_is_even = value_size % 2 == 0
      left, right = str_value[value_size // 2:], str_value[:value_size // 2]
      if (length_is_even and left == right):
        accumulator += value

  return accumulator

def part2(data):
  accumulator = 0
  ranges = data[0].strip().split(',')
  ranges = [item.split('-') for item in ranges]
  ranges = [[int(start), int(stop)] for [start, stop] in ranges]

  for [start, stop] in ranges:
    for value in range(start, stop+1):
      str_value = str(value)
      value_size = len(str_value)
      for divider in range(2, value_size + 1):
        value_divisible_into_equal_chunks = value_size % divider == 0
        if not value_divisible_into_equal_chunks:
          continue

        chunks = []
        chunk_size = value_size // divider
        for chunk_start in range(0, value_size, chunk_size):
          chunk_stop = chunk_start + chunk_size
          chunks.append(str_value[chunk_start:chunk_stop])

        all_chunks_are_equal = len(set(chunks)) == 1
        if all_chunks_are_equal:
          accumulator += value
          break

  return accumulator
