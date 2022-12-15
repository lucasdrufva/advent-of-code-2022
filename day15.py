# Aoc 2022 - Day 15

from utils import get_data

#regex
import re

# a, b = re.search(r"([a-z]+).([a-z]+)", target_string).groups()

lines = get_data(15).strip().split("\n")

#Sensor -> radius
network = {}
beacons = set()

#mapped to ints
#nums = list(map(int, lines))
min_x = 10000
max_x = 0

for line in lines:
    sx,sy,cx,cy = map(int, re.search(r".+x=(-?\d+), y=(-?\d+):.+x=(-?\d+), y=(-?\d+)", line).groups())
    #print(sx,sy,cx,cy)
    beacons.add((cx,cy))
    network[(sx,sy)] = abs(sx-cx) + abs(sy-cy)
    if sx < min_x:
        min_x = sx
    if cx < min_x:
        min_x = cx

    if sx > max_x:
        max_x = sx
    if cx > max_x:
        max_x = sx



test_y = 2000000

count = 0

for x in range(min_x-20000000,max_x+20000000):
    for k, v in network.items():
        if abs(k[0]-x) + abs(k[1]-test_y) <= v and (x, test_y) not in beacons:
            # print(x)
            count += 1
            break


print(count)



