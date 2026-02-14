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


def getMinVertex(dist, selected):
    minv = -1
    mind = INF
    for i in range(len(dist)):
        if not selected[i] and dist[i] < mind:
            mind = dist[i]
            minv = i
    return minv

def MSTPrim(vertex, adj):
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    total = 0

    dist[0] = 0

    for i in range(vsize):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')
        total += dist[u]

        for v in range(vsize):
            if adj[u][v] is not None:
                if not selected[v] and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]

    print("\n가중치 합 :", total)


print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)
