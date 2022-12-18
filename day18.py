# Aoc 2022 - Day 18

from utils import get_data
import re

lines = get_data(18).strip().split("\n")

cubes = {}

for line in lines:
    x,y,z = map(int, line.split(","))
    cubes[(x,y,z)] = 1

def neighbors(cube):
    x,y,z = cube
    neighs = []
    if x >= -1:
        neighs.append((x-1, y, z))
    if x < 21:
        neighs.append((x+1, y, z))
    if y >= -1:
        neighs.append((x, y-1, z))
    if y < 21:
        neighs.append((x, y+1, z))
    if z >= -1:
        neighs.append((x, y, z-1))
    if z < 21:
        neighs.append((x, y, z+1))

    return neighs

reachable_air = set()

def reachable(cube):
    global grid
    global reachable_air
    if cube in reachable_air:
        return True
    
    frontier = []
    frontier.append(cube)
    visited = set()
    while len(frontier) > 0:
        curr = frontier.pop(0)
        if curr in reachable_air or curr == (0,0,0):
            reachable_air.update(visited)
            return True
        for n in neighbors(curr):
            if n not in visited and cubes.get(n, 0) != 1:
                visited.add(n)
                frontier.append(n)

    return False


def calc_sides(part1):
    sides = 0
    for cube in cubes.keys():
        x, y, z = cube
        exposed_sides = 0
        if (x+1, y, z) not in cubes and (reachable((x+1, y, z)) or part1):
            exposed_sides += 1
        if (x-1, y, z) not in cubes and (reachable((x-1, y, z)) or part1):
            exposed_sides += 1
        if (x, y+1, z) not in cubes and (reachable((x, y+1, z)) or part1):
            exposed_sides += 1
        if (x, y-1, z) not in cubes and (reachable((x, y-1, z)) or part1):
            exposed_sides += 1
        if (x, y, z+1) not in cubes and (reachable((x, y, z+1)) or part1):
            exposed_sides += 1
        if (x, y, z-1) not in cubes and (reachable((x, y, z-1)) or part1):
            exposed_sides += 1

        sides += exposed_sides
   
    return sides
    
print("Part 1:", calc_sides(True))
print("Part 2:", calc_sides(False))






