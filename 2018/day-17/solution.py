import os
import time
from enum import Enum


class Matter(Enum):
    SAND         = '.'
    CLAY         = '#'
    WATER_SPRING = '+'
    REST_WATER   = '~'
    PASS_WATER   = '|'


VeinOfClay = tuple[list[int], list[int]]
ScanData = list[VeinOfClay]
Border = BorderTop = BorderRight = BorderBottom = BorderLeft = int
SliceMap = list[list[Matter]]
Position = tuple[int, int]


leak_queue:list[Position] = []
slice_map:SliceMap = []


def read_scan_data_from_file(filename:str) -> ScanData:
    scan_data:ScanData = []
    with open(filename) as f:
        for line in f.readlines():
            x, y = None, None
            for record in line.strip().split(', '):
                dimention, value = record.split('=')
                if '..' in value:
                    start, stop = value.split('..')
                    value = list(range(int(start), int(stop) + 1))
                else:
                    value = [int(value)]

                if dimention == 'x':
                    x = value
                else:
                    y = value
            scan_data.append((x, y))

    return scan_data


def get_borders(scan_data:ScanData) -> tuple[BorderTop, BorderRight, BorderBottom, BorderLeft]:
    border_top, border_right, border_bottom, border_left = None, None, None, None
    for x, y in scan_data:
        border_left = min(border_left, x[0]) if border_left != None else x[0]
        border_right = max(border_right, x[-1]) if border_right != None else x[-1]
        border_top = min(border_top, y[0]) if border_top != None else y[0]
        border_bottom = max(border_bottom, y[-1]) if border_bottom != None else y[-1]

    return (border_top, border_right, border_bottom, border_left)


def fill_with_clay(slice_map:SliceMap, scan_data:ScanData, delta:Position) -> SliceMap:
    delta_x, delta_y = delta
    for x, y in scan_data:
        for j in x:
            for i in y:
                slice_map[i - delta_y][j - delta_x] = Matter.CLAY

    return slice_map


def init_slice_map(scan_data:ScanData) -> None:
    global slice_map

    slice_map = []
    border_top, border_right, border_bottom, border_left = get_borders(scan_data)
    map_height = border_bottom - border_top + 2
    map_width = border_right - border_left + 3

    for _ in range(map_height):
        slice_map += [[Matter.SAND] * map_width]

    slice_map = fill_with_clay(slice_map, scan_data, (border_left - 1, border_top - 1))
    slice_map[0][500 - border_left + 1] = Matter.WATER_SPRING


def get_spring_water_position() -> Position:
    global slice_map

    for y in range(len(slice_map)):
        for x in range(len(slice_map[y])):
            if slice_map[y][x] == Matter.WATER_SPRING:
                return (x, y)


def fill_with_water() -> None:
    global slice_map

    map_height, map_width = len(slice_map), len(slice_map[0])
    while True:
        if not leak_queue:
            break

        start_x, start_y = leak_queue.pop(0)

        y = start_y
        while True:
            slice_map[y][start_x] = Matter.PASS_WATER
            if y == map_height - 1 or slice_map[y+1][start_x] != Matter.SAND:
                break

            y += 1
        
        if y != map_height - 1 and slice_map[y+1][start_x] != Matter.PASS_WATER:
            "try to fill out"
            left_leak, right_leak = False, False

            while y > 0:
                left_x = start_x - 1
                while left_x >= 0:
                    if slice_map[y][left_x] == Matter.CLAY:
                        break

                    if slice_map[y + 1][left_x] == Matter.SAND:
                        left_leak = True
                        break

                    left_x -= 1
                
                right_x = start_x + 1
                while right_x < map_width:
                    if slice_map[y][right_x] == Matter.CLAY:
                        break

                    if slice_map[y + 1][right_x] == Matter.SAND:
                        right_leak = True
                        break

                    right_x += 1
                
                if left_leak or right_leak:
                    for x in range(left_x+1,right_x):
                        slice_map[y][x] = Matter.PASS_WATER

                    if left_leak and (left_x, y) not in leak_queue:
                        leak_queue.append((left_x, y))

                    if right_leak and (right_x, y) not in leak_queue:
                        leak_queue.append((right_x, y))

                    break
                else:
                    for x in range(left_x+1,right_x):
                        slice_map[y][x] = Matter.REST_WATER

                y -= 1


def count_water(kind:list[Matter]) -> int:
    global slice_map

    return sum([sum([1 for tile in line if tile in kind]) for line in slice_map])


def print_slice_map() -> None:
    global slice_map

    for line in slice_map:
        print(' '.join([tile.value for tile in line]))


def main() -> None:
    global leak_queue
    global slice_map

    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    scan_data = read_scan_data_from_file(os.path.join(current_directory, input_filename))
    init_slice_map(scan_data)
    spring_water_position_x, spring_water_position_y = get_spring_water_position()
    leak_queue.append((spring_water_position_x, spring_water_position_y + 1))
    fill_with_water()
    print(f"(part 1) total number of tiles the water can reach is {count_water([Matter.PASS_WATER, Matter.REST_WATER])}")
    print(f"(part 2) {count_water([Matter.REST_WATER])} tiles of water will be retained after the water spring will dry up")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
