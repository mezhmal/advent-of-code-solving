import os

rucksacks = []
input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        rucksacks.append(line.strip())

priority = lambda item : ord(item) - ord('A') + 27 if item.isupper() else ord(item) - ord('a') + 1

# solution for part 1

priorities = []
for items in rucksacks:
    half_items_length = len(items) // 2
    first_compartment, second_compartment = items[:half_items_length], items[half_items_length:]
    intersection_item = next(iter(set(first_compartment).intersection(second_compartment)))
    priorities.append(priority(intersection_item))

print(f"Sum of the priorities for rucksacks: {sum(priorities)}")

# solution for part 2

priorities = []
for i in range(len(rucksacks) // 3):
    slice_from, slice_to = i * 3, i * 3 + 3
    first, second, third = tuple(rucksacks[slice_from:slice_to])
    intersection_item = next(iter(set(first).intersection(second, third)))
    priorities.append(priority(intersection_item))

print(f"Sum of the priorities for three-Elf groups: {sum(priorities)}")
