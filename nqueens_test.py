from csp import NQueens, backtracking_search
import time

for n in [4, 8, 12, 16, 20]:
    prob = NQueens(n)
    start = time.time()
    NQueens.display(backtracking_search(prob))
    print(f"n = {n}")
    print(f"Time to execute: {(time.time()-start)*1000:.2f}ms")
    print()
