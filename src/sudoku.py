import numpy as np
import math
import csp


def main():
    variables = []
    domains = {}
    neighbors = {}

    sudoku = list(
        "004300209005009001070060043006002087190007400050083000600000105003508690042910300")
    for var in range(len(sudoku)):
        variables.append(var)
        if int(sudoku[var]) != 0:
            domains[var] = [int(sudoku[var])]
        else:
            domains[var] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        neighbors[var] = []
        x = int(var / 9)
        y = var % 9
        for otherVar in range(len(sudoku)):
            x1 = int(otherVar/9)
            y1 = otherVar % 9
            """ print(var, otherVar, x, y, x1, y1, math.ceil(x/3) == math.ceil(x1/3)
                  and math.ceil(y/3) == math.ceil(y1/3)) """
            if x == x1 or y == y1 or (int(x/3) == int(x1/3)
                                      and int(y/3) == int(y1/3)):
                neighbors[var].append(otherVar)

    def constraint(A, a, B, b):
        return a != b
    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
