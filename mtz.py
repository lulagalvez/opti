import pulp

def mtz(c):
    
    problema = pulp.LpProblem("Rutas_Minimas_MTZ", pulp.LpMinimize)
    n=len(c)  # cantidad de nodos    
    V = range(n)  # vértices
    A = [(i, j) for i in V for j in V if i != j]  # aristas

    x = pulp.LpVariable.dicts("x", A, 0, 1, pulp.LpBinary) # variables de decisión binarias
    u = pulp.LpVariable.dicts("u", V, 0.9, n+0.1, pulp.LpInteger ) # variables que representan el orden del vertice i en la ruta optima

    problema += pulp.lpSum(c[i][j] * x[(i, j)] for (i, j) in A) # función objetivo de minimización
    # Restricciones
    for i in V:
        problema += pulp.lpSum(x[(i, j)] for j in V if i != j) == 1

    for j in V:
        problema += pulp.lpSum(x[(i, j)] for i in V if i != j) == 1
    # Restricciones adicionales modelo MTZ
    for i,j in A:
        if(i>=1):
            problema += u[i]-u[j]+1<=n*(1-x[(i,j)])
        
    problema.solve()

    print("Calculado utilizando MTZ")
    print("Millas nauticas que Oscarius Lulang debe recorrer =", pulp.value(problema.objective))
    if pulp.LpStatus[problema.status] == 'Optimal':
        current_port = 0 
        visited_ports = set()
        while True:
            visited_ports.add(current_port)
            next_port = None
            for (i, j) in A:
                if x[(i, j)].varValue == 1 and i == current_port and j not in visited_ports:
                    next_port = j
                    break
            if next_port is None:
                break
            print(f"De puerto {current_port} a puerto {next_port}")
            current_port = next_port
    else:
        print("No es optimo")
