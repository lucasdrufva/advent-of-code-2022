# Aoc 2022 - Day 1

elfs = [sum(map(int, e.splitlines())) for e in open("input1.txt").read().split("\n\n")]
elfs.sort()

print("Part1:", max(elfs))

print("Part2:", sum(elfs[-3:]))


