# Aoc 2022 - Day 21

from utils import get_data
import math

lines = get_data(21).strip().split("\n")

monkeys = {}

for line in lines:
    line = line.split(": ")
    monkeys[line[0]] = line[1].split(" ")

super_path = []

def calc_monkey(monkey, path):
    global super_path
    if monkey == "humn":
        super_path = path
    m = monkeys[monkey]
    if len(m) == 1:
        return int(m[0])
    else:
        if m[1] == "+":
            return calc_monkey(m[0], path + [monkey]) + calc_monkey(m[2], path + [monkey])
        elif m[1] == "-":
            return calc_monkey(m[0], path + [monkey]) - calc_monkey(m[2], path + [monkey])
        elif m[1] == "*":
            return calc_monkey(m[0], path + [monkey] ) * calc_monkey(m[2], path + [monkey])
        elif m[1] == "/":
            return math.floor(calc_monkey(m[0], path + [monkey]) / calc_monkey(m[2], path + [monkey]))

print("Part 1:", calc_monkey("root", []))

val = calc_monkey(monkeys["root"][2], [])
origval = val
for i in range(1, len(super_path)):
    m = monkeys[super_path[i]]
    cal = 0
    if m[0] in super_path or m[0] == "humn":
        cal = calc_monkey(m[2], [])
        if m[1] == "*":
            val = math.floor(val/cal)
        elif m[1] == "/":
            val *= cal
        elif m[1] == "-":
            val -= cal
        elif m[1] == "+":
            val -= cal
    else:
        cal = calc_monkey(m[0], [])
        if m[1] == "*":
            val = math.floor(val/cal)
        elif m[1] == "/":
            val = math.floor(cal/val)
        elif m[1] == "-":
            val = cal - val
        elif m[1] == "+":
            val -= cal


for i in range(-10000, 10000):
    monkeys["humn"] = [val+i]
    if calc_monkey(monkeys["root"][0], []) == origval:
        print("Part 2", i+val)
        break







