import os
import time


Program = list[str]


def read_program_from_file(filename:str) -> Program:
    program:Program = []
    with open(filename) as f:
        for line in f.readlines():
            program.append(line.strip())
    return program


def execute_program(program:Program, measurement_scale:list[int]) -> int:
    cycle_count = 0
    register = 1
    signal_strenght = 0

    for instruction in program:
        cycle_count += 1
        if cycle_count in measurement_scale:
            signal_strenght += cycle_count * register

        if instruction.startswith('add'):
            cycle_count += 1
            if cycle_count in measurement_scale:
                signal_strenght += cycle_count * register

        if instruction.startswith('add'):
            _, value = instruction.split(' ')
            register += int(value)

    return signal_strenght


def main():
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    program = read_program_from_file(os.path.join(current_directory, input_filename))

    # solution for part 1
    result = execute_program(program, [20, 60, 100, 140, 180, 220])
    print(f"(part 1) sum of these six signal strengths is {result}")



if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
