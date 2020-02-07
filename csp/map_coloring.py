from csp import CSP, UniversalDict
from collections import defaultdict


class MapColoring(CSP):

    def __init__(self, colors, neighbors):
        """Make a CSP for the problem of coloring a map with different colors
        for any two adjacent regions. Arguments are a list of colors, and a
        dict of {region: [neighbor,...]} entries. This dict may also be
        specified as a string of the form defined by parse_neighbors."""

        def parse_neighbors(neighbors):
            """Convert a string of the form 'X: Y Z; Y: Z' into a dict mapping
            regions to neighbors. The syntax is a region name followed by a ':'
            followed by zero or more region names, followed by ';', repeated for
            each region name. If you say 'X: Y' you don't need 'Y: X'.
            """
            dic = defaultdict(list)
            specs = [spec.split(':') for spec in neighbors.split(';')]
            for (A, Aneighbors) in specs:
                A = A.strip()
                for B in Aneighbors.split():
                    dic[A].append(B)
                    dic[B].append(A)
            return dic

        if isinstance(neighbors, str):
            neighbors = parse_neighbors(neighbors)

        def different_values_constraint(A, a, B, b):
            """A constraint saying two neighboring variables must differ in value."""
            return a != b
        CSP.__init__(self, list(neighbors.keys()), UniversalDict(
            colors), neighbors, different_values_constraint)
