from copy import deepcopy
from solution import *


def get_new_field(height, width):
    field = []
    for _ in range(height):
        field += [[empty_mark] * width]
    return field


test_data_for_move = []

# case 1: from right edge move 2 steps to left edge, initially head covers tail

initial_position = (1,2)
direction = Direction.LEFT
steps = 2

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = deepcopy(initial_field)
mark(expected_field, (1,1))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (1,0), (1,1))
    )
]

# case 2: from center move 1 step to left edge, initially head covers tail

initial_position = (1,1)
direction = Direction.LEFT
steps = 1

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = deepcopy(initial_field)

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (1,0), (1,1))
    )
]

# case 3: from center move 2 steps to out of left edge, initially head covers tail

initial_position = (1,1)
direction = Direction.LEFT
steps = 2

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 1)
mark(expected_field, (1,1))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (1,0), (1,1))
    )
]

# case 4: from left edge move 5 steps to out of left edge, initially head covers tail

initial_position = (1,0)
direction = Direction.LEFT
steps = 5

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 5)
mark(expected_field, (1,1))
mark(expected_field, (1,2))
mark(expected_field, (1,3))
mark(expected_field, (1,4))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (1,0), (1,1))
    )
]

# case 5: from left edge move 2 steps to right edge, initially head covers tail

initial_position = (1,0)
direction = Direction.RIGHT
steps = 2

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = deepcopy(initial_field)
mark(expected_field, (1,1))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (1,2), (1,1))
    )
]

# case 6: from center move 1 step to right edge, initially head covers tail

initial_position = (1,1)
direction = Direction.RIGHT
steps = 1

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = deepcopy(initial_field)

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (1,2), (1,1))
    )
]

# case 7: from center move 2 steps to out of right edge, initially head covers tail

initial_position = (1,1)
direction = Direction.RIGHT
steps = 2

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 1)
mark(expected_field, (1,2))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (1,3), (1,2))
    )
]

# case 8: from right edge move 5 steps to out of right edge, initially head covers tail

initial_position = (1,2)
direction = Direction.RIGHT
steps = 5

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 5)
mark(expected_field, (1,3))
mark(expected_field, (1,4))
mark(expected_field, (1,5))
mark(expected_field, (1,6))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (1,7), (1,6))
    )
]

# case 9: from bottom edge move 2 steps to up at top edge, initially head covers tail

initial_position = (2,1)
direction = Direction.UP
steps = 2

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = deepcopy(initial_field)
mark(expected_field, (1,1))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (0,1), (1,1))
    )
]

# case 10: from center move 1 step to up at top, initially head covers tail

initial_position = (1,1)
direction = Direction.UP
steps = 1

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = deepcopy(initial_field)

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (0,1), (1,1))
    )
]

# case 11: from center move 2 steps to up out of top edge, initially head covers tail

initial_position = (1,1)
direction = Direction.UP
steps = 2

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 1)
mark(expected_field, (1,1))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (0,1), (1,1))
    )
]

# case 12: from top edge move 5 steps to up out of top edge, initially head covers tail

initial_position = (0,1)
direction = Direction.UP
steps = 5

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 5)
mark(expected_field, (1,1))
mark(expected_field, (2,1))
mark(expected_field, (3,1))
mark(expected_field, (4,1))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (0,1), (1,1))
    )
]

# case 13: from top edge move 2 steps to bottom edge, initially head covers tail

initial_position = (0,1)
direction = Direction.DOWN
steps = 2

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = deepcopy(initial_field)
mark(expected_field, (1,1))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (2,1), (1,1))
    )
]

# case 14: from center move 1 step to down at bottom edge, initially head covers tail

initial_position = (1,1)
direction = Direction.DOWN
steps = 1

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = deepcopy(initial_field)

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (2,1), (1,1))
    )
]

# case 15: from center move 2 steps to down out of bottom edge, initially head covers tail

initial_position = (1,1)
direction = Direction.DOWN
steps = 2

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 1)
mark(expected_field, (2,1))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (3,1), (2,1))
    )
]

# case 16: from bottom edge move 5 steps to down out of bottom edge, initially head covers tail

initial_position = (2,1)
direction = Direction.DOWN
steps = 5

initial_field = get_new_field(3, 3)
mark(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 5)
mark(expected_field, (3,1))
mark(expected_field, (4,1))
mark(expected_field, (5,1))
mark(expected_field, (6,1))

test_data_for_move += [
    (
        (initial_field, initial_position, initial_position, direction, steps), 
        (expected_field, (7,1), (6,1))
    )
]

