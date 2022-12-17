# Aoc 2022 - Day 17

from utils import get_data
from collections import defaultdict

input_moves = list(get_data(17).strip())


class Rock:
    def __init__(self, rock_type, x, y):
        self.rock_type = rock_type
        self.x = x
        self.y = y

    def get_shape_start(self):
        if self.rock_type == 0:
            return (0,0)
        elif self.rock_type == 1:
            return (0, 2)
        elif self.rock_type == 2:
            return (0, 2)
        elif self.rock_type == 3:
            return (0, 3)
        elif self.rock_type == 4:
            return (0, 1)

    def get_shape(self):
        if self.rock_type == 0:
            return {(0,0): 1, (1,0): 1, (2, 0): 1, (3, 0): 1}
        elif self.rock_type == 1:
            return {(1,0): 1, (0, 1): 1, (1,1): 1, (2, 1): 1, (1, 2): 1}
        elif self.rock_type == 2:
            return {(2, 0): 1, (2, 1): 1, (0, 2): 1, (1, 2): 1, (2,2): 1}
        elif self.rock_type == 3:
            return {(0,0): 1, (0,1): 1, (0,2): 1, (0,3): 1}
        elif self.rock_type == 4:
            return {(0,0): 1, (1, 0): 1, (0,1): 1, (1,1): 1}

    def get_real_shape_coords(self):
        real = []
        sx, sy = self.get_shape_start()
        rx = self.x
        ry = self.y
        for kx, ky in self.get_shape().keys():
            real.append((rx+kx, ry+(sy-ky)))

        return real

    def can_move(self, dx, dy, grid):
        sx, sy = self.get_shape_start()
        rx = self.x
        ry = self.y
        for kx, ky in self.get_shape().keys():
            if get_grid((rx+kx+dx, ry+(sy-ky)+dy)) == 1:
                return False
        
        return True



grid = {}

def get_grid(key):
    global grid
    if key not in grid:
        return 0 if key[0] < 7 and key[0] >= 0 and key[1] >= 0 else 1
    else:
        return grid[key]

def print_grid(height):
    for i in range(height, -1, -1):
        for j in range(7):
            if get_grid((j, i)) == 1:
                print("#",end = '')
            else:
                print(".",end = '')
        print("")


def lines_as_string(stop, start):
    lines = ""
    for i in range(stop, start-1, -1):
        for j in range(7):
            if get_grid((j, i)) == 1:
                lines += "#"
                #print("#",end = '')
            else:
                lines += "."
                #print(".",end = '')
        #print("")
        lines += "\n"

    return lines

import math

move_index = 0
shape_index = 0
height = 0
rock_n = 0

def place_rocks_until(rock_count, detect_loops=False, search_pattern=None):
    global move_index
    global shape_index
    global height
    global rock_n

    if detect_loops:
        first_repeting_rock = None
        first_repeting_height = None
    
    extra_height = 0

    while rock_n < rock_count:
        moving = True

        #Generate new shape:
        rock = Rock(shape_index, 2, 3+height)
        shape_index += 1
        shape_index = shape_index % 5
    
        while moving:
            if input_moves[move_index] == ">":
                dx = 1
            else:
                dx = -1

            move_index += 1
            move_index = move_index % len(input_moves)


            if rock.can_move(dx, 0, grid):
                rock.x += dx
            
            if not rock.can_move(0, -1, grid):
                moving = False
                for cord in rock.get_real_shape_coords():
                    grid[cord] = 1
                    if cord[1]+1 > height:
                        height = cord[1]+1
            else:
                rock.y -= 1

        if detect_loops:
            test_search = lines_as_string(height, height-10)
            if test_search == search_pattern:
                if first_repeting_rock == None:
                    first_repeting_rock = rock_n
                    first_repeting_height = height
                else:
                    height_difference = height-first_repeting_height
                    rock_difference = rock_n-first_repeting_rock

                    cycles_to_skip = math.floor((rock_count-rock_n)/rock_difference)

                    rock_n += cycles_to_skip*rock_difference
                    
                    extra_height = cycles_to_skip*height_difference




        rock_n += 1

    return height + extra_height

print("Part 1:", place_rocks_until(2022))

#Pattern to search for to detect repetition
search = lines_as_string(height, height-10)

print("Part 2:",place_rocks_until(1000000000000, True, search))
