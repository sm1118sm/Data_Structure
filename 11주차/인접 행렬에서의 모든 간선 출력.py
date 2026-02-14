def printAllEdges(visit, W):    #매개변수 : 정점 리스트, 인접 행렬
    for i in range(len(visit)): 
        for j in range(i+1, len(W[i])): #모든 간선 W[i][j]에 대해
            if W[i][j] != None and W[i][j] != 0:    #간선이 있으면
                print("(%s,%s,%d)"%(visit[i], visit[j], W[i][j]), end=' ')
    print()