from dimacs import *
from sys import argv
from graph import *

(V, E) = loadDirectedWeightedGraph(argv[1])

def buildResidualNetwork(V, E):
    V += 1
    RN = [[] for i in range(V)]
    for (x, y, c) in E:
        RN[x].append([y, c, len(RN[y]), True])
        RN[y].append([x, 0, len(RN[x]) - 1, False])
    return RN

def updateResidualNetwork(RN, path, f):
    for edge in path:
        updateEdge(RN, edge[0], edge[1], f)

def updateEdge(RN, u, v, f):
    for edge in RN[u]:
        if (edge[0] == v):
            edge[1] -= f
            RN[v][edge[2]][1] += f
            break

def createPath(s, v, parents):
    path = []
    while v != s:
        path.append([parents[v], v])
        v = parents[v]
    path.reverse()
    return path

def fordFulkerson(V, E, s, t, dfs = dfs):
    RN = buildResidualNetwork(V, E)
    while(True):
        (parents, flow) = dfs(RN, s, t)
        if (parents[t] == -1):
            break
        path = createPath(s, t, parents)
        updateResidualNetwork(RN, path, flow)
    result = 0
    for edge in RN[t]:
        if edge[3] == False:
            result += edge[1]
    return result

#print(fordFulkerson(V, E, 1, V))

