from csp import Sudoku, backtracking_search

impossible1 = '003020600900305001001806400008102900700000008006708200002609511800203009005010300'

prob = Sudoku(impossible1)
print(backtracking_search(prob))
