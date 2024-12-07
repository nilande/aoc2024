import sys, os
sys.path.append(os.getcwd())
from aoc_utils.input_handling import read_from_file
import re

#
# Process input
#
input = read_from_file('day 3/input.txt')

#
# Puzzle 1
#
matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input)

print(f'Puzzle 1 solution is: {sum(int(a) * int(b) for a, b in matches)}')

#
# Puzzle 2
#
# Remove all inactivated sections (non-greedy)
input = re.sub(r'don\'t\(\).*?do\(\)', '', input, flags=re.DOTALL)
# Remove any final inactivated sections
input = re.sub(r'don\'t\(\).*', '', input, flags=re.DOTALL)
matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input)

print(f'Puzzle 2 solution is: {sum(int(a) * int(b) for a, b in matches)}')