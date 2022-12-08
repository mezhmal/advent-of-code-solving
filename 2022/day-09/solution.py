import os
import time


def read_from_file(filename:str) -> list[list[int]]:
    lines = []
    with open(filename) as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines


def main():
    pass


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    print(f"Done in {stop-start:0.3f}s")
