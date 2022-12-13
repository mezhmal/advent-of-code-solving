import math
import os
import time
from typing import TypedDict, Optional


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


def get_new_worry_level(worry_level:int, operation:str, lcm:Optional[int]=None) -> int:
    operator, value = operation.split(' ')[-2:]
    value = worry_level if value == 'old' else int(value)
    if operator == '+':
        worry_level += value
    if operator == '*':
        worry_level *= value

    if lcm:
        worry_level %= lcm
    else:
        worry_level //= 3

    return worry_level


def play_round(notes:Notes, lcm:Optional[int]=None) -> Notes:
    for monkey in notes:
        for item in monkey['items']:
            worry_level = get_new_worry_level(item, monkey['operation'], lcm)
            to_monkey = monkey['test']['if_true'] if worry_level % monkey['test']['divisible_by'] == 0 else monkey['test']['if_false']
            notes[to_monkey]['items'].append(worry_level)

        monkey['inspected_items'] += len(monkey['items'])
        monkey['items'] = []

    return notes


def get_level_of_monkey_business(notes:Notes) -> int:
    most_inspected_items = sorted([monkey['inspected_items'] for monkey in notes])[-2:]
    return most_inspected_items[0] * most_inspected_items[1]


def main():
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)

    # solution for part 1

    notes = read_notes_from_file(os.path.join(current_directory, input_filename))
    for _ in range(20):
        notes = play_round(notes)

    print(f"(part 1) Level of monkey business after 20 rounds: {get_level_of_monkey_business(notes)}")

    # solution for part 2

    """
    The main difficulity of part 2 is a need to find another way to keep worry levels manageable.
    Because for many round worry level of items increased to huge values.
    So we can get least common multiple (lcm) (see more information on https://en.wikipedia.org/wiki/Least_common_multiple)
    of divisors from monkey tests and use it for reducing worry level after operations.
    """

    lcm = math.lcm(*[monkey['test']['divisible_by'] for monkey in notes])
    notes = read_notes_from_file(os.path.join(current_directory, input_filename))
    for _ in range(10 * 1000):
        notes = play_round(notes, lcm)

    print(f"(part 2) Level of monkey business after 10 000 rounds: {get_level_of_monkey_business(notes)}")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
