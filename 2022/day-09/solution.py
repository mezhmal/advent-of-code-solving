import os
import time
from enum import Enum


class Direction(Enum):
    LEFT  = 'L'
    RIGHT = 'R'
    UP    = 'U'
    DOWN  = 'D'


class Mark(Enum):
    EMPTY   = '.'
    VISITED = '@'

Field = list[list[Mark]]
Motion = tuple[Direction, int]
Motions = list[Motion]
Position = tuple[int, int]
Rope = list[Position]


def read_motions_from_file(filename:str) -> Motions:
    motions:Motions = []
    with open(filename) as f:
        for line in f.readlines():
            direction, steps = line.strip().split(' ')
            motion:Motion = (Direction(direction), int(steps))
            motions.append(motion)
    return motions


def print_field(field:Field) -> None:
    for row in field:
        print(' '.join([position.value for position in row]))


def print_field_and_rope(field:Field, rope:Rope) -> None:
    field_height, field_width = get_field_dimentions(field)
    for i in range(field_height):
        line = []
        for j in range(field_width):
            cell = field[i][j].value
            for knot_i in reversed(range(len(rope))):
                if (i, j) == rope[knot_i]:
                    cell = str(knot_i)
            line.append(cell)
        print(' '.join(line))


def get_field_dimentions(field:Field) -> tuple[int,int]:
    field_height = len(field)
    field_width = len(field[0])
    return (field_height, field_width)


def expand_field(field:Field, direction:Direction, steps:int) -> Field:
    _, field_width = get_field_dimentions(field)
    match direction:
        case Direction.LEFT:
            return [[Mark.EMPTY] * steps + row for row in field]
        case Direction.RIGHT:
            return [row + [Mark.EMPTY] * steps for row in field]
        case Direction.UP:
            result = []
            for i in range(steps):
                result +=  [[Mark.EMPTY] * field_width]
            return result + field
        case Direction.DOWN:
            for i in range(steps):
                field += [[Mark.EMPTY] * field_width]
            return field
    

def mark_visited(field:Field, position:Position) -> None:
    i, j = position
    field[i][j] = Mark.VISITED


def pull_tail(field:Field, rope:Rope, target:Position) -> tuple[Field, Rope]:
    tail_i, tail_j = rope[-1]
    target_i, target_j = target
    steps = max(abs(target_i - tail_i), abs(target_j - tail_j))
    for _ in range(steps):
        if tail_i < target_i:
            tail_i += 1
        if tail_i > target_i:
            tail_i -= 1
        if tail_j < target_j:
            tail_j += 1
        if tail_j > target_j:
            tail_j -= 1

        # mark_visited(field, (tail_i, tail_j))

    rope[-1] = target
    mark_visited(field, target)

    # print()
    # print_field_and_rope(field, rope)
    # print()

    return field, rope


def pull_rope_knots(field:Field, rope:Rope) -> tuple[Field,Rope]:
    rope_length = len(rope)
    tail_idx = rope_length - 1
    for i in range(1, rope_length):
        prev_i, prev_j = rope[i-1]
        curr_i, curr_j = rope[i]

        if curr_j - prev_j > 1:
            # previous node move far away to left
            curr_i = prev_i
            curr_j = prev_j + 1
        elif prev_j - curr_j > 1:
            # previous node move far away to right
            curr_i = prev_i
            curr_j = prev_j - 1
        elif curr_i - prev_i > 1:
            # previous node move far away to up
            curr_i = prev_i + 1
            curr_j = prev_j
        elif prev_i - curr_i > 1:
            # previous node move far away to down
            curr_i = prev_i - 1
            curr_j = prev_j

        if rope[i] != (curr_i, curr_j):
            if i == tail_idx:
                pull_tail(field, rope, (curr_i, curr_j))
            else:
                rope[i] = (curr_i, curr_j)

    return field, rope


def move_rope(field:Field, rope:Rope, direction:Direction, steps:int) -> tuple[Field,Rope]:
    field_height, field_width = get_field_dimentions(field)
    head_i, head_j = rope[0]

    # print_field_and_rope(field, rope)
    # print()

    # expand field if required
    match direction:
        case Direction.RIGHT:
            steps_out_of_boundary = head_j + steps - (field_width - 1)
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)

        case Direction.LEFT:
            steps_out_of_boundary = (head_j - steps) * -1
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)
                for i in range(len(rope)):
                    knot_i, knot_j = rope[i]
                    rope[i] = (knot_i, knot_j + steps_out_of_boundary)

        case Direction.UP:
            steps_out_of_boundary = (head_i - steps) * -1
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)
                for i in range(len(rope)):
                    knot_i, knot_j = rope[i]
                    rope[i] = (knot_i + steps_out_of_boundary, knot_j)

        case Direction.DOWN:
            steps_out_of_boundary = head_i + steps - (field_height - 1)
            if steps_out_of_boundary > 0:
                field = expand_field(field, direction, steps_out_of_boundary)

    # move rope step by step
    for i in range(steps):

        # print()
        # print('step', i + 1, 'to', direction.value)

        head_i, head_j = rope[0]
        match direction:
            case Direction.LEFT:
                head_j -= 1
            case Direction.RIGHT:
                head_j += 1
            case Direction.UP:
                head_i -= 1
            case Direction.DOWN:
                head_i += 1
        rope[0] = (head_i, head_j)
        field, rope = pull_rope_knots(field, rope)

        # print_field_and_rope(field, rope)

    return field, rope


def main():
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    motions = read_motions_from_file(os.path.join(current_directory, input_filename))

    # solution for part 1

    field = [[Mark.VISITED]]
    rope:Rope = [(0, 0)] * 2
    for direction, steps in motions:
        field, rope = move_rope(field, rope, direction, steps)
    result = sum([sum([1 for position in row if position == Mark.VISITED]) for row in field])
    print(f"(part 1) Tail visited {result} positions")

    # solution for part 2

    motion_number = 0
    field = [[Mark.VISITED]]
    rope:Rope = [(0, 0)] * 10
    for direction, steps in motions:
        motion_number += 1

        # print()
        # print('motion', motion_number, ' | move', steps, 'steps' if steps > 1 else 'step', 'to', direction.value)

        field, rope = move_rope(field, rope, direction, steps)

        # print_field_and_rope(field, rope)

    result = sum([sum([1 for position in row if position == Mark.VISITED]) for row in field])
    print(f"(part 2) Tail visited {result} positions")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
