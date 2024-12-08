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
            if c == '^': self.start_pos = self.pos = pos

    def walk(self) -> int:
        while True:
            self.explored.add(self.pos)
            if self.pos + self.dir not in self.tiles: break
            if self.tiles[self.pos + self.dir] == '#': self.dir *= 1j
            else: self.pos += self.dir

        return len(self.explored)

    def test_loop(self, obstruction_pos: complex) -> bool:
        pos = self.start_pos
        dir = -1j
        explored = { 1: set(), -1: set(), 1j: set(), -1j: set() }
        while True:
            explored[dir].add(pos)
            if pos + dir not in self.tiles: return False
            if self.tiles[pos + dir] == '#' or pos + dir == obstruction_pos: dir *= 1j
            else:
                pos += dir
                if pos in explored[dir]: return True

    def find_loops(self) -> int:
        loop_count = 0
        for obstruction_pos in self.explored - {self.start_pos}:
            loop_count += 1 if self.test_loop(obstruction_pos) else 0
        return loop_count

#
# Process input
#
guardmap = read_from_file('day 6/input.txt', GuardMap)

#
# Puzzle 1
# 
print(f'Puzzle 1 solution is: {guardmap.walk()}')

#
# Puzzle 2
#
print(f'Puzzle 2 solution is: {guardmap.find_loops()}')