from dimacs import *
import os

class Node:
  def __init__(self, idx):
    self.idx = idx
    self.out = set()              # zbiór sąsiadów

  def connect_to(self, v):
    self.out.add(v)

def buildGraph(V, E):
    G = [Node(i) for i in range(V)]
    for (x, y, c) in E:
        G[x].connect_to(y)
        G[y].connect_to(x)
    return G

def printGraph(G):
    for i in range(1, len(G)):
        print(i, ":", G[i].out)

def lexBFS(G, s = 1):
    V = len(G)
    sets = [{i for i in range(V)} - {s}, {s}]
    visited = []
    while sets:
        u = sets[-1].pop()
        visited.append(u)
        new_sets = []
        for set in sets:
            if set - G[u].out:
                new_sets.append(set - G[u].out)
            if set & G[u].out:
                new_sets.append(set & G[u].out)
        sets = new_sets
    return visited

