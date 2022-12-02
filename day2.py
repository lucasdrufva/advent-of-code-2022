# Aoc 2022 - Day 2

from enum import Enum
from utils import get_data

lines = get_data(2).split("\n")

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

class Outcome(Enum):
    LOOSE = 0
    DRAW = 1
    WINN = 2

    def to_score(outcome):
        if outcome == Outcome.LOOSE:
            return 0
        if outcome == Outcome.DRAW:
            return 3
        if outcome == Outcome.WINN:
            return 6

#Who beats who
# Map opponent move to your move
game_map = {
        Move.ROCK: {Move.ROCK: Outcome.DRAW, Move.PAPER: Outcome.WINN, Move.SCISSOR: Outcome.LOOSE },
        Move.PAPER: {Move.ROCK: Outcome.LOOSE, Move.PAPER: Outcome.DRAW, Move.SCISSOR: Outcome.WINN},
        Move.SCISSOR: {Move.ROCK: Outcome.WINN, Move.PAPER: Outcome.LOOSE, Move.SCISSOR: Outcome.DRAW}
        }


def next_move(opponent_move, expected_outcome):
    return next(k for k, v in game_map[opponent_move].items() if v == expected_outcome)

def calculate_score(opponent_move, your_move):
    outcome = game_map[opponent_move][your_move]

    return Outcome.to_score(outcome) + your_move.value

    
part1 = 0
part2 = 0

for line in lines:
    a, b = line.strip().split(" ")
    a = Move(ord(a) - ord("A") + 1)
    b = ord(b)- ord("X")

    part1 += calculate_score(a, Move(b+1))
    part2 += calculate_score(a, next_move(a, Outcome(b)))


print(f"Part 1: {part1}, Part 2: {part2}")

