import itertools
import csp


def main():
    variables = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    domains = {}
    neighbors = {}
    for var in variables:
        domains.update({var: [0, 1, 2, 3, 4, 5]})
        neighborsOfVar=[]
        if var-1 >= 0:
            neighborsOfVar.append(var-1)
        if(var+1 < 10):
            neighborsOfVar.append(var+1)
        neighbors.update({var: neighborsOfVar})
    maxNumberOfClasses = [1, 1, 2, 2, 2, 2]

    def constraint(A, a, B, b, assignment):
        maxNumberOfClasses = [1, 1, 2, 2, 2, 2]
        maxNumberOfClasses[b]-=1
        for key, value in assignment.items():
            maxNumberOfClasses[value]-=1
            print(maxNumberOfClasses)
            if maxNumberOfClasses[value] < 0:
                return False
        classes = {0: [1, 0, 1, 1, 0],
                   1: [0, 0, 0, 1, 0],
                   2: [0, 1, 0, 0, 1],
                   3: [0, 1, 0, 1, 0],
                   4: [1, 0, 1, 0, 0],
                   5: [1, 1, 0, 0, 0]}
        blocks = [1, 2, 1, 2, 1]
        isOk = True
        for i in range(5):
            if classes[a][i] + classes[b][i] > blocks[i]:
                isOk = False
        return isOk
    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
