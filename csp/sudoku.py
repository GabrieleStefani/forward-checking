from csp import CSP
import itertools
import re
from functools import reduce


def flatten(seqs):
    return sum(seqs, [])


# list(range(3))
# _CELL = itertools.count().__next__
# [[[[_CELL() for x in _R3] for y in _R3] for bx in _R3] for by in _R3]
# flatten([list(map(flatten, brow)) for brow in _BGRID])
# flatten([list(map(flatten, zip(*brow))) for brow in _BGRID])
# list(zip(*_ROWS))
_BGRID = [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[9, 10, 11], [12, 13, 14], [15, 16, 17]], [[18, 19, 20], [21, 22, 23], [24, 25, 26]]], [[[27, 28, 29], [30, 31, 32], [33, 34, 35]], [[36, 37, 38], [39, 40, 41], [42, 43, 44]], [[45, 46, 47], [
    48, 49, 50], [51, 52, 53]]], [[[54, 55, 56], [57, 58, 59], [60, 61, 62]], [[63, 64, 65], [66, 67, 68], [69, 70, 71]], [[72, 73, 74], [75, 76, 77], [78, 79, 80]]]]
_BOXES = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43, 44], [
    45, 46, 47, 48, 49, 50, 51, 52, 53], [54, 55, 56, 57, 58, 59, 60, 61, 62], [63, 64, 65, 66, 67, 68, 69, 70, 71], [72, 73, 74, 75, 76, 77, 78, 79, 80]]
_ROWS = [[0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23], [6, 7, 8, 15, 16, 17, 24, 25, 26], [27, 28, 29, 36, 37, 38, 45, 46, 47], [30, 31, 32, 39, 40, 41, 48, 49, 50], [33, 34, 35,
                                                                                                                                                                                              42, 43, 44, 51, 52, 53], [54, 55, 56, 63, 64, 65, 72, 73, 74], [57, 58, 59, 66, 67, 68, 75, 76, 77], [60, 61, 62, 69, 70, 71, 78, 79, 80]]
_COLS = [(0, 3, 6, 27, 30, 33, 54, 57, 60), (1, 4, 7, 28, 31, 34, 55, 58, 61), (2, 5, 8, 29, 32, 35, 56, 59, 62), (9, 12, 15, 36, 39, 42, 63, 66, 69), (10, 13, 16, 37, 40, 43, 64,
                                                                                                                                                        67, 70), (11, 14, 17, 38, 41, 44, 65, 68, 71), (18, 21, 24, 45, 48, 51, 72, 75, 78), (19, 22, 25, 46, 49, 52, 73, 76, 79), (20, 23, 26, 47, 50, 53, 74, 77, 80)]

_NEIGHBORS = {v: set() for v in flatten(_ROWS)}
for unit in map(set, _BOXES + _ROWS + _COLS):
    for v in unit:
        _NEIGHBORS[v].update(unit - {v})


class Sudoku(CSP):
    """
    A Sudoku problem.
    The box grid is a 3x3 array of boxes, each a 3x3 array of cells.
    Each cell holds a digit in 1..9. In each box, all digits are
    different; the same for each row and column as a 9x9 grid.
    """
    rows = _ROWS
    bgrid = _BGRID
    neighbors = _NEIGHBORS

    def __init__(self, grid):
        """Build a Sudoku problem from a string representing the grid:
        the digits 1-9 denote a filled cell, '.' or '0' an empty one;
        other characters are ignored."""
        squares = iter(re.findall(r'\d|\.', grid))
        domains = {var: [ch] if ch in '123456789' else '123456789'
                   for var, ch in zip(flatten(self.rows), squares)}
        for _ in squares:
            raise ValueError("Not a Sudoku grid", grid)  # Too many squares

        def different_values_constraint(A, a, B, b):
            """A constraint saying two neighboring variables must differ in value."""
            return a != b
        CSP.__init__(self, None, domains, self.neighbors,
                     different_values_constraint)

    def display(assignment):
        if assignment != None:
            for brow in _BGRID:
                for box in brow:
                    for row in box:
                        for cell in row:
                            print(assignment[cell], end=' ')
                        print('|', end=' ')
                    print()
                print("------+-------+--------")
        else:
            print("Failed!")
