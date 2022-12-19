# Aoc 2022 - Day 19

from utils import get_data

import re

lines = get_data(19).strip().split("\n")

blueprints ={}

for line in lines:
    b_id, ore_robot_cost, clay_robot_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost  = map(int, re.search(r"\s(\d+):.+\s(\d+) ore.+\s(\d+).+\s(\d+).+\s(\d+).+\s(\d+).+\s(\d+)", line).groups())
    blueprints[b_id] = (ore_robot_cost, clay_robot_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost)


def run(b_id, time):
    frontier = set()
    frontier.add((0,0,0,0,1,0,0,0))
    max_geode = 0
    for t in range(time):
        #print("T", t, len(frontier))
        #print(frontier)
        new_frontier = set()
        max_geode = 0
        for state in frontier:
            #if t==11 and state[0] == 2 and state[1]== 4 and state[2] == 0 and state[3] == 0:
            #    print("Found", state)
            ore = state[0] + state[4]
            clay = state[1] + state[5]
            obsidian = state[2] + state[6]
            geode = state[3] + state[7]
            if geode > max_geode:
                #print("New max")
                #print(state)
                max_geode = geode

            if state[0] >= blueprints[b_id][4] and state[2] >= blueprints[b_id][5]:
                new_frontier.add((ore-blueprints[b_id][4] , clay, obsidian-blueprints[b_id][5], geode, state[4], state[5], state[6], state[7]+1))
            else:
                if state[0] >= blueprints[b_id][2] and state[1] >= blueprints[b_id][3]:
                    new_frontier.add((ore-blueprints[b_id][2], clay-blueprints[b_id][3], obsidian, geode, state[4], state[5], state[6]+1, state[7]))

                if state[0] >= blueprints[b_id][1]:
                    new_frontier.add((ore-blueprints[b_id][1], clay, obsidian, geode, state[4], state[5]+1, state[6], state[7]))

                if state[0] >= blueprints[b_id][0] and state[4] < 4:
                    new_frontier.add((ore-blueprints[b_id][0], clay, obsidian, geode, state[4]+1, state[5], state[6], state[7]))

                if state[0] < 5:
                    new_frontier.add((ore, clay, obsidian, geode, state[4], state[5], state[6], state[7]))

        frontier = set()
        if t < (time-2):
            for state in new_frontier:
                if state[3]+(state[7]*(time-1-t)) >= max_geode:
                    frontier.add(state)

        else:
            frontier = new_frontier

    return max_geode


part1 = 0
for i in blueprints.keys():
    part1 += i*run(i, 24)

print("Part 1:", part1)
print("Part 2:", run(1, 32) * run(2, 32) * run(3, 32))

