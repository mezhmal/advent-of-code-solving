import os


commands = []
input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        direction, units = line.strip().split(' ')
        commands.append((direction, int(units)))

# solution for part 1

depth = 0
horizontal_position = 0
for direction, units in commands:
    match direction:
        case 'down':
            depth += units
        case 'up':
            depth -= units
        case 'forward':
            horizontal_position += units

print(f"horizontal_position * depth = {horizontal_position * depth}")

# solution for part 2

aim = 0
depth = 0
horizontal_position = 0
for direction, units in commands:
    match direction:
        case 'down':
            aim += units
        case 'up':
            aim -= units
        case 'forward':
            horizontal_position += units
            depth += aim * units

print(f"(new interpretation of the commands) horizontal_position * depth = {horizontal_position * depth}")
