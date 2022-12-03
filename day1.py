# Aoc 2022 - Day 1

from utils import get_data

elfs = [sum(map(int, e.splitlines())) for e in get_data(1).split("\n\n")]
elfs.sort()

print("Part1:", max(elfs))

print("Part2:", sum(elfs[-3:]))


