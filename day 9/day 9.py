import sys, os
sys.path.append(os.getcwd())
from aoc_utils.input_handling import read_from_file

#
# Classes
#
class Disk:
    def __init__(self, init_string: str) -> None:
        self.blocks = []
        file_id = 0
        for i, c in enumerate(init_string.strip()):
            if i % 2 == 0:
                self.blocks += [ file_id ] * int(c)
                file_id += 1
            else: self.blocks += [ None ] * int(c)

    def __repr__(self) -> str:
        return "".join([str(c) if c is not None else "." for c in self.blocks])

    def move_blocks(self) -> str:
        start = 0
        end = len(self.blocks) - 1

        while True:
            while self.blocks[start] is not None: start += 1
            if start >= end: break
            self.blocks[start], self.blocks[end] = self.blocks[end], self.blocks[start]
            end -= 1

    def get_checksum(self) -> int:
        return sum([ i * c if c is not None else 0 for i, c in enumerate(self.blocks)] )

#
# Process input
#
disk_string = read_from_file('day 9/input2.txt')

#
# Puzzle 1
#
disk = Disk(disk_string)
disk.move_blocks()
print(f'Puzzle 1 solution is: {disk.get_checksum()}')

#
# Puzzle 2
#
disk = Disk(disk_string)
