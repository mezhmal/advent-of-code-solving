import math
import os
import time
from typing import TypedDict


Monkey = TypedDict('Monkey', {
    'i': int,
    'items': list[int],
    'operation': int,
    'test': TypedDict('test', {
        'divisible_by': int,
        'if_true': int,
        'if_false': int
    }),
    'inspected_items': int
})

Notes = list[Monkey]


def get_empty_monkey() -> Monkey:
    return {
        'i': 0,
        'items': [],
        'operation': 0,
        'test': {
            'divisible_by': 0,
            'if_true': 0,
            'if_false': 0
        },
        'inspected_items': 0,
    }


def read_notes_from_file(filename:str) -> Notes:
    notes:Notes = []
    monkey = get_empty_monkey()

    with open(filename) as f:
        for line in f.readlines():
            stripped_line = line.strip()
            if stripped_line.startswith('Monkey'):
                monkey = get_empty_monkey()
                monkey['i'] = len(notes)
            elif stripped_line.startswith('Starting items'):
                _, items = stripped_line.split(': ')
                monkey['items'] = [int(item) for item in items.split(', ')]
            elif stripped_line.startswith('Operation'):
                _, operation = stripped_line.split(': ')
                monkey['operation'] = operation
            elif stripped_line.startswith('Test'):
                _, divisible_by = stripped_line.split(': divisible by ')
                monkey['test']['divisible_by'] = int(divisible_by)
            elif stripped_line.startswith('If true'):
                _, to_monkey = stripped_line.split(': throw to monkey ')
                monkey['test']['if_true'] = int(to_monkey)
            elif stripped_line.startswith('If false'):
                _, to_monkey = stripped_line.split(': throw to monkey ')
                monkey['test']['if_false'] = int(to_monkey)
            else:
                notes.append(monkey)

    return notes


def get_new_worry_level(old:int, operation:str) -> int:
    new = 0
    operator, value = operation.split(' ')[-2:]
    value = old if value == 'old' else int(value)
    if operator == '+':
        new = old + value
    if operator == '*':
        new = old * value

    return math.floor(new / 3)


def play_round(notes:Notes) -> Notes:
    for monkey in notes:
        for item in monkey['items']:
            worry_level = get_new_worry_level(item, monkey['operation'])
            to_monkey = monkey['test']['if_true'] if worry_level % monkey['test']['divisible_by'] == 0 else monkey['test']['if_false']
            notes[to_monkey]['items'].append(worry_level)

        monkey['inspected_items'] += len(monkey['items'])
        monkey['items'] = []

    return notes


def main():
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    notes = read_notes_from_file(os.path.join(current_directory, input_filename))
    for i in range(20):
        notes = play_round(notes)

    max_times = sorted([monkey['inspected_items'] for monkey in notes])[-2:]
    print(f"(part 1) Level of monkey business: {max_times[0] * max_times[1]}")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
