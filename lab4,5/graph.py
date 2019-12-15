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

def checkLexBFS(G, vs):
  n = len(G)
  pi = [None] * n
  for i, v in enumerate(vs):
    pi[v] = i

  for i in range(n-1):
    for j in range(i+1, n-1):
      Ni = G[vs[i]].out
      Nj = G[vs[j]].out

      verts = [pi[v] for v in Nj - Ni if pi[v] < i]
      if verts:
        viable = [pi[v] for v in Ni - Nj]
        if not viable or min(verts) <= min(viable):
          return False
  return True

def test_lexBFS(dir):
    for file in os.listdir(dir):
        name = dir + '\\' + file
        (V, E) = loadWeightedGraph(name)
        G = buildGraph(V+1, E)
        if checkLexBFS(G, lexBFS(G)) == True:
            print("ok", end = " - ")
        else:
            print("ERROR", end = " - ")
        print(file)

test_lexBFS("graphs-lab4\chordal")