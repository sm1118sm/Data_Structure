# 무한대 값
INF = 9999

weight = [
    [INF,  2,   INF,  1,   INF, INF, INF],
    [2,    INF, 3,    INF, INF,  5,   INF],
    [INF,  3,   INF,  4,   INF, INF,  6],
    [1,    INF, 4,    INF, 7,   INF, INF],
    [INF,  INF, INF, 7,   INF, 2,    3],
    [INF,  5,   INF, INF, 2,   INF,  4],
    [INF,  INF, 6,   INF, 3,   4,   INF]
]

weight_dijkstra = [
    [0,   2,   INF, 1,   INF, INF, INF],
    [2,   0,   3,   INF, INF, 5,   INF],
    [INF, 3,   0,   4,   INF, INF, 6],
    [1,   INF, 4,   0,   7,   INF, INF],
    [INF, INF, INF, 7,   0,   2,   3],
    [INF, 5,   INF, INF, 2,   0,   4],
    [INF, INF, 6,   INF, 3,   4,   0]
]

# 정점 이름
vertex_new = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
