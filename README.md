# Forward Checking

## Description

This code can solve 3 problems:

- Map coloring
- Sudoku
- NQueens

It "models" the three problems as binary CSP and use backtracking search with forward checking inference to solve them. There are better solvers for these kinds of problems. If you want to solve more difficult problems this solver is not that efficient.

## Requirements

The code has been written with python `3.8.1`.

## Testing

To run the test execute the files that end with `_test.py`. The name of the files should be self descriptive.

### Example

Assuming `python` is python 3

```
$ python sudoku_test.py
4 8 3 | 9 6 7 | 2 5 1 |
9 2 1 | 3 4 5 | 8 7 6 |
6 5 7 | 8 2 1 | 4 9 3 |
------+-------+-------+
5 4 8 | 7 2 9 | 1 3 6 |
1 3 2 | 5 6 4 | 7 9 8 |
9 7 6 | 1 3 8 | 2 4 5 |
------+-------+-------+
3 7 2 | 8 1 4 | 6 9 5 |
6 8 9 | 2 5 3 | 4 1 7 |
5 1 4 | 7 6 9 | 3 8 2 |
------+-------+-------+
$ python sudoku_fail_test.py
Failed!
```

## Python Shell

If you want you can use the python shell like this:

```
>>> ...
>>> import csp
>>> problem = csp.NQueens(8)
>>> solution = csp.backtracking_search(problem)
>>> csp.NQueens.display(solution)
Q - . - . - . -
- . - . Q . - .
. - . - . - . Q
- . - . - Q - .
. - Q - . - . -
- . - . - . Q .
. Q . - . - . -
- . - Q - . - .
>>> ...
```

## References

The code comes from a very far galaxy, but this link should help you reach it -> https://github.com/aimacode/aima-python
