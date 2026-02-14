parent = []
set_size = 0
#서로 집합의 초기화
def init_set(nSets):
    global set_size, parent
    get_size = nSets
    for i in range(nSets):
        parent.append(-1)

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
