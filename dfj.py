import pulp

def dfj(c):
    problem = pulp.LpProblem("Rutas_minimas_DFJ", pulp.LpMinimize)

    n = len(c)
    V = range(n) # vertices
    edges = [(i, j) for i in V for j in V if i != j] # aristas

    x = pulp.LpVariable.dicts("x", edges, cat=pulp.LpBinary)

    # Funcion objetivo
    problem += pulp.lpSum(x[i, j] * c[i][j] for i in V for j in V if i != j)

    # Restricciones
    for i in V:
        problem += pulp.lpSum(x[(i, j)] for j in V if i != j) == 1
    for j in V:
        problem += pulp.lpSum(x[(i, j)] for i in V if i != j) == 1

    # Eliminando subtours
    for s in range(2, n):
        for i in range(n - s + 1):
            subset = V[i:i + s]
            problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

    problem.solve()

    print("Millas nauticas que Oscarius Lulang debe recorrer =", pulp.value(problem.objective))
    if pulp.LpStatus[problem.status] == 'Optimal':
        current_port = 0 
        visited_ports = set()
        while True:
            visited_ports.add(current_port)
            next_port = None
            for (i, j) in edges:
                if x[(i, j)].varValue == 1 and i == current_port and j not in visited_ports:
                    next_port = j
                    break
            if next_port is None:
                break
            print(f"De puerto {current_port} a puerto {next_port}")
            current_port = next_port
    else:
        print("No es optimo")
    

