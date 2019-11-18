from dimacs import *
from sys import argv
from graph import *
from queue import PriorityQueue

(V, E) = loadWeightedGraph(argv[1])

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

def minimumCutPhase(G):
    V = len(G)
    a = 1
    s = a
    t = None
    S = [a]
    sums = [0] * V

    visited = [False] * V
    Q = PriorityQueue()
    Q.put((0, a))

    while Q:
        s = t
        (t, u) = Q.get()
        u = -u
        if visited[t] == False:
            visited[t] = True
            for (v, c) in G[t].edges.items():
                sums[v] += c
                Q.put(())




