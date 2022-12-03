# Aoc 2022 - Day 3

from utils import get_data

lines = get_data(3).split("\n")

def calculate_priority(item):
    if (item.isupper()):
        return ord(item)-ord('A') + 27
    else:
        return ord(item)-ord('a') + 1


total_priorities = 0
total_badge_priorities = 0

current_group = []

for line in lines:
    # Part 1
    middle = int(len(line)/2)
    left = set(line[:middle])
    right = set(line[middle:])
    common = left & right


    for _, elem in enumerate(common):
        total_priorities += calculate_priority(elem)    

    # Part 2
    
    # Add current elfs packing to current group
    current_group.append(set(line))

    if len(current_group) == 3:
        # Find common
        (badge, ) = current_group[0] & current_group[1] & current_group[2]

        # Increase priority sum
        total_badge_priorities += calculate_priority(badge)

        # reset group to empty
        current_group = []


print("Part 1:", total_priorities)
print("Part 2:", total_badge_priorities)



