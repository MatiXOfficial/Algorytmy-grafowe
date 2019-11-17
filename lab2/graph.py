from dimacs import *
from sys import argv
from sys import maxsize
from collections import deque

def dfs(RN, s, t):
    V = len(RN)
    parents = [-1] * V
    visited = [False] * V
    flow = [maxsize] * V
    dfsVisit(RN, s, visited, parents, flow)
    return (parents, flow[t])

def dfsVisit(RN, s, visited, parents, flow):
    visited[s] = True
    for (v, f, i, ni) in RN[s]:
        if visited[v] == False and f > 0:
            parents[v] = s
            if (flow[v] > min(flow[s], f)):
                flow[v] = min(flow[s], f)
            dfsVisit(RN, v, visited, parents, flow)

def bfs(RN, s, t):
    V = len(RN)
    parents = [-1] * V
    visited = [False] * V
    flow = [maxsize] * V
    Q = deque()
    Q.append(s)
    while(Q):
        u = Q.popleft()
        visited[u] = True
        for (v, f, i, ni) in RN[u]:
            if visited[v] == False and f > 0:
                Q.append(v)
                parents[v] = u
                if flow[v] > min(flow[u], f):
                    flow[v] = min(flow[u], f)
    return (parents, flow[t])