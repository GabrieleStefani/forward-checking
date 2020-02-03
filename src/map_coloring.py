import csp


def main():
    variables = ["WA", "NT", "V", "NSW", "Q", "SA", "T"]
    domains = {}
    neighbors = {"WA": ["NT", "SA"],
                 "NT": ["WA", "SA", "Q"],
                 "V": ["SA", "NSW"],
                 "NSW": ["V", "SA", "Q"],
                 "Q": ["NT", "SA", "NSW"],
                 "SA": ["WA", "NT", "V", "NSW", "Q"],
                 "T": []}
    for var in variables:
        domains.update({var: ["r", "g", "b"]})

    def constraint(A, a, B, b):
        return a != b
    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
