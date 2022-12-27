import os
import sys
import time
from enum import Enum


class Matter(Enum):
    AIR          = '.'
    ROCK         = '#'
    SAND_SOURCE  = '+'
    REST_SAND    = 'o'
    FALLING_SAND = '~'

PositionX = int
PositionY = int
Position = tuple[PositionX, PositionY]
Rocks = set[Position]
Map = list[list[Matter]]


map:Map = []


def read_scan_data_from_file(filename:str) -> Rocks:
    rocks:Rocks = set()
    with open(filename) as f:
        for line in f.readlines():
            prev_position: Position | None = None
            for position in line.strip().split(' -> '):
                x, y = [int(value) for value in position.split(',')]                
                if prev_position != None:
                    prev_x, prev_y = prev_position
                    if prev_x != x:
                        for j in range(min(prev_x, x), max(prev_x, x) + 1):
                            rocks.add((j, y))
                    else:
                        for i in range(min(prev_y, y), max(prev_y, y) + 1):
                            rocks.add((x, i))
                
                prev_position = (x, y)

    return rocks


def find_edges(rocks:Rocks) -> tuple[PositionX, PositionY, PositionX, PositionY]:
    min_x, min_y, max_x, max_y = sys.maxsize, 0, 0, 0
    for x, y in rocks:
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)
    return min_x, min_y, max_x, max_y


def fill_with_rocks(rocks:Rocks, offset:Position) -> None:
    offset_x, offset_y = offset
    for x, y in rocks:
        map[y - offset_y][x - offset_x] = Matter.ROCK


def init_map(rocks:Rocks) -> None:
    global map
    
    min_x, min_y, max_x, max_y = find_edges(rocks)
    top_gap = 0
    map_height = max_y - min_y + top_gap + 1
    map_width = max_x - min_x + 3

    for _ in range(map_height):
        map += [[Matter.AIR] * map_width]

    fill_with_rocks(rocks, (min_x - 1, min_y - top_gap))
    map[0][500 - min_x + 1] = Matter.SAND_SOURCE


def simulate_falling_sand() -> None:
    pass


def print_map() -> None:
    global map

    for line in map:
        print(' '.join([tile.value for tile in line]))


def main() -> None:
    input_filename = 'example.txt'
    current_directory = os.path.dirname(__file__)
    rocks = read_scan_data_from_file(os.path.join(current_directory, input_filename))
    init_map(rocks)
    simulate_falling_sand()
    print_map()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
