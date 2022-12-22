# Aoc 2022 - Day 22

from utils import get_data

import re

lines = get_data(22).split("\n\n")

grid = lines[0].split("\n")

def wrap(x, y, dx, dy, part1):
    global grid
    if dx == 1:
        if part1:
            for k in range(len(grid[y])):
                if not grid[y][k].isspace():
                    return (k, y, 0)

        if x==149:
            return (49, 149-y, 2)
        if x==99:
            if y < 100:
                return (y, 49, 3)
            else:
                return (149, 49-(y-100), 2)
        if x==49:
            return (50+(y-150), 149,3)
    elif dx == -1:
        if part1:
            for k in range(len(grid[y])-1, -1, -1):
                if not grid[y][k].isspace():
                    return (k, y, 2)

        if x == 50:
            if y < 50:
                return (0, 149-y, 0)
            else:
                return ((y-50), 100, 1)
        if x == 0:
            if y < 150:
                return (50, 49-(y-100), 0)
            else:
                return ((y-150)+50, 0, 1)
    elif dy == 1:
        if part1:
            for k in range(len(grid)):
                if not grid[k][x].isspace():
                    return (x, k, 1)

        if y == 199:
            return (x+50, 0, 1)
        if y == 149:
            return (49, 150+(x-50), 2)
        if y == 49:
            return (99, x, 2)
    elif dy == -1:
        if part1:
            for k in range(len(grid)-1, -1, -1):
                if x < len(grid[k]) and not grid[k][x].isspace():
                    return (x, k, 3)

        if y == 0:
            if x < 100:
                return (0, 150+(x-50), 0)
            else:
                return (x-100, 199, 3)
        if y == 100:
            return (50, 50+x, 0)

def run(part1):
    pos_y = 0
    pos_x = 0
    facing = 0

    for i in range(len(grid[0])):
        if grid[0][i] == '.':
            pos_x = i
            break
    
    instruction_index = 0

    while instruction_index < len(lines[1]):
        if instruction_index < len(lines[1])-2:
            start = re.search(r"[RL]", lines[1][instruction_index:]).start() + instruction_index
        else:
            start = len(lines[1])
        count = int(lines[1][instruction_index:start])
        instruction_index = start+1
        
        for _ in range(count):
            if facing == 0:
                if pos_x+1 < len(grid[pos_y]) and grid[pos_y][pos_x+1] == ".":
                    pos_x += 1
                elif pos_x+1 == len(grid[pos_y]) or grid[pos_y][pos_x+1] != "#":
                    new_x, new_y, new_facing = wrap(pos_x, pos_y, 1, 0, part1)
                    if grid[new_y][new_x] == ".":
                        pos_x = new_x
                        pos_y = new_y
                        facing = new_facing
                    else:
                        continue
            if facing == 1:
                if pos_y+1 < len(grid) and pos_x < len(grid[pos_y+1]) and grid[pos_y+1][pos_x] == ".":
                    pos_y += 1
                elif pos_y+1 == len(grid) or pos_x >= len(grid[pos_y+1]) or grid[pos_y+1][pos_x] != "#":
                    new_x, new_y, new_facing = wrap(pos_x, pos_y, 0, 1, part1)
                    if grid[new_y][new_x] == ".":
                        pos_x = new_x
                        pos_y = new_y
                        facing = new_facing
                    else:
                        continue
        

            if facing == 2:
                if pos_x -1 >= 0 and grid[pos_y][pos_x-1] == ".":
                    pos_x -= 1
                elif pos_x == 0 or grid[pos_y][pos_x-1] != "#":
                    new_x, new_y, new_facing = wrap(pos_x, pos_y, -1, 0, part1)
                    if grid[new_y][new_x] == ".":
                        pos_x = new_x
                        pos_y = new_y
                        facing = new_facing
                    else:
                        continue

            if facing == 3:
                if pos_y -1 >= 0 and grid[pos_y-1][pos_x] == ".":
                    pos_y -= 1
                elif pos_y == 0 or grid[pos_y-1][pos_x] != "#":
                    new_x, new_y, new_facing = wrap(pos_x, pos_y, 0, -1, part1)
                    if grid[new_y][new_x] == ".":
                        pos_x = new_x
                        pos_y = new_y
                        facing = new_facing
                    else:
                        continue

        if start < len(lines[1]):
            if lines[1][start] == "R":
                facing += 1
            elif lines[1][start] == "L":
                facing -= 1


            facing = facing%4

    return (pos_y+1)*1000 + (pos_x+1)*4 + facing




print("Part 1:", run(True))
print("Part 2:", run(False))




