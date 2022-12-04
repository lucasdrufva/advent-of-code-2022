# Aoc 2022 - Day X

from utils import get_data

#regex
import re

# a, b = re.search(r"([a-z]+).([a-z]+)", target_string).groups(1,2)

lines = get_data(4).split("\n")

#mapped to ints
#nums = list(map(int, lines))

part1 = 0
part2 = 0

for line in lines:
    a, b, c, d = map(int, re.search(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups())
   
    if(a <= c and b >= d):
        part2 += 1
        part1 += 1
    elif(a >= c and b<=d):
        part2 += 1
        part1 += 1
    elif(a <= c and b >= c or a <= d and b >= d):
        part2 += 1


print("Part 1: ", part1)
print("Part 2: ", part2)
    

