def part1(data):
  accumulator = 0
  for bank in data:
    batteries = [int(battery) for battery in list(bank.strip())]
    first_max_jolt = max(batteries[:-1])
    index = batteries.index(first_max_jolt)
    second_max_jolt = max(batteries[index+1:])
    joltage = int(str(first_max_jolt) + str(second_max_jolt))
    accumulator += joltage

  return accumulator

def part2(data):
  accumulator = 0
  digits = 12
  for bank in data:
    batteries = [int(battery) for battery in list(bank.strip())]
    jolts = []
    for i in range(digits):
      scan_range = batteries[:-digits+i+1] if i < digits-1 else batteries
      max_jolt = max(scan_range)
      jolts.append(max_jolt)
      index = batteries.index(max_jolt)
      batteries = batteries[index+1:]

    joltage = int(''.join(map(str, jolts)))
    accumulator += joltage

  return accumulator
