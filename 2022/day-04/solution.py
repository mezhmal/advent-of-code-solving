import os


assignments = []
input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        assignments.append(line.strip().split(','))

contains_count = 0
for first, second in assignments:
    first_from, first_to = first.split('-')
    second_from, second_to = second.split('-')
    first_contains_second = int(first_from) <= int(second_from) and int(first_to) >= int(second_to)
    second_contains_first = int(second_from) <= int(first_from) and int(second_to) >= int(first_to)
    if first_contains_second or second_contains_first:
        contains_count += 1

print(f"{contains_count} assignment pairs does one range fully contain the other")
