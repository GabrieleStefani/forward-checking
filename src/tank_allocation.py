import xml.etree.ElementTree as ET
import numpy as np
import itertools
import csp


def main():
    variables = []
    domains = {}
    neighbors = {}
    data = ET.parse("chemical.xml")
    for tank in list(data.getroot()[2].getchildren()):
        var = tank.get("id")
        variables.append(var)
        domains[var] = []
        neighbors[var] = []
        for cargo in data.getroot().find("cargos").iter("cargo"):
            impossible = False
            if tank.find("impossiblecargos"):
                for impossibleCargo in tank[0].iter("cargo"):
                    if cargo.get("id") == impossibleCargo.get("id"):
                        impossible = True
            if(not impossible):
                domains[var].append(cargo.get("id"))
        if tank.find("neighbours"):
            for neighbor in tank.find("neighbours").iter("tank"):
                neighbors[var].append(neighbor.get("id"))

    incompatibles = []
    for incompatible in data.getroot().find("incompatibles").iter("incompatible"):
        incompatibles.append(
            (incompatible.get("cargo1"), incompatible.get("cargo2")))

    def constraint(A, a, B, b):
        found = False
        for (cargo1, cargo2) in incompatibles:
            found = found or (cargo1 == a and cargo2 == b) or (
                cargo2 == a and cargo1 == b)
        return found

    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
