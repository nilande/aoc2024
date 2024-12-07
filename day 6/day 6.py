import sys, os
sys.path.append(os.getcwd())
from aoc_utils.input_handling import read_from_file

#
# Classes
#
class GuardMap:
    def __init__(self, map_string: str) -> None:
        width = map_string.find('\n') + 1
        self.tiles = {}
        self.explored = set()
        self.dir = -1j
        for i, c in enumerate(map_string):
            if c == '\n': continue
            pos = i%width + i//width*1j
            self.tiles[pos] = c
            if c == '^': self.pos = pos

    def walk(self) -> int:
        while True:
            self.explored.add(self.pos)
            if self.pos + self.dir not in self.tiles: break
            if self.tiles[self.pos + self.dir] == '#': self.dir *= 1j
            else: self.pos += self.dir

        return len(self.explored)

#
# Process input
#
guardmap = read_from_file('day 6/input.txt', GuardMap)

#
# Puzzle 1
# 
print(f'Puzzle 1 solution is: {guardmap.walk()}')