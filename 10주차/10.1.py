import networkx as nx
import matplotlib.pyplot as plt

# 노드
vtx = ['a','b','c','d','e','f','g','h','i','j']

# 인접 행렬
adjMat = [
 [0,1,0,0,0,0,0,0,0,0],  # a
 [1,0,1,0,0,0,0,0,0,0],  # b
 [0,1,0,1,0,0,0,0,0,0],  # c
 [0,0,1,0,1,0,0,0,0,0],  # d
 [0,0,0,1,0,1,0,0,0,0],  # e
 [0,0,0,0,1,0,1,0,0,0],  # f
 [0,0,0,0,0,1,0,1,0,0],  # g
 [0,0,0,0,0,0,1,0,1,0],  # h
 [0,0,0,0,0,0,0,1,0,1],  # i
 [0,0,0,0,0,0,0,0,1,0],  # j
]

# 인접 리스트 (선형 트리)
adjList = [
    [1],       # a → b
    [0, 2],    # b → a, c
    [1, 3],    # c → b, d
    [2, 4],    # d → c, e
    [3, 5],    # e → d, f
    [4, 6],    # f → e, g
    [5, 7],    # g → f, h
    [6, 8],    # h → g, i
    [7, 9],    # i → h, j
    [8]        # j → i
]

# 인접 행렬 기반 그래프
def graph1():
    G = nx.Graph()
    for i, v in enumerate(vtx):
        G.add_node(v)
    for i in range(len(vtx)):
        for j in range(i+1, len(vtx)):
            if adjMat[i][j]==1:
                G.add_edge(vtx[i], vtx[j])
    print("graph1 트리 여부:", nx.is_tree(G))
    pos = nx.spring_layout(G, k=0.3)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_weight='bold')
    plt.title("graph1: 인접 행렬 기반")
    plt.show()

# 인접 리스트 기반 그래프
def graph2():
    G = nx.Graph()
    for i, v in enumerate(vtx):
        G.add_node(v)
    for i in range(len(vtx)):
        for j in adjList[i]:
            G.add_edge(vtx[i], vtx[j])
    print("graph2 트리 여부:", nx.is_tree(G))
    pos = nx.shell_layout(G)  # 트리 구조에 적합
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_weight='bold')
    plt.title("graph2: 인접 리스트 기반")
    plt.show()

# 실행
graph1()
graph2()
