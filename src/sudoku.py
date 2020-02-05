import numpy as np
import csp


def main():
    variables = []
    domains = {}
    neighbors = {}

    sudoku = list(
        "004300209005009001070060043006002087190007400050083000600000105003508690042910300")
    for var in len(sudoku):
        variables.append(var)
        if var != 0:
            domains[var] = [sudoku[var]]
        neighbors[var] = []

    def constraint(A, a, B, b):
        return True

    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
