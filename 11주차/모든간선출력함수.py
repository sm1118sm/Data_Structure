def printAllEdges(graph):
    for v in graph:
        for e in graph[v]:
            print( "( %s, %s, %d)"%(v, e[0], e[1]),end='')