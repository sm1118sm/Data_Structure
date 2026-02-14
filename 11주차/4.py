# 무한대 값
INF = 9999

weight = [
    [INF,  2,   INF,  1,   INF, INF, INF],
    [2,    INF, 3,    INF, INF,  5,   INF],
    [INF,  3,   INF,  4,   INF, INF,  6],
    [1,    INF, 4,    INF, 7,   INF, INF],
    [INF,  INF, INF, 7,   INF, 2,    3],
    [INF,  5,   INF, INF, 2,   INF,  4],
    [INF,  INF, 6,   INF, 3,   4,   INF]
]

weight_dijkstra = [
    [0,   2,   INF, 1,   INF, INF, INF],
    [2,   0,   3,   INF, INF, 5,   INF],
    [INF, 3,   0,   4,   INF, INF, 6],
    [1,   INF, 4,   0,   7,   INF, INF],
    [INF, INF, INF, 7,   0,   2,   3],
    [INF, 5,   INF, INF, 2,   0,   4],
    [INF, INF, 6,   INF, 3,   4,   0]
]

# 정점 이름
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def choose_vertex(dist, found):
    minv = INF
    minpos = -1
    for i in range(len(dist)):
        if dist[i] < minv and not found[i]:
            minv = dist[i]
            minpos = i
    return minpos

def shortest_path_dijkstra(vertex, adj, start):
    vsize = len(vertex)
    dist = adj[start][:]
    path = [start] * vsize
    found = [False] * vsize

    found[start] = True
    dist[start] = 0

    for step in range(vsize):
        print(f"Step{step+1:2d}:", dist)
        u = choose_vertex(dist, found)
        found[u] = True

        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u

    return path

print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, weight_dijkstra, start)
for end in range(len(vertex)):
    if end != start:
        print(f"[최단경로: {vertex[start]}->{vertex[end]}] {vertex[end]}", end='')
        cur = end
        while path[cur] != start:
            print(f" <- {vertex[path[cur]]}", end='')
            cur = path[cur]
        print(f" <- {vertex[start]}")