import sys, os
sys.path.append(os.getcwd())
from aoc_utils.input_handling import read_lines_from_file

#
# Process input
#
lines = read_lines_from_file('day 1/input.txt', lambda x: map(int, x.split()))
left, right = map(sorted, zip(*lines))

#
# Puzzle 1
#
acc = 0
for l, r in zip(left, right):
    acc += abs(r - l)

print(f'Puzzle 1 solution is: {acc}')

#
# Puzzle 2
#
acc = 0
for l in left:
    acc += sum([r for r in right if r == l])

print(f'Puzzle 2 solution is: {acc}')