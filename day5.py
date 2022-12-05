# Aoc 2022 - Day 5

from copy import deepcopy
from utils import get_data
import re

lines = get_data(5).split("\n\n")
cargo = lines[0].split("\n")
instructions = lines[1].strip().split("\n")

stack_labels = list(map(int, re.findall(r"(\s\d\s)+", cargo[-1])))
stack_indexes = []

stacks = {}
for s in stack_labels:
    stacks[s] = []
    stack_indexes.append(cargo[-1].index(str(s)))


for i in range(len(cargo)-2, -1, -1):
    for label, index in zip(stack_labels, stack_indexes):
        if cargo[i][index] != " ":
            stacks[label].append(cargo[i][index])


part1_stacks = stacks
part2_stacks = deepcopy(stacks)

for line in instructions:
    count, from_stack, to_stack = list(map(int, re.findall(r"\d+", line)))
    # Part 1
    for _ in range(count):
        value = part1_stacks[from_stack].pop()
        part1_stacks[to_stack].append(value)

    # Part 2
    moving = part2_stacks[from_stack][(-count):]

    # Delete moving part from from stack
    part2_stacks[from_stack] = part2_stacks[from_stack][:(-count)]

    part2_stacks[to_stack] += moving



part1 = ""
part2 = ""
for k in stacks:
    part1 += part1_stacks[k].pop()
    part2 += part2_stacks[k].pop()


print("Part 1: ", part1)
print("Part 2: ", part2)

