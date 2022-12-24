# Aoc 2022 - Day 24

from utils import get_data
import heapq

#regex
#import re

# a, b = re.search(r"([a-z]+).([a-z]+)", target_string).groups()

lines = get_data(24).strip().split("\n")

#mapped to ints
#nums = list(map(int, lines))
max_x = len(lines[0]) - 2
max_y = len(lines) - 2

blizzards = set()

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "<":
            blizzards.add((i-1, j-1, 0, -1))
        elif c == ">":
            blizzards.add((i-1, j-1, 0, 1))
        elif c == "v":
            blizzards.add((i-1, j-1, 1, 0))
        elif c == "^":
            blizzards.add((i-1, j-1, -1, 0))

walls = {(-2, 0), (-1, -1), (-1, 1)}
for i in range(-1, max_x+1):
    if i != 0:
        walls.add((-1, i))
    if i != max_x-1:
        walls.add((max_y, i))

for i in range(-1, max_y+1):
    walls.add((i, -1))
    walls.add((i, max_x))


t = 0
frontier = {(-1, 0)}
goals = [(max_y, max_x-1), (-1, 0), (max_y, max_x-1)]
while len(goals) > 0:
    t+=1
    blizz = {((y+dy*t)%max_y, (x+dx*t)%max_x) for y, x, dy, dx, in blizzards}
    new_front = {(y+dy, x+dx) for dy,dx in ((-1, 0), (1, 0), (0, 1), (0, -1), (0,0)) for y, x in frontier}
    frontier = new_front - blizz - walls

    if goals[0] in frontier:
        if len(goals) == 3:
            print("Part 1:", t)
        frontier = {goals.pop(0)}

print("Part 2:", t)


