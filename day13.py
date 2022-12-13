# Aoc 2022 - Day 13

from utils import get_data

pairs = get_data(13).strip().split("\n\n")

def compare(a, b):
    if type(a) is int and type(b) is int:
        return b-a

    if type(a) is list and type(b) is list:
        rv = 0
        for i in range(min(len(a), len(b))):
            if compare(a[i], b[i]) != 0:
                return compare(a[i], b[i])

        return len(b)-len(a)
    
    if type(a) is int and type(b) is list:
        return compare([a], b)
    if type(a) is list and type(b) is int:
        return compare(a, [b])
              
                
part1 = 0 
all_packets = [[[2]], [[6]]]

for i, pair in enumerate(pairs):
    a, b = pair.split("\n")
    a = eval(a)
    b = eval(b)
    if compare(a,b) > 0:
        part1 += i+1

    all_packets.append(a)
    all_packets.append(b)

print("Part1:", part1)

from functools import cmp_to_key
ordered_packets = sorted(all_packets, key=cmp_to_key(compare))
ordered_packets.reverse()

divider_index = None
for i, packet in enumerate(ordered_packets):
    if packet == [[2]] or packet == [[6]]:
        if divider_index == None:
            divider_index = i+1
        else:
            print("Part 2:", (i+1)*divider_index)
            break


