import os
import sys
import time
from enum import Enum


class Matter(Enum):
    EMPTY   = '.'
    COVERED = '#'
    SENSOR  = 'S'
    BEACON  = 'B'


PositionX = int
PositionY = int
Position = tuple[PositionX, PositionY]
SensorPosition = Position
BeaconPosition = Position
Distance = int
Record = tuple[SensorPosition, BeaconPosition, Distance]
Report = list[Record]
Map = list[list[Matter]]


map = []
relative_shift:Position = (0, 0)


def read_report_from_file(filename:str) -> Report:
    report:Report = []
    with open(filename) as f:
        for line in f.readlines():
            sensor_part, beacon_part = line.strip().split(': ')
            sensor_position_x, sensor_position_y = sensor_part[10:].split(', ')
            sensor_position_x_value, sensor_position_y_value = int(sensor_position_x[2:]), int(sensor_position_y[2:])
            beacon_position_x, beacon_position_y = beacon_part[21:].split(', ')
            beacon_position_x_value, beacon_position_y_value = int(beacon_position_x[2:]), int(beacon_position_y[2:])
            distance = abs(sensor_position_x_value - beacon_position_x_value) + abs(sensor_position_y_value - beacon_position_y_value)
            report += [((sensor_position_x_value, sensor_position_y_value), (beacon_position_x_value, beacon_position_y_value ), distance)]

    return report


def find_edges(report:Report) -> tuple[PositionX, PositionY, PositionX, PositionY]:
    min_x, min_y = sys.maxsize, sys.maxsize
    max_x, max_y = sys.maxsize * -1, sys.maxsize * -1
    for sensor_position, beacon_position, _ in report:
        for x, y in [sensor_position, beacon_position]:
            min_x, min_y = min(x, min_x), min(y, min_y)
            max_x, max_y = max(x, max_x), max(y, max_y)

    return min_x, min_y, max_x, max_y


def strip_report(report:Report, line:int) -> Report:
    '''
    we can exclude those sensors coverage area of which not crossing the target line
    that would greatly reduce size of map
    '''

    result:Report = []
    for record in report:
        sensor_position, _, distance = record
        _, sensor_position_y = sensor_position
        if sensor_position_y - distance < line < sensor_position_y + distance:
            result.append(record)
    return result


def init_map(report:Report, target_line:int) -> None:
    '''
    attempt to reduce map to one target line
    '''

    global map
    global relative_shift

    min_x, min_y, max_x, _ = find_edges(report)
    map_width = max_x - min_x + 1

    map = [Matter.EMPTY] * map_width

    relative_shift_x, relative_shift_y = min_x, target_line - min_y
    relative_shift = relative_shift_x, relative_shift_y

    for sensor_position, beacon_position, _ in report:
        sensor_position_x, sensor_position_y, beacon_position_x, beacon_position_y = sensor_position + beacon_position
        sensor_calibrated_x = sensor_position_x - relative_shift_x
        beacon_calibrated_x = beacon_position_x - relative_shift_x

        if sensor_position_y == target_line:
            map[sensor_calibrated_x] = Matter.SENSOR
        if beacon_position_y == target_line:
            map[beacon_calibrated_x] = Matter.BEACON


def set_coverage(report:Report, target_line:int) -> None:
    global map
    global relative_shift

    for sensor_position, _, distance in report:
        relative_shift_x, relative_shift_y = relative_shift

        sensor_position_x, sensor_position_y = sensor_position

        actual_target_line = target_line - relative_shift_y
        actual_sensor_position_x = sensor_position_x - relative_shift_x
        actual_sensor_position_y = sensor_position_y - relative_shift_y

        map_width = len(map)

        if actual_sensor_position_x - distance < 0:
            'expand map to left if necessary'
            expand_length = abs(actual_sensor_position_x - distance)
            map = [Matter.EMPTY] * expand_length + map
            relative_shift_x -= expand_length
            actual_sensor_position_x = sensor_position_x - relative_shift_x
            relative_shift = relative_shift_x, relative_shift_y
            map_width = len(map)

        if actual_sensor_position_x + distance >= map_width:
            'expand map to right if necessary'
            expand_length = abs(actual_sensor_position_x + distance - map_width) + 1
            map += [Matter.EMPTY] * expand_length
            map_width = len(map)

        for i in range(distance + 1):
            if actual_sensor_position_y - i == actual_target_line or actual_sensor_position_y + i == actual_target_line:
                for j in range(distance + 1 - i):
                    '←'
                    covered_x = actual_sensor_position_x - j
                    if map[covered_x] == Matter.EMPTY:
                        map[covered_x] = Matter.COVERED

                    '→'
                    covered_x = actual_sensor_position_x + j
                    if map[covered_x] == Matter.EMPTY:
                        map[covered_x] = Matter.COVERED


def get_distance_to_possible_next_beacon():
    global map
    return len([tile for tile in map if tile == Matter.COVERED])


def print_map() -> None:
    global map
    print(''.join([tile.value for tile in map]))


def main() -> None:
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    report = read_report_from_file(os.path.join(current_directory, input_filename))

    # solution for part 1

    target_line = 2000000
    stripped_report = strip_report(report, target_line)
    init_map(stripped_report, target_line)
    set_coverage(stripped_report, target_line)
    print(f"(part 1) {get_distance_to_possible_next_beacon()} positions cannot contain a beacon")
    
    # print_map()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
