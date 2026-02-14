def DFS(vtx, adjList, s, visited):
    print(vtx[s], end=' ')          # 현재 정점 s를 출력함
    visited[s] = True               # 방문한 정점을 True로 표시

    for v in adjList[s]:            # 인접 리스트를 순회
        if not visited[v]:          # v를 아직 방문하지 않았다면 다시 DFS 실행
            DFS(vtx, adjList, v, visited)

vtx = ['a', 'b', 'c', 'd']

adjList = [
    [1],      # a - b
    [0, 2],   # b - a, c
    [1, 3],   # c - b, d
    [2]       # d - c
]
print("DFS(출발:a) :", end=" ")
DFS(vtx, adjList, 0, [False]*len(vtx))
print()
