import os


crates_heap = []
stack_numbers_line = ''
steps = []
input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        data = line.strip()
        if data.startswith('['):
            crates_heap.append(line)
        elif data.startswith('1'):
            stack_numbers_line = line.rstrip()
        elif data.startswith('move'):
            _, size, _, stack_from, _, stack_to = data.split(' ')
            steps.append((int(size), stack_from, stack_to))

# solution for part 1

stacks = {}
stack_numbers = [number for number in stack_numbers_line.split(' ') if number]
for number in stack_numbers:
    index = stack_numbers_line.index(number)
    stacks[number] = []
    for line in reversed(crates_heap):
        if len(line) > index and line[index] != ' ':
            stacks[number].append(line[index])

for size, stack_from, stack_to in steps:
    payload = stacks[stack_from][size*-1:][::-1]
    stacks[stack_from] = stacks[stack_from][:size*-1]
    stacks[stack_to] = stacks[stack_to] + payload

message = ''
for number in stack_numbers:
    last_crate = stacks[number][-1:]
    if last_crate:
        message += last_crate[0]

print(f"message: {message}")
