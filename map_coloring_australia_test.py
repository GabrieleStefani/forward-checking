from csp import MapColoring, backtracking_search


australia_csp = MapColoring(
    list('RGB'), """SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: """)

MapColoring.display(backtracking_search(australia_csp))
