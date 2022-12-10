# Aoc 2022 - Day 10
import math
from utils import get_data

lines = get_data(9).strip().split("\n")

def generate_rope(length):
    rope = []
    for i in range(length):
        rope.append((0,0))

    return rope

# Set to 2 for part 1 and 10 for part 2
rope = generate_rope(10)

visited = set()

for line in lines:
    d, a = line.split(" ")
    a = int(a)

    hx = rope[0][0]
    hy = rope[0][1]

    for _ in range(a):
        if d == "R":
            hx += 1
        elif d == "L":
            hx -= 1
        elif d == "U":
            hy += 1
        elif d == "D":
            hy -= 1

        rope[0] = (hx, hy)

        # Update rest of rope
        for i in range(1, len(rope)):
            dx = rope[i-1][0]-rope[i][0]
            dy = rope[i-1][1]-rope[i][1]

            tx = rope[i][0]
            ty = rope[i][1]

            if abs(dx) > 1 or abs(dy) > 1:
                tx += math.ceil(dx/2) if dx > 0 else math.floor(dx/2)
                ty += math.ceil(dy/2) if dy > 0 else math.floor(dy/2)

            rope[i] = (tx, ty)

        visited.add(rope[-1])

print(len(visited))

