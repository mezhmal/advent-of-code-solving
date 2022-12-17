import json
import os
import time
from functools import cmp_to_key, reduce


"""
solution for puzzle https://adventofcode.com/2022/day/13
"""

Packet = list[int|list]
Pair = tuple[Packet, Packet]
Signal = list[Pair]


def read_signal_from_file(filename:str) -> Signal:
    signal:Signal = []
    left_packet, right_packet = None, None
    with open(filename) as f:
        for line in f.readlines():
            stripped_line = line.strip()
            if not stripped_line:
                signal.append((left_packet, right_packet))
                left_packet, right_packet = None, None
            else:
                packet = json.loads(stripped_line)
                if left_packet == None:
                    left_packet = packet
                else:
                    right_packet = packet
    signal.append((left_packet, right_packet))

    return signal


def is_order_right(left_packet:Packet, right_packet:Packet) -> bool | None:
    for i in range(len(left_packet)):
        left_value = left_packet[i]
        right_value = 0
        try:
            right_value = right_packet[i]
        except IndexError:
            return False

        if type(left_value) == int and type(right_value) == int:
            if left_value != right_value:
                return left_value < right_value
        else:
            if type(left_value) == int:
                left_value = [left_value]
            if type(right_value) == int:
                right_value = [right_value]

            order_is_right = is_order_right(left_value, right_value)
            if order_is_right != None:
                return order_is_right

    if len(left_packet) < len(right_packet):
        return True


def packets_comporator(packet1:Packet, packet2:Packet) -> int:
    return -1 if is_order_right(packet1, packet2) else 1


def get_decoder_key(packets:list[Packet], divider_packets:list[Packet]) -> int:
    indices_of_the__divider_packets = [packets.index(divider_packet) + 1 for divider_packet in divider_packets]
    return reduce(lambda x, y: x * y, indices_of_the__divider_packets, 1)


def main() -> None:
    input_filename = 'input.txt'
    current_directory = os.path.dirname(__file__)
    signal = read_signal_from_file(os.path.join(current_directory, input_filename))

    # solution for part 1

    indices_of_the_pairs_that_are_already_in_the_right_order = []
    for i in range(len(signal)):
        if is_order_right(*signal[i]):
            indices_of_the_pairs_that_are_already_in_the_right_order.append(i + 1)

    print(f"(part1) Sum of indices of the pairs that are already in the right order: {sum(indices_of_the_pairs_that_are_already_in_the_right_order)}")


    # solution for part 2

    divider_packets = [[[2]], [[6]]]
    packets:list[Packet] = [] + divider_packets
    for left_packet, right_packet in signal:
        packets += [left_packet, right_packet]

    sort_key = cmp_to_key(packets_comporator)
    packets.sort(key=sort_key)
    decoder_key = get_decoder_key(packets, divider_packets)
    print(f"(part 2) Decoder key for the distress signal: {decoder_key}")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    result = f"Done in {stop-start:0.3f}s"
    print('-' * len(result))
    print(result)
