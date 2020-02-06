import numpy as np
import math
import csp


def main():
    variables = []
    domains = {}
    neighbors = {}

    def constraint(A, a, B, b):
        return A == B or (a != b and A + a != B + b and A - a != B - b)

    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
