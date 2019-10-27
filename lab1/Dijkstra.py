#Only Dijsktra's algorithm implementation

from sys import argv
from sys import maxsize
from dimacs import *
from queue import PriorityQueue

def buildGraph(V, E):
    G = [[] for i in range(V + 1)]
    for (x, y, c) in E:
        G[x].append((y, c))
        G[y].append((x, c))
    return G

(V, E) = loadWeightedGraph(argv[1])

G = buildGraph(V, E)

def dijkstra(G, s):
    V = len(G)
    distance = [maxsize] * (V)
    parent = [-1] * (V)
    distance[s] = 0

    Q = PriorityQueue() 
    Q.put((s, distance[s]))

    for i in range(V):
        if (Q.empty()):
            break
        u = Q.get()
        for v in G[u[0]]:
            if (distance[v[0]] > distance[u[0]] + v[1]):
                distance[v[0]] = distance[u[0]] + v[1]
                parent[v[0]] = u[0]
                Q.put(v)

    return (distance, parent)

(distance, parent) = dijkstra(G, 1)

print(distance[1:])
print(parent[1:])