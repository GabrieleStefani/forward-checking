# Forward Checking

### Requirements

The code has been written with python 3.8.1, use at least python 3

## Testing

To run the test execute the files that end with `test.py`
The name of the files should be self descriptive

## Console

If you want you can use the python shell like this:

```
>>> import csp
>>> problem = csp.NQueens(8)
>>> solution = csp.backtracking_search(problem)
>>> csp.NQueens.diplay(solution)
>>> csp.NQueens.display(solution)
Q - . - . - . -
- . - . Q . - .
. - . - . - . Q
- . - . - Q - .
. - Q - . - . -
- . - . - . Q .
. Q . - . - . -
- . - Q - . - .
```
