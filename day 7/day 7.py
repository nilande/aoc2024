import sys, os
sys.path.append(os.getcwd())
from aoc_utils.input_handling import read_lines_from_file

#
# Process input
#
def split_input(input: str) -> tuple:
    result, params = input.split(': ')
    return int(result), tuple(map(int, params.split()))
equations = read_lines_from_file('day 7/input.txt', split_input)

#
# Functions
#
def test_equation(result: int, params: tuple, enable_concat: bool = False) -> bool:
    if len(params) == 1: return True if result == params[0] else False
    if result < 0: return False
    found_solution = False
    if result % params[-1] == 0:
        found_solution = test_equation(result // params[-1], tuple(params[:-1]), enable_concat)
    if not found_solution and enable_concat:
        result_str = str(result)
        param_str = str(params[-1])
        if len(result_str) > len(param_str) and result_str.endswith(param_str):
            new_result = int(result_str[:-len(param_str)])
            found_solution = test_equation(new_result, tuple(params[:-1]), enable_concat)
    if not found_solution:
        found_solution = test_equation(result - params[-1], tuple(params[:-1]), enable_concat)
    return found_solution

#
# Puzzle 1
#
acc = 0
for result, params in equations:
    acc += result if test_equation(result, params) else 0

print(f'Puzzle 1 solution is: {acc}')

#
# Puzzle 2
#
acc = 0
for result, params in equations:
    acc += result if test_equation(result, params, True) else 0

print(f'Puzzle 2 solution is: {acc}')
