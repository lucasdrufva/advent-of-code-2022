# Aoc 2022 - Day 11

from utils import get_data

import re
import math

lines = get_data(11).split("\n\n")

monkeys = {}
for line in lines:
    i, items, operation, constant, test, true, false = re.search(r"^Monkey (\d):\s+.+:([0-9\, ]+)\s+.+([\*\+]) (\d+|old)\s+.+by (\d+)\s+.+(\d)\s+.+(\d)", line).groups()
    i = int(i)
    items = list(map(int, items.split(",")))

    if operation == "*":
        operation = lambda x, y: x * y
    else:
        operation = lambda x, y: x + y
    
    monkeys[i] = {"items": items, "operation": operation, "constant": constant, "test": int(test), "true": int(true), "false": int(false), "inspections": 0}

def play(iterations, worry):
    global monkeys
    for _ in range(iterations):
        for monkey in monkeys.values():
            for _ in range(len(monkey["items"])):
                item = monkey["items"].pop(0)
                monkey["inspections"] += 1
                if monkey["constant"] == "old":
                    new = monkey["operation"](item, item)
                else:
                    new = monkey["operation"](item, int(monkey["constant"]))
                
                if not worry:
                    new = math.floor(new/3)
                
                new = new % 9699690
                
                if new % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(new)
                else: 
                    monkeys[monkey["false"]]["items"].append(new)

    inspections = []
    for monkey in monkeys.values():
        inspections.append(monkey["inspections"])
   
    inspections.sort()
    return inspections[-2]*inspections[-1]

#print("Part1:", play(20, False))
print("Part2", play(10000, True))




