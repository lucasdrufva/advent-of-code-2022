# Aoc 2022 - Day 16

from utils import get_data
import re

lines = get_data(16).strip().split("\n")

grid = {}

for line in lines:
    name, flow, tunnels, *_ = re.search(r"Valve (\w\w) has.+=(\d+);.+valves? ((\w\w(,\s)?)+)", line).groups()
    flow = int(flow)
    tunnels = tunnels.split(", ")
    print(name, flow, tunnels)
    grid[name] = {"flow": flow, "tunnels": tunnels}


distances = {}

def shortest_path(s, e):
    global distances
    global grid

    if (s, e) in distances:
        return distances[(s, e)]

    frontier = []
    frontier.append(s)
    
    dist = {s: 0}

    while len(frontier) > 0:
        curr = frontier.pop(0)
        if curr == e:
            distances[(s, e)] = dist[curr]
            return dist[curr]
        for c in grid[curr]["tunnels"]:
            
            if c not in dist or dist[curr] + 1 < dist[c]:
                frontier.append(c)
                dist[c] = dist[curr]+1
   

valves_of_interrest = [valve for valve, flow in grid.items() if flow["flow"] > 0]

paths = []

def max_pressure(current, total_flow, time_elapsed, max_time, visited, store_path):
    global paths
    global valves_of_interrest
    global grid

    if store_path:
        paths.append((total_flow, visited))

    possible_values = []

    for v in [valve for valve in valves_of_interrest if valve not in visited]:
        time = (shortest_path(current, v) + time_elapsed +1)
        time_left = max_time - time
        if time_left > 0:
            possible_values.append(max_pressure(v, total_flow+(grid[v]["flow"]*time_left), time, max_time, visited + [v], store_path))

    if len(possible_values) == 0:
        return total_flow
    else:
        possible_values.sort()
        return possible_values[-1]


print("Part 1:", max_pressure("AA", 0, 0, 30, [], False))

max_pressure("AA", 0, 0, 26, [], True)

max_value = 0
for pressure, path in paths:
    total_pressure = max_pressure("AA", pressure ,0, 26, path, False)

    if total_pressure > max_value:
        max_value = total_pressure

print("Part 2:", max_val)



