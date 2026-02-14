from queue import Queue
def bfs_cc(vtx, adj, s, visited):
    visited[s] = True
    group = []
    for i in range(len(vtx)):
        if adj[s][i] != 0 and visited[i] == False:
            group.append(bfs_cc(vtx, adj, i, visited))
    return group 
def find_connected_component(vtx, adj):
    n = len(vtx)
    visited = [False]*n
    groups = []

    for v in range(n):
        if visited[v] == False:
            print("정점 : ", v, " 방문안함")
            color = bfs_cc(vtx, adj, v, visited)
            groups.append(color)

    return groups

vertex = ['A', 'B', 'B', 'D', 'E']
adjMat = [[0, 1, 1, 0, 0],
          [1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1],
          [0, 0, 0, 1, 0]]

colorGroup = find_connected_component(vertex, adjMat)
print("연결성분 개수 = %d" % len(colorGroup))
print(colorGroup)