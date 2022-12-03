import os

rucksacks = []
input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        rucksacks.append(line.strip())


def priority(item):
    return ord(intersection_item) - 38 if intersection_item.isupper() else ord(intersection_item) - 96

# solution for part 1

priorities = []
for items in rucksacks:
    half_items_length = len(items) // 2
    first_compartment = items[:half_items_length]
    second_compartment = items[half_items_length:]
    intersection_item = next(iter(set(first_compartment).intersection(second_compartment)))
    priorities.append(priority(intersection_item))

print(f"Sum of the priorities for rucksacks: {sum(priorities)}")

# solution for part 2

priorities = []
for i in range(len(rucksacks) // 3):
    three_elf_group = rucksacks[i*3:i*3+3]
    intersection_item = next(iter(set(three_elf_group[0]).intersection(three_elf_group[1], three_elf_group[2])))
    priorities.append(priority(intersection_item))

print(f"Sum of the priorities for three-Elf groups: {sum(priorities)}")
