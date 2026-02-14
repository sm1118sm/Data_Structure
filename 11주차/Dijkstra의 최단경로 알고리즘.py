INF = 9999
def choose_vertex(dist, found):
    print("choose_vertex")
    min = INF
    minpos = -1
    for i in range(len(dist)):
        if dist[i] < min and found[i] == False:
            print(vertex[i]," 으로 가는 ",min, "보다 작은 간선 ",dist[i]," 발견")
            min = dist[i]
            minpos = i
    return minpos

def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True
    dist[start] = 0

    for i in range(vsize):
        print("Step%2d : "%(i+1), dist)
        u = choose_vertex(dist, found)
        found[u] = True

        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    print(dist[u]," 와 ",adj[u][w]," 를 더한게 ",dist[w], "보다 작음")
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u

    return path
'''
vertex = ['A', 'B', 'C', "D", "E", "F", "G"]
weight = [
        [0, 7, INF, INF, 3, 10 ,INF],
        [7, 0, 4, 10, 2, 6 ,INF],
        [INF, 4, 0, 2, INF, INF ,INF],
        [INF, 10, 2, 0,11, 9 ,4],
        [3, 2, INF, 11, 0, INF ,5],
        [10, 6, INF, 9, INF, 0 ,INF],
        [INF, INF, INF, 4, 5, INF ,0],
]
'''
'''
vertex = ['A', 'B', 'C', 'D']
weight = [
    [0, 2, 1, INF],
    [2, 0, INF, 4],
    [1, INF, 0, 3],
    [INF, 4, 3, 0],
]
'''
vertex = ['A', 'B', 'C', 'D']
weight = [
    [0, 5, INF, INF],
    [INF, 0, 2, 1],
    [INF, INF, 0, 4],
    [3, INF, INF, 0],
]

start = 0
path = shortest_path_dijkstra(vertex, weight, start)

for end in range(len(vertex)):
    if end != start:
        print("[최단경로: %s -> %s] %s"% 
              (vertex[start], vertex[end], vertex[end]), end='')
        while (path[end] != start):
            print(" <- %s" % vertex[path[end]],end='')
            end = path[end]
        print(" <-%s" % vertex[path[end]])