# Aoc 2022 - Day 6

from utils import get_data

data = get_data(6)

def find_end_of_unique_string_of_length(length, text):
    for i in range(len(text)):
        if len(set(text[i:i+length])) == length:
            return i+length

print("Part 1: ", find_end_of_unique_string_of_length(4, data))
print("Part 2: ", find_end_of_unique_string_of_length(14, data))

