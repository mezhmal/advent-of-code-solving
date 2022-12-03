import os

commands = []
input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        direction, units = line.strip().split(' ')
        commands.append({
            'direction': direction,
            'units': int(units)
        })

# solution for part 1

horizontal_position = sum([command.get('units', 0) for command in commands if command.get('direction') == 'forward'])
summary_moves_to_down = sum([command.get('units', 0) for command in commands if command.get('direction') == 'down'])
summary_moves_to_up = sum([command.get('units', 0) for command in commands if command.get('direction') == 'up'])
depth = summary_moves_to_down - summary_moves_to_up

print(f"horizontal_position * depth = {horizontal_position * depth}")
