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


parent = []
set_size = 0
total = 0

def init_set(n):
    global parent, set_size, total
    parent = [-1] * n
    set_size = n
    total = 0

def find(x):
    while parent[x] >= 0:
        x = parent[x]
    return x

def union(s1, s2):
    parent[s1] = s2

def MSTKruskal(vertex, adj):
    global total
    vsize = len(vertex)

    init_set(vsize)

    eList = []
    for i in range(vsize):
        for j in range(i+1, vsize):
            if adj[i][j] is not None:
                eList.append((i, j, adj[i][j]))

    eList.sort(key=lambda x: x[2])  # 오름차순

    edgeAccepted = 0

    while edgeAccepted < vsize - 1:
        e = eList.pop(0)
        uset = find(e[0])
        vset = find(e[1])

        if uset != vset:
            print(f"간선 추가 : ({vertex[e[0]]}, {vertex[e[1]]}, {e[2]})")
            total += e[2]
            union(uset, vset)
            edgeAccepted += 1

    print("가중치의 합 :", total)


print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, weight)
