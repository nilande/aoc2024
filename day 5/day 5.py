import sys, os
sys.path.append(os.getcwd())
from aoc_utils.input_handling import read_from_file

#
# Process input
#
rules_string, updates_string = read_from_file('day 5/input.txt', lambda x: x.split('\n\n'))

rules = []
for rule_string in rules_string.split('\n'):
    rules.append(tuple(rule_string.split('|')))

#
# Puzzle 1
#
result = 0
for update_string in updates_string.split('\n'):
    if len(update_string) == 0: continue

    pages = tuple(update_string.split(','))
    for l, r in rules:
        if l not in pages or r not in pages: continue
        if pages.index(l) > pages.index(r): break
    else: result += int(pages[len(pages)//2])

print(f'Puzzle 1 solution is: {result}')
    
#
# Puzzle 2
#
new_result = 0
for update_string in updates_string.split('\n'):
    if len(update_string) == 0: continue

    pages = update_string.split(',')
    go_again = True
    while go_again:
        go_again = False

        for l, r in rules:
            if l not in pages or r not in pages: continue
            if pages.index(l) > pages.index(r):
                pages[pages.index(l)], pages[pages.index(r)] = pages[pages.index(r)], pages[pages.index(l)]
                go_again = True
                break
        else: new_result += int(pages[len(pages)//2])

print(f'Puzzle 2 solution is: {new_result - result}')   
