from dimacs import *
from sys import argv
from graph import *
from FordFulkerson import *

(V, E) = (V, E) = loadWeightedGraph(argv[2])

def buildConnectivityResidualNetwork(V, E):
    V += 1
    RN = [[] for i in range(V)]
    for (x, y, c) in E:
        RN[x].append([y, 1, len(RN[y]), False])
        RN[y].append([x, 1, len(RN[x]) - 1, False])
    return RN

def connectivityFordFulkerson(V, E, s, t, dfs = dfs):
    RN = buildConnectivityResidualNetwork(V, E)
    while(True):
        (parents, flow) = dfs(RN, s, t)
        if (parents[t] == -1):
            break
        path = createPath(s, t, parents)
        updateResidualNetwork(RN, path, flow)
    result = 0
    for edge in RN[t]:
        result += edge[1]
        result -= RN[edge[0]][edge[2]][1]
    return result

def connectivity(V, E):
    result = maxsize

    for u in range(1, V + 1):
        for v in range(u + 1, V + 1):
            tmp = connectivityFordFulkerson(V, E, u, v, dfs)
            if tmp < result:
                result = tmp
    return result // 2

print(connectivity(V, E))