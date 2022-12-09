import os
import time
from enum import Enum


class Direction(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'


empty_mark = '◻︎'
visited_mark = '◼︎'


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
            return [[empty_mark] * steps + row for row in field]
        case Direction.RIGHT:
            return [row + [empty_mark] * steps for row in field]
        case Direction.UP:
            result = []
            for i in range(steps):
                result +=  [[empty_mark] * field_width]
            return result + field
        case Direction.DOWN:
            for i in range(steps):
                field += [[empty_mark] * field_width]
            return field
    

def mark(field:list[list[str]], position:tuple[int,int]) -> None:
    i, j = position
    field[i][j] = visited_mark


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
            for _ in range(steps):
                head_j += 1
                if head_j - tail_j > 1:
                    tail_i = head_i
                    tail_j = head_j - 1
                    mark(field, (tail_i, tail_j))

        case Direction.LEFT:
            steps_out_of_boundary = (head_j - steps) * -1
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)
                head_j += steps_out_of_boundary
                tail_j += steps_out_of_boundary
            for _ in range(steps):
                head_j -= 1
                if tail_j - head_j > 1:
                    tail_i = head_i
                    tail_j = head_j + 1
                    mark(field, (tail_i, tail_j))

        case Direction.UP:
            steps_out_of_boundary = (head_i - steps) * -1
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)
                head_i += steps_out_of_boundary
                tail_i += steps_out_of_boundary
            for _ in range(steps):
                head_i -= 1
                if tail_i - head_i > 1:
                    tail_i = head_i + 1
                    tail_j = head_j
                    mark(field, (tail_i, tail_j))

        case Direction.DOWN:
            steps_out_of_boundary = head_i + steps - (field_height - 1)
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)
            for _ in range(steps):
                head_i += 1
                if head_i - tail_i > 1:
                    tail_i = head_i - 1
                    tail_j = head_j
                    mark(field, (tail_i, tail_j))

    return field, (head_i, head_j), (tail_i, tail_j)


def main():
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    motions = read_motions_from_file(os.path.join(current_directory, input_filename))
    field = [[visited_mark]]
    head_position, tail_position = (0, 0), (0, 0)

    # solution for part 1

    for direction, steps in motions:
        field, head_position, tail_position = move(field, head_position, tail_position, direction, steps)
    result = sum([sum([1 for position in row if position == visited_mark]) for row in field])
    print(f"(part 1) Tail visited {result} positions")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
