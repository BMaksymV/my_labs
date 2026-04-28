import heapq

INF = 10**18

def minimize(n, m, clients, graph):
    max_dist = [0] * (n + 1)

    def dijkstra(start):
        dist = [INF] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            
            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        
        return dist

    for c in clients:
        dist = dijkstra(c)
        for i in range(1, n + 1):
            max_dist[i] = max(max_dist[i], dist[i])

    clients_set = set(clients)
    answer = INF

    for i in range(1, n + 1):
        if i not in clients_set:
            answer = min(answer, max_dist[i])

    return answer


def read_input(filename):
    with open(filename, "r") as f:
        n, m = map(int, f.readline().split())
        clients = list(map(int, f.readline().split()))
        
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            graph[u].append((v, w))
            graph[v].append((u, w))
    
    return n, m, clients, graph

if __name__ == "__main__":
    n, m, clients, graph = read_input("gamsrv.in")
    answer = minimize(n, m, clients, graph)

    with open("gamsrv.out", "w") as f:
        f.write(str(answer))