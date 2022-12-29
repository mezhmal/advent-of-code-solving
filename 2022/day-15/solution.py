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


def strip_report(report:Report, target_line:int) -> Report:
    '''
    we can exclude those sensors coverage area of which not crossing the target line
    that would greatly reduce size of map
    '''
    result:Report = []
    for record in report:
        sensor_position, _, distance = record
        _, sensor_position_y = sensor_position
        if sensor_position_y - distance < target_line < sensor_position_y + distance:
            result.append(record)
    return result


def init_map(report:Report) -> None:
    global map
    global relative_shift

    min_x, min_y, max_x, max_y = find_edges(report)
    map_height = max_y - min_y + 1
    map_width = max_x - min_x + 1

    for _ in range(map_height):
        map.append([Matter.EMPTY] * map_width)

    relative_shift_x, relative_shift_y = min_x, min_y
    relative_shift = relative_shift_x, relative_shift_y

    for sensor_position, beacon_position, _ in report:
        sensor_position_x, sensor_position_y, beacon_position_x, beacon_position_y = sensor_position + beacon_position
        sensor_calibrated_x = sensor_position_x - relative_shift_x
        sensor_calibrated_y = sensor_position_y - relative_shift_y
        beacon_calibrated_x = beacon_position_x - relative_shift_x
        beacon_calibrated_y = beacon_position_y - relative_shift_y
        map[sensor_calibrated_y][sensor_calibrated_x] = Matter.SENSOR
        map[beacon_calibrated_y][beacon_calibrated_x] = Matter.BEACON


def set_coverage(report:Report) -> None:
    global map
    global relative_shift

    for sensor_position, _, distance in report:
        relative_shift_x, relative_shift_y = relative_shift

        sensor_position_x, sensor_position_y = sensor_position

        actual_sensor_position_x = sensor_position_x - relative_shift_x
        actual_sensor_position_y = sensor_position_y - relative_shift_y

        map_height = len(map)
        map_width = len(map[0])

        if actual_sensor_position_y - distance < 0:
            'expand map to top if necessary'
            expand_length = abs(actual_sensor_position_y - distance)
            for _ in range(expand_length):
                map.insert(0, [Matter.EMPTY] * map_width)

            relative_shift_y -= expand_length
            actual_sensor_position_y = sensor_position_y - relative_shift_y
            relative_shift = relative_shift_x, relative_shift_y
            map_height = len(map)

        if actual_sensor_position_x - distance < 0:
            'expand map to left if necessary'
            expand_length = abs(actual_sensor_position_x - distance)
            for i in range(map_height):
                map[i] = [Matter.EMPTY] * expand_length + map[i]

            relative_shift_x -= expand_length
            actual_sensor_position_x = sensor_position_x - relative_shift_x
            relative_shift = relative_shift_x, relative_shift_y
            map_width = len(map[0])

        if actual_sensor_position_y + distance >= map_height:
            'expand map to bottom if necessary'
            expand_length = abs(actual_sensor_position_y + distance - map_height) + 1
            for _ in range(expand_length):
                map.append([Matter.EMPTY] * map_width)

            map_height = len(map)

        if actual_sensor_position_x + distance >= map_width:
            'expand map to right if necessary'
            expand_length = abs(actual_sensor_position_x + distance - map_width) + 1
            for i in range(map_height):
                map[i] += [Matter.EMPTY] * expand_length

            map_width = len(map[0])

        for i in range(distance + 1):
            for j in range(distance + 1 - i):
                '↑'
                covered_y = actual_sensor_position_y - i
                '←'
                covered_x = actual_sensor_position_x - j
                if map[covered_y][covered_x] == Matter.EMPTY:
                    map[covered_y][covered_x] = Matter.COVERED

                '→'
                covered_x = actual_sensor_position_x + j
                if map[covered_y][covered_x] == Matter.EMPTY:
                    map[covered_y][covered_x] = Matter.COVERED

                '↓'
                covered_y = actual_sensor_position_y + i
                '←'
                covered_x = actual_sensor_position_x - j
                if map[covered_y][covered_x] == Matter.EMPTY:
                    map[covered_y][covered_x] = Matter.COVERED

                '→'
                covered_x = actual_sensor_position_x + j
                if map[covered_y][covered_x] == Matter.EMPTY:
                    map[covered_y][covered_x] = Matter.COVERED

        # print()
        # print(sensor_position)
        # print_map()
        # print()


def print_map() -> None:
    global map

    for line in map:
        print(' '.join([tile.value for tile in line]))


def main() -> None:
    input_filename = 'example.txt'
    current_directory = os.path.dirname(__file__)
    report = read_report_from_file(os.path.join(current_directory, input_filename))

    # solution for part 1

    target_line = 10
    stripped_report = strip_report(report, target_line)

    init_map(stripped_report)
    set_coverage(stripped_report)
    print_map()

    print()
    _, shift_y = relative_shift
    print(' '.join([tile.value for tile in map[target_line - shift_y]]))


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
