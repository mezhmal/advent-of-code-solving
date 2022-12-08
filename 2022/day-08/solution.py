import os
import time
from enum import Enum


class Direction(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'


def read_field_from_file(filename:str) -> list[list[int]]:
    field = []
    with open(filename) as f:
        for line in f.readlines():
            field.append([int(i) for i in list(line.strip())])
    return field


def is_row_visible(row:list[int]) -> bool:
    return row and row[0] > max(row[1:])


def is_tree_visible(field:list[list[int]], position:tuple) -> bool:
    if is_row_visible(get_row(field, position, Direction.LEFT)):
        return True
    if is_row_visible(get_row(field, position, Direction.RIGHT)):
        return True
    if is_row_visible(get_row(field, position, Direction.UP)):
        return True
    if is_row_visible(get_row(field, position, Direction.DOWN)):
        return True
    return False


def get_row(field:list[list[int]], position:tuple, direction:Direction) -> list[int]:
    i, j = position
    match direction:
        case Direction.LEFT:
            return field[i][j::-1]
        case Direction.RIGHT:
            return field[i][j:]
        case Direction.UP:
            return [row[j] for row in field[i::-1]]
        case Direction.DOWN:
            return [row[j] for row in field[i:]]
        case _:
            return []


def get_perimeter_length(field:list[list[int]]) -> int:
    field_height = len(field)
    field_width = len(field[0])
    if field_height == 1:
        return field_width
    if field_width == 1:
        return field_height
    return field_height * 2 + (field_width - 2) * 2


def get_inner_visible_count(field:list[list[int]]) -> int:
    field_height = len(field)
    field_width = len(field[0])
    count = 0
    for i in range(1, field_height-1):
        for j in range(1, field_width-1):
            if is_tree_visible(field, (i, j)):
                count += 1
    return count


def main():
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    field = read_field_from_file(os.path.join(current_directory, input_filename))

    # solution for part 1

    result = get_perimeter_length(field) + get_inner_visible_count(field)
    print(f"(part 1) {result} trees are visible from outside the grid")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    print(f"Done in {stop-start:0.4f} seconds")
