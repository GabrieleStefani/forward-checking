from csp import Sudoku, backtracking_search

hard = '417369805030000000000700000020000060000080400000010000000603070500200000104000000'
easy = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'

prob = Sudoku(easy)
Sudoku.display(backtracking_search(prob))