import os
import time
from copy import deepcopy
from enum import Enum


class Direction(Enum):
    LEFT  = '◀︎'
    RIGHT = '▶︎'
    UP    = '▲'
    DOWN  = '▼'


SourceMap = list[list[str]]
ConvertedMap = list[list[int]]
Position = tuple[int, int]
NodeKey = str
Nodes = dict[NodeKey, Position]
Branch = list[tuple[NodeKey, Direction | None]]
Tree = list[Branch]


"""
tree = [
    (branch 0) [
        (node_key, direction to next node | None for last node),
        ('(0, 0)', 'R'),
        ('(0, 1)', None),
    ],
    (branch 1) [
        ('(0, 0)', 'D'),
        ('(1, 0)', None),
    ],
]

on each step we lookup last nodes for each branch
if way will be found and there are no loops, then we clone brance for each found way
then current branch will be deleted 

if node in any branch is end_position, then we stop find process

collect touched nodes for exclude re-lookup nodes and loops in pathes

"""

source_map:SourceMap = []
map:ConvertedMap = []
touched_nodes:Nodes = {}
tree:Tree = []


def read_map_from_file(filename:str) -> SourceMap:
    map:SourceMap = []
    with open(filename) as f:
        for line in f.readlines():
            map.append(list(line.strip()))

    return map


def convert_map(map:SourceMap) -> tuple[ConvertedMap, Position, Position]:
    """
    returns map letters replace by numbers, position for start and position for stop
    """
    start_position:Position
    end_position:Position
    converted_map:ConvertedMap = []
    shift = ord('a')
    for i in range(len(map)):
        converted_row = []
        for j in range(len(map[0])):
            if map[i][j] == 'S':
                start_position = (i, j)
                converted_row.append(ord('a') - shift)
            elif map[i][j] == 'E':
                end_position = (i, j)
                converted_row.append(ord('z') - shift)
            else:
                converted_row.append(ord(map[i][j]) - shift)
        converted_map.append(converted_row)

    return converted_map, start_position, end_position


def setup(start_position:Position) -> None:
    global touched_nodes
    global tree
    touched_nodes = {}
    tree = []
    node_key = get_node_key(start_position)
    touched_nodes[node_key] = start_position
    for neighbor_position, _ in get_neighbors_higher(start_position):
        neighbor_key = get_node_key(neighbor_position)
        touched_nodes[neighbor_key] = neighbor_position
        branch:Branch = [(neighbor_key, None)]
        tree.append(branch)


def get_node_key(node_position:Position) -> NodeKey:
    return str(node_position)


def climb_up(end_position:Position) -> Branch:
    global tree
    max_steps = 1000
    end_position_key = get_node_key(end_position)

    start = time.perf_counter()

    for step in range(max_steps):

        stop = time.perf_counter()

        # print(f"step: {step}; branches: {len(tree)}; {stop-start:0.2f}s")

        for i in range(len(tree)):
            branch = tree[i]
            last_node_key, _ = branch[-1]
            if last_node_key == end_position_key:
                return branch
            
            tree += take_one_step(branch)
            tree[i] = None

        tree = [branch for branch in tree if branch]

        if step in []:
            for b in range(len(tree)):
                print()
                print(f"branch {b}")
                print_path(deepcopy(source_map), tree[b])
                print()

        if not tree:
            print('no more branches')
            return


def take_one_step(branch:Branch) -> list[Branch]:
    branches:list[Branch] = []
    last_node_key, _ = branch[-1]
    last_node_position = touched_nodes[last_node_key]
    neighbors = get_neighbors_higher(last_node_position)
    for neighbor_position, neighbor_direction in neighbors:
        neighbor_key = get_node_key(neighbor_position)
        node_is_toched = touched_nodes.get(neighbor_key) != None
        if not node_is_toched:
            touched_nodes[neighbor_key] = neighbor_position
            branches += [branch[:-1] + [(last_node_key, neighbor_direction), (neighbor_key, None)]]
    
    return branches


def get_neighbors_higher(position:Position) -> list[tuple[Position, Direction]]:
    i, j = position
    height, width = len(map), len(map[0])
    neighbors = []

    """
    it seems here using incorrect comparison
    but if try to fix it, no path will be found 
    """

    if 0 <= j - 1 and map[i][j-1] - 1 <= map[i][j]:
        neighbors.append(((i, j-1), Direction.LEFT))
    if 0 <= i - 1 and map[i-1][j] - 1 <= map[i][j]:
        neighbors.append(((i-1, j), Direction.UP))
    if j + 1 < width and map[i][j+1] - 1 <= map[i][j]:
        neighbors.append(((i, j+1), Direction.RIGHT))
    if i + 1 < height and map[i+1][j] - 1 <= map[i][j]:
        neighbors.append(((i+1, j), Direction.DOWN))

    return neighbors


def print_path(field:SourceMap, branch:Branch) -> None:
    for i, j in touched_nodes.values():
        field[i][j] = ' '

    for node_key, next_node_direction in branch:
        i, j = touched_nodes[node_key]
        field[i][j] = next_node_direction.value if next_node_direction else '❖'

    for row in field:
        print(''.join(row))


def main() -> None:
    global map
    global source_map

    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    source_map = read_map_from_file(os.path.join(current_directory, input_filename))
    map, start_position, end_position = convert_map(source_map)

    # print(start_position, '→', end_position)
    # for row in map:
    #     print(' '.join([str(node).rjust(2, ' ') for node in row]))

    setup(start_position)
    path = climb_up(end_position)
    
    # if path:
    #     print()
    #     print_path(deepcopy(source_map), path)
    #     print()

    if path:
        print(f"(part 1) required {len(path)} steps for climp up to get the best signal")
    else:
        print('¯\_(ツ)_/¯')


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
