from solution import *

initial_field = [[undefined_position] * 3] * 3

test_data_for_move = [
    (
        (initial_field, (1,2), (1,2), Direction.LEFT, 2), 
        (initial_field, (1,0), (1,2))
    ),
    (
        (initial_field, (1,1), (1,1), Direction.LEFT, 1), 
        (initial_field, (1,0), (1,1))
    ),
    (
        (initial_field, (1,1), (1,1), Direction.LEFT, 2),
        (expand_field(initial_field, Direction.LEFT, 1), (1,0), (1,2))
    ),
    (
        (initial_field, (1,0), (1,0), Direction.LEFT, 10),
        (expand_field(initial_field, Direction.LEFT, 10), (1,0), (1,10))
    ),
    (
        (initial_field, (1,0), (1,0), Direction.RIGHT, 2), 
        (initial_field, (1,2), (1,0))
    ),
    (
        (initial_field, (1,1), (1,1), Direction.RIGHT, 1), 
        (initial_field, (1,2), (1,1))
    ),
    (
        (initial_field, (1,1), (1,1), Direction.RIGHT, 2),
        (expand_field(initial_field, Direction.RIGHT, 1), (1,3), (1,1))
    ),
    (
        (initial_field, (1,2), (1,2), Direction.RIGHT, 10),
        (expand_field(initial_field, Direction.RIGHT, 10), (1,12), (1,2))
    ),
    (
        (initial_field, (2,1), (2,1), Direction.UP, 2), 
        (initial_field, (0,1), (2,1))
    ),
    (
        (initial_field, (1,1), (1,1), Direction.UP, 1), 
        (initial_field, (0,1), (1,1))
    ),
    (
        (initial_field, (1,1), (1,1), Direction.UP, 2),
        (expand_field(initial_field, Direction.UP, 1), (0,1), (2,1))
    ),
    (
        (initial_field, (0,1), (0,1), Direction.UP, 10),
        (expand_field(initial_field, Direction.UP, 10), (0,1), (10,1))
    ),
    (
        (initial_field, (0,1), (0,1), Direction.DOWN, 2), 
        (initial_field, (2,1), (0,1))
    ),
    (
        (initial_field, (1,1), (1,1), Direction.DOWN, 1), 
        (initial_field, (2,1), (1,1))
    ),
    (
        (initial_field, (1,1), (1,1), Direction.DOWN, 2),
        (expand_field(initial_field, Direction.DOWN, 1), (3,1), (1,1))
    ),
    (
        (initial_field, (2,1), (2,1), Direction.DOWN, 10),
        (expand_field(initial_field, Direction.DOWN, 10), (12,1), (2,1))
    ),
]
