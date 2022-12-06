import os


input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    data = f.read().rstrip()

start_of_packet_marker_length = 4

# solution for part 1

result = 0
for i in range(len(data) - start_of_packet_marker_length + 1):
    if len(set(data[i:i+start_of_packet_marker_length])) == start_of_packet_marker_length:
        result = i + start_of_packet_marker_length
        break

print(f"{result} characters need to be processed before the first start-of-packet marker is detected")
