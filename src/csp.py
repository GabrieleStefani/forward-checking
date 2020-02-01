class CSP:
    """This class describes finite-domain Constraint Satisfaction Problems.
      A CSP is specified by the following three inputs:
          vars        A list of variables; each is atomic (e.g. int or string).
          domains     A dict of {var:[possible_value, ...]} entries.
          neighbors   A dict of {var:[var,...]} that for each variable lists
                      the other variables that participate in constraints.
          constraints A function f(A, a, B, b) that returns true if neighbors
                      A, B satisfy the constraint when they have values A=a, B=b
      In the textbook and in most mathematical definitions, the
      constraints are specified as explicit pairs of allowable values,
      but the formulation here is easier to express and more compact for
      most cases. (For example, the n-Queens problem can be represented
      in O(n) space using this notation, instead of O(N^4) for the
      explicit representation.) In terms of describing the CSP as a
      problem, that's all there is.

      However, the class also supports data structures and methods that help you
      solve CSPs by calling a search function on the CSP.  Methods and slots are
      as follows, where the argument 'a' represents an assignment, which is a
      dict of {var:val} entries:
          assign(var, val, a)     Assign a[var] = val; do other bookkeeping
          unassign(var, a)        Do del a[var], plus other bookkeeping
          curr_domains[var]       Slot: remaining consistent values for var
                                  Used by constraint propagation routines.
      The following are just for debugging purposes:
          nassigns                Slot: tracks the number of assignments made
          display(a)              Print a human-readable representation
          """

    def __init__(self, vars, domains, neighbors, constraints):
        "Construct a CSP problem. If vars is empty, it becomes domains.keys()."
        vars = vars or domains.keys()
        self.vars = vars
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.initial = {}
        self.curr_domains = None
        self.pruned = None
        self.nassigns = 0

    def assign(self, var, val, assignment):
        """Add {var: val} to assignment; Discard the old value if any.
        Do bookkeeping for curr_domains and nassigns."""
        self.nassigns += 1
        assignment[var] = val
        if self.curr_domains:
            self.forward_check(var, val, assignment)

    def unassign(self, var, assignment):
        """Remove {var: val} from assignment; that is backtrack.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that."""
        if var in assignment:
            # Reset the curr_domain to be the full original domain
            if self.curr_domains:
                self.curr_domains[var] = self.domains[var][:]
            del assignment[var]

    def forward_check(self, var, val, assignment):
        "Do forward checking (current domain reduction) for this assignment."
        if self.curr_domains:
            # Restore prunings from previous value of var
            for (B, b) in self.pruned[var]:
                self.curr_domains[B].append(b)
            self.pruned[var] = []
            # Prune any other B=b assignement that conflict with var=val
            for B in self.neighbors[var]:
                if B not in assignment:
                    for b in self.curr_domains[B][:]:
                        if not self.constraints(var, val, B, b):
                            self.curr_domains[B].remove(b)
                            self.pruned[var].append((B, b))

    def display(self, assignment):
        "Show a human-readable representation of the CSP."
        # Subclasses can print in a prettier way, or display with a GUI
        print('CSP:', self, 'with assignment:', assignment)

# CSP Backtracking Search


def backtracking_search(csp):
    "Set up to do recursive backtracking search"
    csp.curr_domains, csp.pruned = {}, {}
    for v in csp.vars:
        csp.curr_domains[v] = csp.domains[v][:]
        csp.pruned[v] = []
    return recursive_backtracking({}, csp)


def recursive_backtracking(assignment, csp):
    """Search for a consistent assignment for the csp.
    Each recursive call chooses a variable, and considers values for it."""
    if len(assignment) == len(csp.vars):
        return assignment
    var = select_unassigned_variable(assignment, csp)
    for val in order_domain_values(var, assignment, csp):
        csp.assign(var, val, assignment)
        result = recursive_backtracking(assignment, csp)
        if result is not None:
            return result
    csp.unassign(var, assignment)
    return None


def select_unassigned_variable(assignment, csp):
    "Select the variable to work on next"
    for v in csp.vars:
        if v not in assignment:
            return v


def order_domain_values(var, assignment, csp):
    "Decide what order to consider the domain variables."
    if csp.curr_domains:
        domain = csp.curr_domains[var]
    else:
        domain = csp.domains[var][:]
    while domain:
        yield domain.pop()
