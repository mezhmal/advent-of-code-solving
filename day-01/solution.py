calories = []
with open('calories.txt') as f:
    elf_inventory = 0
    for line in f.readlines():
        value = line.strip()
        if not value:
            calories.append(elf_inventory)
            elf_inventory = 0
        else:
            elf_inventory += int(value)

calories.sort(reverse=True)
print(f"Max calories: {calories[0]}")
print(f"Top three total calories: {sum(calories[:3])}")
