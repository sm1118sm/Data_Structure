from queue import Queue

def BFS(vtx, adj, s):
    n = len(vtx)                     # 그래프의 정점 수
    visited = [False] * n            # 방문 확인을 위한 리스트
    Q = Queue()                      # 공백 상태의 큐 생성
    Q.put(s)                         # 맨 처음에는 시작 정점만 있음
    visited[s] = True                # s는 "방문"했다고 표시
    while not Q.empty():
        s = Q.get()                  # 큐에서 정점을 꺼냄
        print(vtx[s], end=' ')       # 정점을 출력(처리)함
        for v in range(n):           # 정점의 개수만큼 실행
            if adj[s][v] != 0 and not visited[v]:  # 간선이 있고, 방문하지 않은 이웃 정점이면
                Q.put(v)             # 큐에 삽입
                visited[v] = True    # "방문"했다고 표시

vtx2 = ['a', 'b', 'c', 'd', 'e', 'f']
edge2 = [
    [0,1,1,0,0,0],  # a
    [1,0,0,1,1,0],  # b
    [1,0,0,0,0,1],  # c
    [0,1,0,0,0,0],  # d
    [0,1,0,0,0,0],  # e
    [0,0,1,0,0,0]   # f
]
print('BFS(출발:a): ', end="")
BFS(vtx2, edge2, 0)
print()