def MSTPrim(vertex, adj) :
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0
    for i in range(vsize) :
        u = getMinVertex(dist, selected)
        selected[u] = True
        print("--",vertex[u], "--")

        for v in range(vsize) :
            if adj[u][v] != None:
                print(vertex[u],"에서 ", vertex[v], "로 가는 간선 발견 : ",adj[u][v])
                if selected[v] == False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]
    print()
    
INF = 9999  # 가장 큰 가중치 (무한대)
def getMinVertex(dist, selected) :
    print("getMinVertex")
    minv = 0
    mindist = INF
    for v in range(len(dist)) :
        if not selected[v] and dist[v] < mindist:
            print(vertex[v],"에서 ", mindist, "보다 작은 값 ", dist[v], " 발견")
            mindist = dist[v]
            minv = v
    print(dist)
    return minv

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[None,    29,     None,   None,   None,   10,     None],
          [29,      None,   16,     None,   None,   None,   15],
          [None,    16,     None,   12,     None,   None,   None],
          [None,    None,   12,     None,   22,     None,   18],
          [None,    None,   None,   22,     None,   27,     25],
          [10,      None,   None,   None,   27,     None,   None],
          [None,    15,     None,   18,     25,     None,   None],
          ]

MSTPrim(vertex, weight)