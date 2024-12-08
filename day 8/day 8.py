import sys, os
sys.path.append(os.getcwd())
from aoc_utils.input_handling import read_from_file
import itertools

#
# Classes
#
class AntennaMap:
    def __init__(self, map_string: str) -> None:
        width = map_string.find('\n') + 1
        self.tiles = set()
        self.frequencies = {}
        for i, c in enumerate(map_string):
            pos = i%width + i//width*1j
            match c:
                case '\n': continue
                case '.': 
                    self.tiles.add(pos)
                case _:
                    self.tiles.add(pos)
                    self.frequencies.setdefault(c, set())
                    self.frequencies[c].add(pos)

    def get_antinodes(self) -> set:
        antinodes = set()
        for antennas in self.frequencies.values():
            for a, b in itertools.combinations(antennas, 2):
                if 2*b-a in self.tiles: antinodes.add(2*b-a)
                if 2*a-b in self.tiles: antinodes.add(2*a-b)
        return antinodes
    
    def get_harmonics_antinodes(self) -> set:
        antinodes = set()
        for antennas in self.frequencies.values():
            for a, b in itertools.combinations(antennas, 2):
                # NOTE: We should potentially check GCD(step.imag, step.real) but it seems not to be needed for the puzzle input
                step = b-a
                pos = a
                while pos in self.tiles:
                    antinodes.add(pos)
                    pos += step
                pos = a
                while pos in self.tiles:
                    antinodes.add(pos)
                    pos -= step

        return antinodes

#
# Process input
#
antennamap = read_from_file('day 8/input.txt', AntennaMap)

#
# Puzzle 1
#
print(f'Puzzle 1 solution is: {len(antennamap.get_antinodes())}')

#
# Puzzle 2
#
print(f'Puzzle 2 solution is: {len(antennamap.get_harmonics_antinodes())}')