def part1(data:list[str]) -> int:
  accumulator = 0
  data = [item.strip() for item in data]
  separator_position = data.index('')
  ranges:list[str, str] = [item.split('-') for item in data[:separator_position]]
  ranges:list[tuple[int, int]] = [(int(pair[0]), int(pair[1])) for pair in ranges]

  for id in [int(id) for id in data[separator_position+1:]]:
    for start, stop in ranges:
      if id >= start and id <= stop:
        accumulator += 1
        break

  return accumulator

def merge_overlap_ranges(ranges:list[tuple[int, int]]) -> list[tuple[int, int]]:
  ranges.sort()
  merged_ranges:list[tuple[int, int]] = []
  cur_start, cur_stop = ranges[0]
  for start, stop in ranges[1:]:
    if start <= cur_stop+1:
      cur_stop = max(cur_stop, stop)
    else:
      merged_ranges.append((cur_start, cur_stop))
      cur_start, cur_stop = start, stop
  merged_ranges.append((cur_start, cur_stop))

  return merged_ranges

def part2(data:list[str]) -> int:
  data = [item.strip() for item in data]
  separator_position = data.index('')
  ranges:list[str, str] = [item.split('-') for item in data[:separator_position]]
  ranges:list[tuple[int, int]] = [(int(pair[0]), int(pair[1])) for pair in ranges]
  merged_ranges = merge_overlap_ranges(ranges)

  return sum(end - start + 1 for start, end in merged_ranges)
