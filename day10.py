# Aoc 2022 - Day 10

from utils import get_data
import re

lines = get_data(10).split("\n")

clock = 0

x=1
next_x = 1

part1 = 0

def add_clock():
    global clock
    global x
    global part1
    
    if(abs(x-(clock%40)) <= 1):
        print("#", end="")
    else:
        print(" ", end="")

    clock += 1
    if clock > 0 and clock%40 == 0:
        print("")


    if clock in [20, 60, 100, 140, 180, 220]:
        part1 += clock*x

for line in lines:
    if match := re.match(r"addx (\-?\d+)", line):
        next_x = x + int(match.group(1))
        add_clock()

    add_clock()
    x = next_x

print(part1)


