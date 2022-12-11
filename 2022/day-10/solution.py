import os
import time
from enum import Enum


class Pixel(Enum):
    LIT  = '#'
    DARK = '.'


SourceProgram = list[str]
TranspiledProgram = list[int|None]
Screen = list[list[Pixel]]


def read_program_from_file(filename:str) -> SourceProgram:
    program:SourceProgram = []
    with open(filename) as f:
        for line in f.readlines():
            program.append(line.strip())
    return program


def transpile(src:SourceProgram) -> TranspiledProgram:
    result:TranspiledProgram = []
    for instruction in src:
        result.append(None)
        if instruction.startswith('add'):
            _, value = instruction.split(' ')
            result.append(int(value))
    
    return result


def get_sum_of_signal_strengths(program:TranspiledProgram, measurement_scale:list[int]) -> int:
    register = 1
    signal_strenght = []

    for i in range(len(program)):
        cycle = i + 1
        if cycle in measurement_scale:
            signal_strenght.append(cycle * register)

        if program[i]:
            register += program[i]

    return sum(signal_strenght)


def draw_image(program:TranspiledProgram) -> Screen:
    register = 1
    screen_width = 40
    work_row = []
    screen:Screen = []

    for i in range(len(program)):
        cycle = i + 1
        sprite = range(register-1, register+2)
        pixel = Pixel.LIT if i % screen_width in sprite else Pixel.DARK
        work_row.append(pixel)

        if cycle % screen_width == 0:
            screen.append(work_row)
            work_row = []

        if program[i]:
            register += program[i]

    return screen


def print_screen(screen:Screen) -> None:
    for row in screen:
        print(' '.join([pixel.value for pixel in row]))


def main():
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    src = read_program_from_file(os.path.join(current_directory, input_filename))
    program = transpile(src)

    # solution for part 1
    result = get_sum_of_signal_strengths(program, [20, 60, 100, 140, 180, 220])
    print(f"(part 1) sum of these six signal strengths is {result}")

    # solution for part 2
    screen = draw_image(program)
    print('(part 2) Letters on CRT:')
    print_screen(screen)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
