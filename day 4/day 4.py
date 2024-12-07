import sys, os
sys.path.append(os.getcwd())
from aoc_utils.input_handling import read_from_file

#
# Classes
#
class WordSearch:
    ALL_DIRECTIONS = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]

    def __init__(self, search_string: str) -> None:
        width = search_string.find('\n') + 1
        self.tiles = {}
        for i, c in enumerate(search_string):
            if c == '\n': continue
            pos = i%width + i//width*1j
            self.tiles[pos] = c

    def search_pos_dir(self, string: str, pos: complex, dir: complex) -> bool:
        if pos in self.tiles and self.tiles[pos] == string[0]:
            if len(string) == 1: return True
            else: return self.search_pos_dir(string[1:], pos+dir, dir)
        return False
        
    def search_all_xmas(self, string: str) -> int:
        matches = 0
        for pos in self.tiles.keys():
            for dir in WordSearch.ALL_DIRECTIONS:
                matches += 1 if self.search_pos_dir(string, pos, dir) else 0
        
        return matches
    
    def search_all_x_mas(self) -> int:
        matches = 0
        for pos in self.tiles.keys():
            if pos+1+1j not in self.tiles or pos-1-1j not in self.tiles: continue
            if self.tiles[pos] != 'A': continue
            if self.tiles[pos+1+1j] == 'M' and self.tiles[pos-1-1j] == 'S' and self.tiles[pos+1-1j] == 'M' and self.tiles[pos-1+1j] == 'S': matches += 1
            elif self.tiles[pos+1+1j] == 'S' and self.tiles[pos-1-1j] == 'M' and self.tiles[pos+1-1j] == 'M' and self.tiles[pos-1+1j] == 'S': matches += 1
            elif self.tiles[pos+1+1j] == 'M' and self.tiles[pos-1-1j] == 'S' and self.tiles[pos+1-1j] == 'S' and self.tiles[pos-1+1j] == 'M': matches += 1
            elif self.tiles[pos+1+1j] == 'S' and self.tiles[pos-1-1j] == 'M' and self.tiles[pos+1-1j] == 'S' and self.tiles[pos-1+1j] == 'M': matches += 1

        return matches


#
# Process input
#
wordsearch = read_from_file('day 4/input.txt', WordSearch)

#
# Puzzle 1
#
print(f'Puzzle 1 solution is: {wordsearch.search_all_xmas('XMAS')}')

#
# Puzzle 2
#
print(f'Puzzle 1 solution is: {wordsearch.search_all_x_mas()}')
