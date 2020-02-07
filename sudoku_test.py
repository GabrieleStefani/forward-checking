from csp import Sudoku, backtracking_search

hard = '417369805030000000000700000020000060000080400000010000000603070500200000104000000'
easy = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

prob = Sudoku(easy)
Sudoku.display(backtracking_search(prob))
