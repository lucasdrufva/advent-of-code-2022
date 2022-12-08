# Aoc 2022 - Day 8

from utils import get_data

lines = get_data(8).strip().split("\n")

grid = [[int(j) for j in list(i)] for i in lines]

def calc_visible(x, y):
    height = grid[x][y]

    up = [grid[i][y] for i in range(x)[::-1]]
    up_score = next((i+1 for i in range(len(up)) if up[i] >= height), len(up))

    down = [grid[i][y] for i in range(x+1, len(grid))]
    down_score = next((i+1 for i in range(len(down)) if down[i] >= height), len(down))

    left = [grid[x][j] for j in range(y+1, len(grid[x]))]
    left_score = next((i+1 for i in range(len(left)) if left[i] >= height), len(left))

    right = [grid[x][j] for j in range(y)[::-1]]
    right_score = next((i+1 for i in range(len(right)) if right[i] >= height), len(right))

    visible = all([h < height for h in up]) or all([h < height for h in down]) or all([h < height for h in left]) or all([h < height for h in right])
    score = up_score * down_score * left_score * right_score

    return visible, score

count_visible = 0
max_score = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        visible, score = calc_visible(i, j)

        if visible:
            count_visible += 1

        if score > max_score:
            max_score = score

print("Part 1: ", count_visible)
print("Part 2: ", max_score)

