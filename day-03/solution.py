import os

intersection_items = []
input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        stripped_line = line.strip()
        half_length = len(stripped_line) // 2
        first_compartment = stripped_line[:half_length]
        second_compartment = stripped_line[half_length:]
        intersection_item = next(iter(set(first_compartment).intersection(second_compartment)))
        intersection_items.append(intersection_item)

priorities = [ord(item) - 38 if item.isupper() else ord(item) - 96 for item in intersection_items]
print(f"Sum of the priorities: {sum(priorities)}")
