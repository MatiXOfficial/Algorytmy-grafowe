from dimacs import *
from sys import argv

(V, E) = loadWeightedGraph(argv[1])

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

def _lexBFS(G, s = 1):
    V = len(G)
    sets = [{i for i in range(V)} - {s}, {s}]
    visited = []
    while sets:
        u = sets[-1].pop()
        visited.append(u)
        i = 0
        while i < len(sets):
            set = sets[i]
            sets.pop(i)
            if set - G[u].out:
                sets.insert(i, set - G[u].out)
                i += 1
            if set & G[u].out:
                sets.insert(i, set & G[u].out)
                i += 1
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

def find_RN(G, vs, u):
    neigh = G[u].out
    prev = {vs[i] for i in range(u)}
    return neigh & prev

def parent(G, RN, vs, u):
    for i in range(u - 1, -1, -1):
        if vs[i] in RN:
            return vs[i]

    

def is_chordal(G):
    V = len(G)
    vs = lexBFS(G)
    for i in range(1, V - 1):
        u = vs[i]
        RN = find_RN(G, vs, u)
        parent = parent(G, RN, vs, u)
        if not RN - parent in find_RN(G, vs, parent):
            return False
    return True





G = buildGraph(V+1, E)
vs = lexBFS(G)
print(vs)
print(checkLexBFS(G, vs))