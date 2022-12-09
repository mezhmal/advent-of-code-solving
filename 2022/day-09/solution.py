import os
import time
from enum import Enum


class Direction(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'


undefined_position = '◻︎'
visited_position = '◼︎'


def read_motions_from_file(filename:str) -> list[tuple[str,int]]:
    motions = []
    with open(filename) as f:
        for line in f.readlines():
            direction, steps = line.strip().split(' ')
            motions.append((Direction(direction), int(steps)))
    return motions


def print_field(field:list[list[str]]) -> None:
    for row in field:
        print(' '.join(row))


def get_field_dimentions(field:list[list[str]]) -> tuple[int,int]:
    field_height = len(field)
    field_width = len(field[0])
    return (field_height, field_width)


def expand_field(field:list[list[str]], direction:Direction, steps:int) -> list[list[str]]:
    _, field_width = get_field_dimentions(field)
    match direction:
        case Direction.LEFT:
            return [[undefined_position] * steps + row for row in field]
        case Direction.RIGHT:
            return [row + [undefined_position] * steps for row in field]
        case Direction.UP:
            result = []
            for i in range(steps):
                result +=  [[undefined_position] * field_width]
            return result + field
        case Direction.DOWN:
            for i in range(steps):
                field += [[undefined_position] * field_width]
            return field


def move(*params:tuple) -> tuple:
    field, head_position, tail_position, direction, steps = params
    field_height, field_width = get_field_dimentions(field)
    head_i, head_j = head_position
    tail_i, tail_j = tail_position
    match direction:
        case Direction.RIGHT:
            steps_out_of_boundary = head_j + steps - (field_width - 1)
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)

            print('r', head_j, steps, range(head_j, steps))

            for _ in range(steps):
                head_j += 1

        case Direction.LEFT:
            steps_out_of_boundary = (head_j - steps) * -1
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)
                head_j += steps_out_of_boundary
                tail_j += steps_out_of_boundary

            for _ in range(steps):
                head_j -= 1

        case Direction.UP:
            steps_out_of_boundary = (head_i - steps) * -1
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)
                head_i += steps_out_of_boundary
                tail_i += steps_out_of_boundary

            for _ in range(steps):
                head_i -= 1

        case Direction.DOWN:
            steps_out_of_boundary = head_i + steps - (field_height - 1)
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)

            for _ in range(steps):
                head_i += 1

    field[head_i][head_j] = visited_position
    return field, (head_i, head_j), (tail_i, tail_j)


def main():
    input_filename = 'example.txt'
    current_directory = os.path.dirname(__file__)
    motions = read_motions_from_file(os.path.join(current_directory, input_filename))
    field = [[visited_position]]
    head_position, tail_position = (0, 0), (0, 0)
    print_field(field)
    print(head_position)
    for direction, steps in motions:
        print()
        field, head_position, tail_position = move(field, head_position, tail_position, direction, steps)
        print(direction, steps, head_position)
        print_field(field)
        print()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
