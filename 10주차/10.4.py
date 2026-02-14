from queue import Queue

vtx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

adjMat = [
 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # a
 [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # b
 [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # c
 [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # d
 [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],  # e
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],  # f
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],  # g
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # h
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # i
 [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]   # j
]

adjList = [
    [1, 2],        # a
    [0, 3, 4],     # b
    [0, 5, 6],     # c
    [1, 7],        # d
    [1, 8],        # e
    [2, 9],        # f
    [2, 9],        # g
    [3],           # h
    [4],           # i
    [5, 6]         # j
]


def bfsST(vtx, adj, s, visited):
    n = len(vtx)                      # 그래프 정점의 수
    visited = [False] * n             # 이미 방문한 정점인지 확인하는 리스트
    Q = Queue()
    Q.put(s)                          # 시작 정점을 큐에 추가
    visited[s] = True                 # 시작 정점을 방문 처리

    while not Q.empty():
        s = Q.get()                   # 큐에서 정점을 꺼냄
        for v in range(n):
            if adj[s][v] != 0 and not visited[v]:  # 간선이 있고 방문하지 않은 정점이라면
                Q.put(v)             # 큐에 정점을 추가
                visited[v] = True    # 정점을 방문 처리
                print("(", vtx[s], vtx[v], ")", end=' ')  # 간선 출력

print('신장트리(BFS): ', end="")
bfsST(vtx, adjMat, 0, [False] * len(vtx))
print()

