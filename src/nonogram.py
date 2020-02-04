import numpy as np
import csp


def main():
    matrix =np.arange(25).reshape(5,5)
    variables = np.arange(25)
    domains = {}
    neighbors = {}
    for row in matrix:
        for var in row:
            neighborsOfVar = []
            domains.update({var: [0, 1]})
            if var-1 >= row[0]:
                neighborsOfVar.append(var-1)
            if var+1 <= row[4]:
                neighborsOfVar.append(var+1)
            if(var+5 < 25):
                neighborsOfVar.append(var+5)
            if(var-5 >= 0):
                neighborsOfVar.append(var-5)
            neighbors.update({var: neighborsOfVar})

    def constraint(A, a, B, b):
        return True
    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
