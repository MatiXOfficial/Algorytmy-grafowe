from sys import argv
from dimacs import *

def buildGraph(V, E):
    G = [[] for i in range(V + 1)]
    for (x, y, c) in E:
        G[x].append((y, c))
        G[y].append((x, c))
    return G

(V, E) = loadWeightedGraph(argv[1])

def guideProblemDFS(V, E, s, t):
    max = 0
    for (x, y, c) in E:
        if max < c:
            max = c

    G = buildGraph(V, E)
    print(G)
    for result in range(max, -1, -1):
        if (DFS(G, s, t, result)):
            return result
    return -1

def DFS(G, s, t, min):
    V = len(G)
    visited = [False] * (V + 1)
    return DFSVisit(G, s, t, visited, min)

def DFSVisit(G, s, t, visited, min):
    if s == t:
        return True
    visited[s] = True
    for (y, c) in G[s]:
        if (c >= min and visited[y] == False):
            if DFSVisit(G, y, t, visited, min) == True:
                return True
    return False

print(guideProblemDFS(V, E, 1, 2))