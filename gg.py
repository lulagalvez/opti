import pulp

def gg(c):
    problema = pulp.LpProblem("Rutas_Minimas_GG", pulp.LpMinimize)
    n=len(c)  # cantidad de nodos
    V = range(n)  # vertices
    A = [(i, j) for i in V for j in V if i != j]  # aristas

    x = pulp.LpVariable.dicts("x", A, 0, 1, pulp.LpBinary)  # variables de desicion binarias
    g = pulp.LpVariable.dicts("g", A, 0, None, pulp.LpInteger)  # variable entera que define el numero de aristas que van desde el vertice 1 hacia el vertice ij dentro de la ruta optima

    problema += pulp.lpSum(c[i][j] * x[(i, j)] for (i, j) in A) # funcion objetivo de minimización

    # Restricciones
    for i in V:   
        problema += pulp.lpSum(x[(i, j)] for j in V if i != j) == 1

    for j in V:
        problema += pulp.lpSum(x[(i, j)] for i in V if i != j) == 1
    # Restricciones adcicionales del modelo
    for i in range(1,n):
        problema += pulp.lpSum(g[(i,j)] for j in V if i!=j) - pulp.lpSum(g[(j,i)] for j in range(1,n) if i != j) == 1
        for j in V:
            if i!=j:
                problema += g[(i,j)] <= (n-1)*x[(i,j)]  
        
    problema.solve()
    
    print("Calculado utilizando gg")
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
