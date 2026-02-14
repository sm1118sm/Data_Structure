def DFS2(graph, v, visited):
    if v not in visited:
        visited.add(v)
        print(v, end=' ')
        nbr = graph[v] - visited
        for u in nbr:
            DFS2(graph, u, visited)

mygraph = { "A" : {"B", "C"},
            "B" : {"A", "D"},
            "C" : {"A", "D", "E"},
            "D" : {"B", "C", "F"},
            "E" : {"C", "G", "H"},
            "F" : {"D"},
            "G" : {"E", "H"},
            "H" : {"E", "G"}
            }

print("DFS2(출발:A) : ", end="")
DFS2(mygraph, "A", set())
print()