# Aoc 2022 - Day 14

from utils import get_data

lines = get_data(14).strip().split("\n")

grid = {}
max_y = 0

for line in lines:
    points = []
    for point in line.split(" -> "):
        x,y = map(int, point.split(","))
        points.append((x,y))
        if y > max_y:
            max_y = y

    for i in range(len(points)-1):
        dx = points[i+1][0]-points[i][0]
        dy = points[i+1][1]-points[i][1]

        if dx > 0:
            for j in range(dx+1):
                grid[(points[i][0]+j, points[i][1])] = "#"

        elif dx < 0:
            for j in range(0, dx-1, -1):
                grid[(points[i][0]+j, points[i][1])] = "#"
        
        elif dy > 0:
            for j in range(dy+1):
                grid[(points[i][0], points[i][1]+j)] = "#"

        elif dy < 0:
            for j in range(0, dy-1, -1):
                grid[(points[i][0], points[i][1]+j)] = "#"

# Floor level
max_y += 2

def check_pos_blocked(x,y, floor):
    global grid
    global max_y

    if y >= max_y and floor:
        return True
    
    return (x,y) in grid


# Sand generation
def sand(grid, floor):
    count = 0
    while True:
        sand_x = 500
        sand_y = 0

        # Start falling
        moved = True
        moves = 0
        while moved:
            moved = False
            if not check_pos_blocked(sand_x, sand_y+1, floor):
                sand_y += 1
                moved = True
            elif not check_pos_blocked(sand_x-1, sand_y+1, floor):
                sand_x -= 1
                sand_y += 1
                moved = True
            elif not check_pos_blocked(sand_x+1, sand_y+1, floor):
                sand_x += 1
                sand_y += 1
                moved = True

            moves += 1
            # Moves over 300 probably = falling forever
            if moves > 300 and not floor:
                return count
                
        grid[(sand_x, sand_y)] = "S"
        count += 1

        if sand_x == 500 and sand_y == 0:
            return count


part1 = sand(grid, False)
print("Part 1:", part1)

part2 = part1 + sand(grid, True)
print("Part 2", part2)

        

