count_of_increases = 0
previous_measurement = 0
with open('input.txt') as f:
    for line in f.readlines():
        measurement = int(line.strip())
        if previous_measurement and previous_measurement < measurement:
            count_of_increases += 1

        previous_measurement = measurement

print(f"There are {count_of_increases} measurements that are larger than the previous measurement")
