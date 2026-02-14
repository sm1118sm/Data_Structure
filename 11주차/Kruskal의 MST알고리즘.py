parent = []
set_size = 0

#대표 원소의, 투트의 인덱스 반환
def find(id):
    while(parent[id] >= 0):
        id = parent[id]
    return id

#집합을 병합, s1을 s2에 병합, 집합의 수가 1개 감소
def union(s1, s2):
    global set_size
    parent[s1] = s2
    set_size = set_size -1


def init_set(nSets):
    global set_size, parent
    get_size = nSets
    for i in range(nSets):
        parent.append(-1)

def MSTKruskal(vertex, adj):
    vsize = len(vertex)
    init_set(vsize) #서로소 집합의 초기화
    eList = []

    for i in range(vsize-1):
        for j in range(i + 1, vsize):
            if adj[i][j] != None:
                eList.append( (i, j, adj[i][j]) )

    eList.sort(key = lambda e : e[2], reverse=True)
    edgeAcceped = 0
    while(edgeAcceped < vsize -1):
        e = eList.pop()
        uset = find(e[0])
        vset = find(e[1])

        if uset != vset:
            print("간선 추가 : (%s, %s, %d)" %
                  (vertex[e[0]], vertex[e[1]],e[2]))
            union(uset, vset)
            edgeAcceped += 1

'''vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[None,    29,     None,   None,   None,   10,     None],
          [29,      None,   16,     None,   None,   None,   15],
          [None,    16,     None,   12,     None,   None,   None],
          [None,    None,   12,     None,   22,     None,   18],
          [None,    None,   None,   22,     None,   27,     25],
          [10,      None,   None,   None,   27,     None,   None],
          [None,    15,     None,   18,     25,     None,   None],
          ]'''

vertex = ['A', 'B', 'C', "D", "E"]
weight = [
    [None,  1,  None,  2,  None],
    [1,  None,  3,  1,  None],
    [None,  3,  None,  3,  1],
    [2,  1,  3,  None,  2],
    [None,  None,  1,  2,  None],
]

print("MST By Kruskal's Algorith")
MSTKruskal(vertex, weight)