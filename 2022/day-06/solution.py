import os


input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    data = f.read().rstrip()


def get_start_position(data, marker_length):
    for i in range(len(data) - marker_length + 1):
        if len(set(data[i:i+marker_length])) == marker_length:
            return i + marker_length


# solution for part 1

print(f"Packet starts at {get_start_position(data, 4)} position")

# solution for part 2

print(f"Message starts at {get_start_position(data, 14)} position")
