def weightSum(visit, W):    #매개변수 : 정점 리스트, 인접 행렬
    sum = 0 #가중치의 합
    for i in range(len(visit)): #모든 정점에 대해(i: 0, ... N-1)
        for j in range(i + 1, len(visit)):  #하나의 행에 대해 (삼각영역)
            if W[i][j] != None: #만약 간선이 있으면
                sum += W[i][j]  #sum에 추가
    return sum  #전체 가중치 합을 반환