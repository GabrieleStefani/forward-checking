import csv
import csp


def main():
    variables = []
    domains = {}
    neighbors = {}


with open('sudoku.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for elem in row:

    def constraint(A, a, B, b):
        return True

    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
