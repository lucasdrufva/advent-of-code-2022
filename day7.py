# Aoc 2022 - Day 7

from utils import get_data
import re

lines = get_data(7).split("\n")

tree = {"/": {}}

current_path = []

def add_to_tree(path, key, value):
    global tree

    pos = tree

    for d in path:
        pos = pos[d]

    pos[key] = value


for line in lines:
    if match := re.match(r"\$ cd (.+)", line):
        # cd command
        if(match.group(1) == ".."):
            current_path.pop()
        else:
            current_path.append(match.group(1))
    
    if match := re.match(r"dir (.+)", line):
        # Directory
        add_to_tree(current_path, match.group(1), {})


    if match := re.match(r"(\d+) (.+)", line):
        # File
        add_to_tree(current_path, match.group(2), int(match.group(1)))
 

def traverse(node, search):
    size = 0

    for n in node.values():
        if isinstance(n, dict):
            size += traverse(n, search)
        else:
            size += n

    search(size)

    return size


small_folders = []
total = traverse(tree, lambda size: small_folders.append(size) if size <= 100000 else None)

print("Part 1:")
print(sum(small_folders))

big_folders = []
space_to_free = 30000000-(70000000-total)
traverse(tree, lambda size: big_folders.append(size) if size >= space_to_free else None)
big_folders.sort()

print("Part 2:")
print(big_folders[0])
        
