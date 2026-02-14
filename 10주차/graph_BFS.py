from queue import Queue
def BFS_AL(vtx, aList, s):
    n = len(vtx)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        s = Q.get()
        print(vtx[s], end=' ')
        for v in aList[s]:
            if visited[v] == False:
                Q.put(v)
                visited[v] = True

vtx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
aList = [
    [1, 2, 8],  # a
    [0, 3],  # b
    [0, 3, 4],  # c
    [1, 2, 5],  # d
    [2, 6, 7],  # e
    [ 3, 9],  # f
    [4, 7],  # g
    [4, 6]  # h
]

print('BFS_AL(출발 : A) : ',end=' ')
BFS_AL(vtx, aList, 0)
print()