from dimacs import *
from sys import argv
from sys import maxsize
from collections import deque

(V, E) = loadDirectedWeightedGraph(argv[1])

def buildGraph(V, E):
    G = [[] for i in range(V + 1)]
    for (x, y, c) in E:
        G[x].append((y, c, 0))
    return G

def dfs(Gr, s, t):
    V = len(Gr)
    parents = [-1] * V
    visited = [False] * V
    flow = [maxsize] * V
    dfsVisit(Gr, s, visited, parents, flow)
    return (parents, flow[t])

def dfsVisit(Gr, s, visited, parents, flow):
    visited[s] = True
    for v in Gr[s]:
        if visited[v[0]] == False and v[1] > 0:
            parents[v[0]] = s
            if (flow[v[0]] > min(flow[s], v[1])):
                flow[v[0]] = min(flow[s], v[1])
            dfsVisit(Gr, v[0], visited, parents, flow)

def bfs(Gr, s, t):
    V = len(Gr)
    parents = [-1] * V
    visited = [False] * V
    flow = [maxsize] * V
    Q = deque()
    Q.append(s)
    while(Q):
        u = Q.popleft()
        visited[u] = True
        for (v, f) in Gr[u]:
            if visited[v] == False and f > 0:
                Q.append(v)
                parents[v] = u
                if flow[v] > min(flow[u], f):
                    flow[v] = min(flow[u], f)
    return (parents, flow[t])