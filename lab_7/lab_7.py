import csv

def read_matrix(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        matrix = [list(map(int, row)) for row in reader]
    return matrix

def prim_alg(matrix):
    n = len(matrix)
    visited = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    
    total = 0
    
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or min_edge[i] < min_edge[u]):
                u = i
        
        visited[u] = True
        total += min_edge[u]
        
        for v in range(n):
            if matrix[u][v] != 0 and not visited[v]:
                min_edge[v] = min(min_edge[v], matrix[u][v])
    
    return total

matrix = read_matrix("islands.csv")
result = prim_alg(matrix)

print(f"MST :{result}")