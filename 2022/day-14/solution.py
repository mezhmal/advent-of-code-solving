import os
import sys
import time
from enum import Enum


class Matter(Enum):
    AIR            = '.'
    ROCK           = '#'
    SOURCE_OF_SAND = '+'
    REST_SAND      = 'o'
    FALLING_SAND   = '~'

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
    map[0][500 - min_x + 1] = Matter.SOURCE_OF_SAND


def simulate_falling_sand() -> int:
    source_of_sand = find_source_of_sand()

    fallen_units = 0

    while fall_one_unit_of_sand(source_of_sand):
        fallen_units += 1

        if fallen_units > 10000:
            return 0

    return fallen_units

def find_source_of_sand() -> Position:
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == Matter.SOURCE_OF_SAND:
                return x, y


def fall_one_unit_of_sand(position:Position) -> bool:
    x, y = position
    map_heigth = len(map)
    while True:
        if y + 1 == map_heigth:
            'sand starts flowing into the abyss below'
            return False

        if map[y + 1][x] == Matter.AIR:
            'trying to move down'
            y += 1
            continue

        if map[y + 1][x - 1] == Matter.AIR:
            'trying to move down-left'
            y += 1
            x -= 1
            continue

        if map[y + 1][x + 1] == Matter.AIR:
            'trying to move down-right'
            y += 1
            x += 1
            continue

        map[y][x] = Matter.REST_SAND
        return True


def print_map() -> None:
    global map

    for line in map:
        print(' '.join([tile.value for tile in line]))


def main() -> None:
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    rocks = read_scan_data_from_file(os.path.join(current_directory, input_filename))
    init_map(rocks)
    
    # solution for part 1

    fallen_units = simulate_falling_sand()
    print(f"(part 1) {fallen_units} units of sand come to rest before sand starts flowing into the abyss below")

    # print_map()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
