# Aoc 2022 - Day 25

from utils import get_data

import math

lines = get_data(25).strip().split("\n")

sums = 0

for line in lines:
    tal = 0
    for i, c in enumerate(line[::-1]):
        if c == "2":
            tal += 5**i * 2
        elif c == "1":
            tal += 5**i
        elif c == "-":
            tal += 5**i * -1
        elif c == "=":
            tal += 5**i * -2
    
    sums += tal

tal = []

for i in range(19, -1, -1):
    if sums / (5**i) >= 1:
        n = math.floor(sums / (5**i) )
        tal.append(n)
        sums -= n * (5**i)
    elif len(tal) > 0:
        tal.append(0)

tal = tal[::-1]

def calc_val(t):
    s = 0
    for i in range(len(t)):
        s += t[i] * (5**i)

    return s

val = calc_val(tal)

for i in range(len(tal)):
    if tal[i] > 2:
        tal[i+1] += 1
        new_val = calc_val(tal)
        j = 0
        while val != new_val:
            if tal[i-j] > -2:
                tal[i-j] -= 1
            else:
                j += 1

            new_val = calc_val(tal)

i_to_SNAFU = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}

answer = ''.join(map(lambda x: i_to_SNAFU[x], tal[::-1]))

print("Part 1:", answer)
