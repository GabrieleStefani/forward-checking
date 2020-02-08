class CSP:
    """This class describes finite-domain Constraint Satisfaction Problems.
    A CSP is specified by the following inputs:
        variables   A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b
    In the textbook and in most mathematical definitions, the
    constraints are specified as explicit pairs of allowable values,
    but the formulation here is easier to express and more compact for
    most cases (for example, the n-Queens problem can be represented
    in O(n) space using this notation, instead of O(n^4) for the
    explicit representation). In terms of describing the CSP as a
    problem, that's all there is.
    However, the class also supports data structures and methods that help you
    solve CSPs by calling a search function on the CSP. Methods and slots are
    as follows, where the argument 'a' represents an assignment, which is a
    dict of {var:val} entries:
        assign(var, val, a)     Assign a[var] = val; do other bookkeeping
        unassign(var, a)        Do del a[var], plus other bookkeeping
        curr_domains[var]       Slot: remaining consistent values for var
                                Used by constraint propagation routines.
    """

    def __init__(self, variables, domains, neighbors, constraints):
        "Construct a CSP problem."
        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.curr_domains = None

    def assign(self, var, val, assignment):
        """Add {var: val} to assignment; Discard the old value if any."""
        assignment[var] = val

    def unassign(self, var, assignment):
        """Remove {var: val} from assignment.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that."""
        if var in assignment:
            del assignment[var]

    def support_pruning(self):
        """Make sure we can prune values from domains. (We want to pay
        for this only if we use it.)"""
        if self.curr_domains is None:
            self.curr_domains = {
                v: list(self.domains[v]) for v in self.variables}

    def suppose(self, var, value):
        """Start accumulating inferences from assuming var=value."""
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        self.curr_domains[var] = [value]
        return removals

    def prune(self, var, value, removals):
        """Rule out var=value."""
        self.curr_domains[var].remove(value)
        removals.append((var, value))

    def choices(self, var):
        """Return all values for var that aren't currently ruled out."""
        return (self.curr_domains or self.domains)[var]

    def restore(self, removals):
        """Undo a supposition and all inferences from it."""
        for B, b in removals:
            self.curr_domains[B].append(b)

    def display(assignment):
        """Print assignment."""
        print(assignment)


class UniversalDict:
    """A universal dict maps any key to the same value. We use it here
    as the domains dict for CSPs in which all variables have the same domain.
    """

    def __init__(self, value): self.value = value

    def __getitem__(self, key): return self.value

# CSP Backtracking Search


def forward_checking(csp, var, value, assignment, removals):
    """Prune neighbor values inconsistent with var=value."""
    csp.support_pruning()  # clone domains in curr_domains
    for B in csp.neighbors[var]:  # get var neighbors
        if B not in assignment:  # check if neighbor is already assigned
            for b in csp.curr_domains[B][:]:  # get neighbor domain
                # VVV check constraint between var=value and B=b (B is the neighbor) VVV
                if not csp.constraints(var, value, B, b):
                    csp.prune(B, b, removals)  # remove value b from B domain
            if not csp.curr_domains[B]:  # check if curr_domains[B] is empty
                return False  # neighbor B has empty domain after pruning => var != val
    return True  # every neighbor of var has at least one element in the pruned domain


def backtracking_search(csp):
    """[Figure 6.5]"""

    def backtrack(assignment):
        """This is a step of the backtracking_search"""
        # assinged all the variables => found a solution
        if len(assignment) == len(csp.variables):
            return assignment
        # VVV get first not assigned variable VVV
        var = next(var for var in csp.variables if var not in assignment)
        for value in csp.choices(var):  # return the current domain of var
            csp.assign(var, value, assignment)  # assign the value found to var
            # VVV reducing var domain to contain only value VVV
            removals = csp.suppose(var, value)
            # VVV checking respect of neighbors' contraints and reducing their domain VVV
            if forward_checking(csp, var, value, assignment, removals):
                result = backtrack(assignment)  # next step of backtrack
                if result is not None:  # check if backtrack has failed
                    return result
            csp.restore(removals)  # restore the reduced domains
        # VVV unassing var (we have assigned the wrong value) VVV
        csp.unassign(var, assignment)
        return None  # return None to tell the caller backtrack has failed

    return backtrack({})  # start backtrack with no assigned variables
