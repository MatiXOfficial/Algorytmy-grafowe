from dimacs import *
from sys import argv

(V, E) = loadWeightedGraph(argv[1])

class Node:
    def __init__(self, i):
        self.edges = {}
        self.vertices = [i]

    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight

    def delEdge(self, to):
        del self.edges[to]

def buildGraph(V, E):
    G = [Node(i) for i in range(V)]
    for (x, y, c) in E:
        G[x].addEdge(y, c)
        G[y].addEdge(x, c)
    return G

def printGraph(G):
    for i in range(1, len(G)):
        if G[i].vertices:
            print(G[i].vertices, ":", G[i].edges)

def verticesNumber(G):
    V = len(G)
    result = 0
    for i in range(1, V):
        if G[i].vertices:
            result += 1

    return result

#G = buildGraph(V+1, E)
#printGraph(G)