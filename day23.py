# Aoc 2022 - Day 23

from utils import get_data
from math import inf

lines = get_data(23).strip().split("\n")

elfs = set()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            elfs.add((j, i))

directions = [0,2,3,1]
moved = True
rounds = 0
while moved:
    moved = False
    rounds += 1
    propossed = {}
    for elf in elfs:
        x, y = elf

        empty = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not ( i==0 and j==0):
                    if (x+i, y+j) in elfs:
                        empty = False
                        break

            if not empty:
                break

        if not empty:
            for d in directions:
                if d == 0:
                    if (x, y-1) not in elfs and (x-1, y-1) not in elfs and (x+1, y-1) not in elfs:
                        propossed[elf]= (x, y-1)
                        break
                
                elif d == 1:
                    if (x+1, y) not in elfs and (x+1, y-1) not in elfs and (x+1, y+1) not in elfs:
                        propossed[elf]= (x+1, y)
                        break

                elif d == 2:
                    if (x, y+1) not in elfs and (x+1, y+1) not in elfs and (x-1, y+1) not in elfs:
                        propossed[elf]= (x, y+1)
                        break

                elif d == 3:
                    if (x-1, y) not in elfs and (x-1, y-1) not in elfs and (x-1, y+1) not in elfs:
                        propossed[elf]= (x-1, y)
                        break

        if elf not in propossed:
            propossed[elf] = elf

    
    dup = [x for x in propossed.keys() if list(propossed.values()).count(propossed[x]) > 1]

    new_elfs = set()

    for du in dup:
        new_elfs.add(du)

    for k,v in propossed.items():
        if k not in dup:
            new_elfs.add(v)

    old_d = directions.pop(0)
    directions.append(old_d)

    propossed = {}

    if new_elfs != elfs:
        moved = True

    elfs = new_elfs


    if rounds == 10:
        min_x = min_y = inf
        max_x = max_y = -inf

        for x, y in elfs:
            if x > max_x:
                max_x = x

            if x < min_x:
                min_x = x
            
            if y > max_y:
                max_y = y
            
            if y < min_y:
                min_y = y

        print("Part 1:", (max_x-min_x+1)*(max_y-min_y+1)-len(elfs))


print("Part 2:", rounds)
