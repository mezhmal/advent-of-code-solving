def part1(data):
  position = 50
  accumulator = 0

  for rotation in data:
    direction = direction = 1 if rotation[0] == 'R' else -1
    seek = int(rotation[1:]) * direction

    position += seek
    position %= 100

    if (position == 0):
      accumulator += 1

  return accumulator

def part2(data):
  position = 50
  accumulator = 0

  for rotation in data:
    direction = 1 if rotation[0] == 'R' else -1
    seek = int(rotation[1:]) * direction

    next_position = position + seek
    accumulator += abs(next_position) // 100
    if position > 0 and next_position <= 0:
      accumulator += 1

    position = next_position % 100

  return accumulator
