import os


field = []
input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        field.append(list(line.strip()))

steps_limit = 1000

field_width = len(field[0])
field_height = len(field)

empty_cell = '.'
east_facing_herd = '>'
south_facing_herd = 'v'


def can_move_to_east(_i, _j):
    if field[_i][_j] == east_facing_herd:
        idx_east_next = 0 if _j + 1 >= field_width else _j + 1
        return field[_i][idx_east_next] == empty_cell

    return False


def can_move_to_south(_i, _j):
    if field[_i][_j] == south_facing_herd:
        idx_south_next = 0 if _i + 1 >= field_height else _i + 1
        return field[idx_south_next][_j] == empty_cell

    return False


def move_to_east(_i, _j):
    idx_east = 0 if _j + 1 >= field_width else _j + 1
    field[_i][_j] = empty_cell
    field[_i][idx_east] = east_facing_herd


def move_to_south(_i, _j):
    idx_south = 0 if _i + 1 >= field_height else _i + 1
    field[_i][_j] = empty_cell
    field[idx_south][_j] = south_facing_herd


print('Initial state')
for row in field:
    print(''.join(row))

for step in range(1, steps_limit):
    print()
    print(f"Step {step}")

    cucumbers_moved = False

    movable_cucumbers = [[can_move_to_east(i, j) for j in range(field_width)] for i in range(field_height)]
    for i in range(field_height):
        for j in range(field_width):
            if movable_cucumbers[i][j]:
                move_to_east(i, j)
                cucumbers_moved = True

    movable_cucumbers = [[can_move_to_south(i, j) for j in range(field_width)] for i in range(field_height)]
    for i in range(field_height):
        for j in range(field_width):
            if movable_cucumbers[i][j]:
                move_to_south(i, j)
                cucumbers_moved = True

    print(f"Cucumbers{'' if cucumbers_moved else ' not'} moved")

    for row in field:
        print(''.join(row))

    if not cucumbers_moved:
        break
