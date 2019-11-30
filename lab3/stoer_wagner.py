from dimacs import *
from sys import argv
from sys import maxsize
from graph import *
from queue import PriorityQueue

(V, E) = loadWeightedGraph(argv[1])
G = buildGraph(V+1, E)

def merge(G, i, j): # merges i and j to i
    for (v, c) in G[j].edges.items(): # all edges (j, v) from j
        G[i].vertices += G[j].vertices
        G[j].vertices = []
        if v == i:
            G[i].delEdge(j)
        else:
            c = G[v].edges.get(j)
            G[v].delEdge(j)
            G[v].addEdge(i, c)
            G[i].addEdge(v, c)

def minimumCutPhase(G, a = 1):
    V = len(G)
    u = None
    v = a
    S = [a]
    edges_sum = [0] * V

    visited = [False] * V
    Q = PriorityQueue()
    Q.put((-edges_sum[a], a))

    while not Q.empty():
        u = v
        (k, v) = Q.get()
        if not visited[v]:
            s = u
            t = v
            visited[v] = True
            for (y, c) in G[v].edges.items():
                if not visited[y]:
                    edges_sum[y] += c
                    Q.put((-edges_sum[y], y))

    return (s, t, edges_sum[t])

def minimumCut(G):
    result = maxsize
    while verticesNumber(G) > 1:
        (s, t, c) = minimumCutPhase(G, 1)
        if c < result:
            result = c
        merge(G, s, t)
    return result

print(minimumCut(G))