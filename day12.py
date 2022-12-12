# Aoc 2022 - Day 12

from utils import get_data

import collections
lines = get_data(12).strip().split("\n")

grid = []

starts = []
start = (0,0)
end = (1,1)

for k, line in enumerate(lines):
    grid.append(list(map(lambda x: ord(x)-ord('a'), line)))

    for i, c in enumerate(grid[k]):
        if c == 0:
            starts.append((k, i))

    l = line.find("S")
    if l != -1:
        start = (k, l)
        grid[k][l] = 0

    l = line.find("E")
    if l != -1:
        end = (k, l)
        grid[k][l] = ord('z')-ord('a')


def dist(s, e):
    return abs(e[0]-s[0]) + abs(e[1]-s[1])

def next_steps(i,j):
    global grid
    possible = []

    val = grid[i][j]
    
    if j+1 < len(grid[i]) and grid[i][j+1] <= val +1:
        possible.append((i, j+1))
    if j > 0 and grid[i][j-1] <= val + 1:
        possible.append((i, j-1))
    if i+1 < len(grid) and grid[i+1][j] <= val +1:
        possible.append((i+1, j))
    if i > 0 and grid[i-1][j] <= val +1:
        possible.append((i-1, j))

    return possible

def calc_steps(starts, end):
    frontier = collections.deque()
    came_from = dict()
    cost_so_far = dict()

    for start in starts:
        frontier.append((start, 0))
        came_from[start] = None
        cost_so_far[start] = 0

    while len(frontier):
        current, _ = frontier.popleft()

        if current == end:
            break
        
        for neigh in next_steps(current[0], current[1]):
            new_cost = cost_so_far[current] + 1
            if neigh not in cost_so_far or new_cost < cost_so_far[neigh]:
                cost_so_far[neigh] = new_cost
                frontier.append((neigh, new_cost + dist(neigh, end)))
                came_from[neigh] = current
    
    return cost_so_far[end]

print("Part 1:", calc_steps([start], end))
print("Part 2:", calc_steps(starts, end))

