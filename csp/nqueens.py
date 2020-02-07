from csp import CSP, UniversalDict


def queen_constraint(A, a, B, b):
    """Constraint is satisfied (true) if A, B are really the same variable,
    or if they are not in the same row, down diagonal, or up diagonal.
    Go here to see why -> http://www.csplib.org/Problems/prob054/
    The position of the first queen is (A, a), the second is (B, b).
    """
    return A == B or (a != b and A + a != B + b and A - a != B - b)


class NQueens(CSP):
    """
    Make a CSP for the nQueens problem.
    Suitable for large n, it uses only data structures of size O(n).
    Think of placing queens one per column, from left to right.
    That means position (x, y) represents (var, val) in the CSP.
    """

    def __init__(self, n):
        """Initialize data structures for n Queens.
        As we are choosing only the y coordinate of every queen the 
        domain and the neighbors are list(range(n)) for every column
        (alias variable)
        """
        CSP.__init__(self, list(range(n)), UniversalDict(list(range(n))),
                     UniversalDict(list(range(n))), queen_constraint)

    def display(assignment):
        """Print the queens"""
        if assignment != None:
            n = len(assignment)
            for var in range(n):
                for val in range(n):
                    if assignment[var] == val:
                        ch = 'Q'
                    elif (var + val) % 2 == 0:
                        ch = '.'
                    else:
                        ch = '-'
                    print(ch, end=' ')
                print()
        else:
            print("Failed!")
