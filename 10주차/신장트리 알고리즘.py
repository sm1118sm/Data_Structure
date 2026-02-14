from queue import Queue
def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                print("(", vtx[s], vtx[v], ")", end='')
                ST_DFS(vtx, adj, v, visited)

def BFS_spanning_tree(graph, root):
    visited = [False]*len(graph)
    queue = Queue()
    queue.put(root)
    visited[root] = True
    spanning_tree = []

    while not queue.empty():
        node = queue.get()
        for neighbor in range(len(graph[node])):
            if graph[node][neighbor] != 0 and not visited[neighbor]:
                queue.put(neighbor)
                visited[neighbor] = True
                spanning_tree.append((node, neighbor))

    return spanning_tree

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

spanning_tree = BFS_spanning_tree(graph, 0)
print("신장 트리의 간선: ", spanning_tree)
