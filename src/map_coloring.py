import csp
from collections import defaultdict

australia_csp = (
    list('RGB'), """SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: """)

usa_csp = (list('RGBY'),
           """WA: OR ID; OR: ID NV CA; CA: NV AZ; NV: ID UT AZ; ID: MT WY UT;
                         UT: WY CO AZ; MT: ND SD WY; WY: SD NE CO; CO: NE KA OK NM; NM: OK TX AZ;
                         ND: MN SD; SD: MN IA NE; NE: IA MO KA; KA: MO OK; OK: MO AR TX;
                         TX: AR LA; MN: WI IA; IA: WI IL MO; MO: IL KY TN AR; AR: MS TN LA;
                         LA: MS; WI: MI IL; IL: IN KY; IN: OH KY; MS: TN AL; AL: TN GA FL;
                         MI: OH IN; OH: PA WV KY; KY: WV VA TN; TN: VA NC GA; GA: NC SC FL;
                         PA: NY NJ DE MD WV; WV: MD VA; VA: MD DC NC; NC: SC; NY: VT MA CT NJ;
                         NJ: DE; DE: MD; MD: DC; VT: NH MA; MA: NH RI CT; CT: RI; ME: NH;
                         HI: ; AK: """)

france_csp = (list('RGBY'),
              """AL: LO FC; AQ: MP LI PC; AU: LI CE BO RA LR MP; BO: CE IF CA FC RA
                            AU; BR: NB PL; CA: IF PI LO FC BO; CE: PL NB NH IF BO AU LI PC; FC: BO
                            CA LO AL RA; IF: NH PI CA BO CE; LI: PC CE AU MP AQ; LO: CA AL FC; LR:
                            MP AU RA PA; MP: AQ LI AU LR; NB: NH CE PL BR; NH: PI IF CE NB; NO:
                            PI; PA: LR RA; PC: PL CE LI AQ; PI: NH NO CA IF; PL: BR NB CE PC; RA:
                            AU BO FC PA LR""")


def main():
    variables = []
    domains = {}
    neighbors = defaultdict(list)
    (domain, countries) = australia_csp
    for country in countries.split(';'):
        (var, var_neighbors) = country.split(":")
        var = var.strip()
        neighbors[var] = []
        for neighbor in var_neighbors.split():
            neighbors[var].append(neighbor)
            neighbors[neighbor].append(var)
    for var in neighbors.keys():
        variables.append(var)
        domains[var] = domain

    def constraint(A, a, B, b):
        return a != b
    prob = csp.CSP(variables, domains, neighbors, constraint)
    prob.display(csp.backtracking_search(prob))


if __name__ == "__main__":
    main()
