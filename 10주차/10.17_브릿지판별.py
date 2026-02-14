graph = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'f'],
    'd': ['b'],
    'e': ['b'],
    'f': ['c']
}


visited = {node: False for node in graph}
dfs_low = {node: 0 for node in graph}
dfs_num = {node: 0 for node in graph}
dfs_parent = {node: None for node in graph}
bridge_list = []

def find_bridges(graph, u, visited, dfs_low, dfs_num, dfs_parent, bridge_list, dfsNumberCounter):
    visited[u] = True
    dfs_low[u] = dfsNumberCounter
    dfs_num[u] = dfsNumberCounter
    dfsNumberCounter += 1

    for v in graph[u]:
        if not visited[v]:
            dfs_parent[v] = u

            find_bridges(graph, v, visited, dfs_low, dfs_num, dfs_parent, bridge_list, dfsNumberCounter)

            if dfs_low[v] > dfs_num[u]:
                bridge_list.append((u, v))

            dfs_low[u] = min(dfs_low[u], dfs_low[v])

        elif v != dfs_parent[u]:
            dfs_low[u] = min(dfs_low[u], dfs_num[v])

find_bridges(graph, 'a', visited, dfs_low, dfs_num, dfs_parent, bridge_list, 0)
print("브리지: ", bridge_list)
