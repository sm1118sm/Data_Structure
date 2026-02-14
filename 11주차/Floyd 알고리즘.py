INF = 9999

def printA(A):
    vsize = len(A)
    print()
    for i in range(vsize):
        for j in range(vsize):
            if A[i][j] == INF : print( " INF ", end='')
            else : print("%4d "%A[i][j], end='')
        print("")

def shortest_path_floyd_with_path(vertex, adj):
    vsize = len(vertex)
    A = list(adj)

    Next = [[0 if i == j 
             else j if adj[i][j] != INF 
             else -1 for j in range(vsize)] 
             for i in range(vsize)]

    for i in range(vsize):
        print(adj[i])
        A[i] = list(adj[i])

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    Next[i][j] = Next[i][k]

    return A, Next

def print_path(Next, u, v):
    path = [u]
    while u != v:
        u = Next[u][v]
        path.append(u)
    return path
"""
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
"""
'''
vertex = ['A', 'B', 'C', 'D']
weight = [
    [0, 2, 1, INF],
    [2, 0, INF, 4],
    [1, INF, 0, 3],
    [INF, 4, 3, 0],
]
'''


vertex = ['A', 'B', 'C', "D", "E", "F"]
weight = [
    [0,   50,  INF,  20,  INF, INF],
    [50,  0,   10,   15,  20,  INF],
    [INF, 10,  0,    INF, 35,  INF],
    [20,  15,  INF,  0,   15,  INF],
    [INF, 20,  35,   15,  0,   3],
    [INF, INF, INF,  INF, 3,   0],
]



A, Next = shortest_path_floyd_with_path(vertex, weight)

for i in range(len(vertex)):
    for j in range(len(vertex)):
        if i != j:
            print("최단 경로 {} : {}"
                    .format(vertex[i]+"-"+vertex[j], 
                    [vertex[u] for u in print_path(Next, i, j)]))


for i in range(len(Next)):
    for j in range(len(Next[i])):
        print(Next[i][j],end=' ')
    print()
