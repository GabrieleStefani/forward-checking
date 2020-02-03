import itertools
import csp


def main():
    variables = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "TOT"]
    domains = {}
    neighbors = {}
    for var in variables:
        domains.update({var: [0, 1, 2, 3, 4, 5]})
        if(var != "TOT"):
            neighborsOfVar = []
            if var-1 >= 0:
                neighborsOfVar.append(var-1)
            if(var+1 < 10):
                neighborsOfVar.append(var+1)
            neighbors.update({var: neighborsOfVar})
        else:
            domains.update({var: [1, 1, 2, 2, 2, 2])})
            neighbors.update({"TOT": range(10)})
    maxNumberOfClasses=[1, 1, 2, 2, 2, 2]

    def constraint(A, a, B, b):
        classes={0: [1, 0, 1, 1, 0],
                   1: [0, 0, 0, 1, 0],
                   2: [0, 1, 0, 0, 1],
                   3: [0, 1, 0, 1, 0],
                   4: [1, 0, 1, 0, 0],
                   5: [1, 1, 0, 0, 0]}
        blocks = [1, 2, 1, 2, 1]
        if A == "TOT":
            return a[B] == b
        elif B == "TOT":
            return b[A] == a
        else:
            isOk = True
            for i in range(5):
                if classes[a][i] + classes[b][i] > blocks[i]:
                    isOk = False
            return isOk
    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
