from copy import deepcopy
from solution import *


def get_new_field(height:int, width:int) -> Field:
    field:Field = []
    for _ in range(height):
        field += [[Mark.EMPTY] * width]
    return field


test_data_for_move_rope = []


"""
case 1
rope has 2 knots, head covers tail
from right edge move 2 steps to left edge
"""

direction = Direction.LEFT
steps = 2

initial_position = (1, 2)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = deepcopy(initial_field)
expected_rope = [(1, 0), (1, 1)]
mark_visited(expected_field, (1, 1))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 2
rope has 2 knots, head covers tail
from center move 1 step to left edge
"""

direction = Direction.LEFT
steps = 1

initial_position = (1, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = deepcopy(initial_field)
expected_rope = [(1, 0), (1, 1)]

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 3
rope has 2 knots, head covers tail
from center move 2 steps to out of left edge
"""

direction = Direction.LEFT
steps = 2

initial_position = (1, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 1)
expected_rope = [(1, 0), (1, 1)]
mark_visited(expected_field, (1, 1))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 4
rope has 2 knots, head covers tail
from left edge move 5 steps to out of left edge
"""

direction = Direction.LEFT
steps = 5

initial_position = (1, 0)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 5)
expected_rope = [(1, 0), (1, 1)]
mark_visited(expected_field, (1, 1))
mark_visited(expected_field, (1, 2))
mark_visited(expected_field, (1, 3))
mark_visited(expected_field, (1, 4))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 5
rope has 2 knots, head covers tail
from left edge move 2 steps to right edge
"""

direction = Direction.RIGHT
steps = 2

initial_position = (1 ,0)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = deepcopy(initial_field)
expected_rope = [(1, 2), (1, 1)]
mark_visited(expected_field, (1, 1))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 6
rope has 2 knots, head covers tail
from center move 1 step to right edge
"""

direction = Direction.RIGHT
steps = 1

initial_position = (1, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = deepcopy(initial_field)
expected_rope = [(1, 2), (1, 1)]

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 7
rope has 2 knots, head covers tail
from center move 2 steps to out of right edge
"""

direction = Direction.RIGHT
steps = 2

initial_position = (1, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 1)
expected_rope = [(1, 3), (1, 2)]
mark_visited(expected_field, (1, 2))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 8
rope has 2 knots, head covers tail
from right edge move 5 steps to out of right edge
"""

direction = Direction.RIGHT
steps = 5

initial_position = (1, 2)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 5)
expected_rope = [(1, 7), (1, 6)]
mark_visited(expected_field, (1, 3))
mark_visited(expected_field, (1, 4))
mark_visited(expected_field, (1, 5))
mark_visited(expected_field, (1, 6))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 9
rope has 2 knots, head covers tail
from bottom edge move 2 steps to up at top edge
"""

direction = Direction.UP
steps = 2

initial_position = (2, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = deepcopy(initial_field)
expected_rope = [(0, 1), (1, 1)]
mark_visited(expected_field, (1, 1))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 10
rope has 2 knots, head covers tail
from center move 1 step to up at top
"""

direction = Direction.UP
steps = 1

initial_position = (1, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = deepcopy(initial_field)
expected_rope = [(0, 1), (1, 1)]

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 11
rope has 2 knots, head covers tail
from center move 2 steps to up out of top edge
"""

direction = Direction.UP
steps = 2

initial_position = (1, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 1)
expected_rope = [(0, 1), (1, 1)]
mark_visited(expected_field, (1, 1))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 12
rope has 2 knots, head covers tail
from top edge move 5 steps to up out of top edge
"""

direction = Direction.UP
steps = 5

initial_position = (0, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 5)
expected_rope = [(0, 1), (1, 1)]
mark_visited(expected_field, (1, 1))
mark_visited(expected_field, (2, 1))
mark_visited(expected_field, (3, 1))
mark_visited(expected_field, (4, 1))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 13
rope has 2 knots, head covers tail
from top edge move 2 steps to bottom edge
"""

direction = Direction.DOWN
steps = 2

initial_position = (0, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = deepcopy(initial_field)
expected_rope = [(2, 1), (1, 1)]
mark_visited(expected_field, (1, 1))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 14
rope has 2 knots, head covers tail
from center move 1 step to down at bottom edge
"""

direction = Direction.DOWN
steps = 1

initial_position = (1, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = deepcopy(initial_field)
expected_rope = [(2, 1), (1, 1)]

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 15
rope has 2 knots, head covers tail
from center move 2 steps to down out of bottom edge
"""

direction = Direction.DOWN
steps = 2

initial_position = (1, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 1)
expected_rope = [(3, 1), (2, 1)]
mark_visited(expected_field, (2, 1))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]


"""
case 16
rope has 2 knots, head covers tail
from bottom edge move 5 steps to down out of bottom edge
"""

direction = Direction.DOWN
steps = 5

initial_position = (2, 1)
initial_rope = [initial_position] * 2
initial_field = get_new_field(3, 3)
mark_visited(initial_field, initial_position)

expected_field = expand_field(deepcopy(initial_field), direction, 5)
expected_rope = [(7, 1), (6, 1)]
mark_visited(expected_field, (3, 1))
mark_visited(expected_field, (4, 1))
mark_visited(expected_field, (5, 1))
mark_visited(expected_field, (6, 1))

test_data_for_move_rope += [( (initial_field, initial_rope, direction, steps), (expected_field, expected_rope) )]
