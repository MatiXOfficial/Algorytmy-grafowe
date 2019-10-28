from dimacs import *
from sys import argv
from graph import *

(V, E) = loadDirectedWeightedGraph(argv[1])

def buildResidualNetwork(G):
    V = len(G)
    Gr = [[] for i in range(V)]
    for u in range(V):
        for v in G[u]:
            Gr[u].append([v[0], v[1]])
            Gr[v[0]].append([u, 0])
    return Gr

def updateResidualNetwork(Gr, path, f):
    V = len(Gr)
    for edge in path:
        updateEdge(Gr, edge[0], edge[1], f)

def updateEdge(Gr, u, v, f):
    for edge in Gr[u]:
        if (edge[0] == v):
            edge[1] -= f
            break
    for edge in Gr[v]:
        if (edge[0] == u):
            edge[1] += f
            break

def fordFulkerson(V, E, s, t, dfs):
    G = buildGraph(V, E)
    Gr = buildResidualNetwork(G)
    while(True):
        (parents, flow) = dfs(Gr, s, t)
        if (parents[t] == -1):
            break
        path = []
        v = t
        while (v != s):
            path.append([parents[v], v])
            v = parents[v]
        path.reverse()
        updateResidualNetwork(Gr, path, flow)
    result = 0
    for edge in Gr[s]:
        for redge in Gr[edge[0]]:
            if (redge[0] == s):
                result += redge[1]
                break
    return result

print(fordFulkerson(V, E, 1, V, bfs))

