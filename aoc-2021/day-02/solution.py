import os

commands = []
up = 'up'
down = 'down'
forward = 'forward'

input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        direction, units = line.strip().split(' ')
        commands.append((direction, int(units)))

# solution for part 1

horizontal_position = sum([units for direction, units in commands if direction == forward])
summary_moves_to_down = sum([units for direction, units in commands if direction == down])
summary_moves_to_up = sum([units for direction, units in commands if direction == up])
depth = summary_moves_to_down - summary_moves_to_up

print(f"horizontal_position * depth = {horizontal_position * depth}")

# solution for part 2

aim = 0
depth = 0
horizontal_position = 0
for direction, units in commands:
    if direction == down:
        aim += units
    elif direction == up:
        aim -= units
    elif direction == forward:
        horizontal_position += units
        depth += aim * units

print(f"(new interpretation of the commands) horizontal_position * depth = {horizontal_position * depth}")
