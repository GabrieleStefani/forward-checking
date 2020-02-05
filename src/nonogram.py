import numpy as np
import itertools
import csp


def main():
    rows = [
        [2],
        [2, 1],
        [1, 1],
        [3],
        [1, 1],
        [1, 1],
        [2],
        [1, 1],
        [1, 2],
        [2]
    ]
    columns = [
        [2, 1],
        [2, 1, 3],
        [7],
        [1, 3],
        [2, 1]
    ]

    variables = list(np.arange(len(rows)*len(columns)))
    domains = {}
    neighbors = {}
    for var in variables:
        domains[var] = [0, 1]
        neighbors[var] = [
            f"row-{var % len(columns)}", f"row-{var % len(columns)}"]
    for i in range(len(rows)):
        var = f"row-{i}"
        variables.append(var)
        rowBlocks = []
        for block in rows[i]:
            rowBlocks.append(0)
            rowBlocks.append(block)
        rowBlocks.append(0)
        domains[var] = list(itertools.permutations(rowBlocks))
        neighbors.update(
            {var: np.arange(i*len(rows), i*len(rows) + len(columns))})
    for i in range(len(columns)):
        var = f"column-{i}"
        variables.append(var)
        columnBlocks = []
        for block in columns[i]:
            columnBlocks.append(0)
            columnBlocks.append(block)
        columnBlocks.append(0)
        domains[var] = list(itertools.permutations(columnBlocks))
        domains.update({var: []})
        neighbors.update(
            {var: np.arange(i*len(columns), i*len(columns) + len(rows))})

    print(domains)

    def constraint(A, a, B, b):
        return True
    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
