from csp import Sudoku, backtracking_search
import time

easy = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
medium = '000012300000400000401005600705000010600020007030000806003600109000001000006590000'
hard = '417369805030000000000700000020000060000080400000010000000603070500200000104000000'

for grid in [easy, medium, hard]:
    prob = Sudoku(grid)
    start = time.time()
    Sudoku.display(backtracking_search(prob))
    print(f"Blank cell = {grid.count('0')}")
    print(f"Time to execute: {(time.time()-start)*1000:.2f}ms")
    print()
