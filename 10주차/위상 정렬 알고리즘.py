def topological_sort_AM(vertex, edge):
    n = len(vertex)
    inDeg = [0] * n
    for i in range(n):
        for j in range(n):
            if edge[i][j]>0:
                inDeg[j] += 1
                print(f"inDeg : {inDeg[j]}")

    visit = []  
    for i in range(n):
        if inDeg[i] == 0:
            print(f"visit append : {i}")
            visit.append(i)

    while len(visit) > 0:
        v = visit.pop()
        print(vertex[v], end=' ')

        for u in range(n):
            if v != u and edge[v][u]>0:
                inDeg[u] -= 1   
                if inDeg[u] == 0:
                    print(f"visit append : {u}")
                    visit.append(u)

vertex = ['A', 'B', 'C', 'D', 'E', 'F']
graphAM = [[0, 0, 1, 1, 0, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0]]
print('topological_sort : ')
topological_sort_AM(vertex, graphAM)
print()