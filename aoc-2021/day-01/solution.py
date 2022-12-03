import os


measurements = []
input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        measurements.append(int(line.strip()))

count_of_increases = 0
previous_measurement = 0
for measurement in measurements:
    if previous_measurement and previous_measurement < measurement:
        count_of_increases += 1

    previous_measurement = measurement

print(f"There are {count_of_increases} measurements that are larger than the previous measurement")

measurements_length = len(measurements)
count_of_increases = 0
previous_measurement = 0

for i in range(measurements_length):
    if i < measurements_length - 2:
        three_measurement_window = sum(measurements[i:i+3])
        if previous_measurement and previous_measurement < three_measurement_window:
            count_of_increases += 1

        previous_measurement = three_measurement_window
        # print(f"{i}: {measurements[i]} [{', '.join([str(m) for m in measurements[i:i+3]])}]")

print(f"There are {count_of_increases} sums that are larger than the previous sum")
