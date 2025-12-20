def part1(data:list[str]) -> int:
  accumulator = 0
  first_line, *lines = [line.strip() for line in data]
  beams:list[int] = [first_line.index('S')]
  splitter = '^'
  for line in lines:
    next_line_beams:list[int] = []
    for beam in beams:
      if line[beam] == splitter:
        accumulator += 1
        next_line_beams.append(beam-1)
        next_line_beams.append(beam+1)
      else:
        next_line_beams.append(beam)
    beams = set(next_line_beams)
  return accumulator

def part2(data:list[str]) -> int:
  first_line, *lines = [line.strip() for line in data]
  first_beam_position = first_line.index('S')
  beams:list[int] = [first_beam_position]
  line_length = len(first_line)
  timelines:list[int] = [0 for i in range(0, line_length)]
  timelines[first_beam_position] = 1
  splitter = '^'
  for line in lines:
    next_line_beams:list[int] = []
    for beam in beams:
      if line[beam] == splitter:
        next_line_beams.append(beam-1)
        next_line_beams.append(beam+1)
        timelines[beam-1] += timelines[beam]
        timelines[beam+1] += timelines[beam]
        timelines[beam] = 0
      else:
        next_line_beams.append(beam)
    beams = set(next_line_beams)

  return sum(timelines)
