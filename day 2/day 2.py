import sys, os
sys.path.append(os.getcwd())
from aoc_utils.input_handling import read_lines_from_file

#
# Process input
#
reports = read_lines_from_file('day 2/input.txt', lambda x: list(map(int, x.split())))

#
# Functions
#
def is_safe(report):
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False

    if all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1)):
       return True

#
# Puzzle 1
#
acc = 0
for report in reports:
    if is_safe(report): acc += 1

print(f'Puzzle 1 solution is: {acc}')

#
# Puzzle 2
#
acc = 0
for report in reports:
    for i in range(len(report)):
        report_copy = report[:i] + report[i+1:]
        if is_safe(report_copy):
            acc += 1
            break

print(f'Puzzle 2 solution is: {acc}')