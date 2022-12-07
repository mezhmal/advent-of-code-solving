import os
import time


def main():
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)

    with open(os.path.join(current_directory, input_filename)) as f:
        for line in f.readlines():
            data = line.strip()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    print(f"Done in {stop-start:0.4f} seconds")
