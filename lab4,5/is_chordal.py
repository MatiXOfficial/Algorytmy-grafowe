from dimacs import *
import os
from graph import *

def find_RN(G, vs, i):
    neigh = G[vs[i]].out
    prev = {vs[j] for j in range(i)}
    return neigh & prev

def find_parent(RN, vs, i):
    for j in range(i - 1, -1, -1):
        if vs[j] in RN:
            return j

def is_chordal(G):
    V = len(G)
    vs = lexBFS(G)
    RN = [set()] * (V - 1)
    parent = [None] * (V - 1)
    for i in range(1, V - 1):
        u = vs[i]
        RN[i] = find_RN(G, vs, i)
        parent[i] = find_parent(RN[i], vs, i)
        if not RN[i] - {vs[parent[i]]} <= RN[parent[i]]:
            return False
    return True

def test_is_chordal(dir):
    for file in os.listdir(dir):
        name = dir + '\\' + file
        with open(name, 'r') as file2:
            data = file2.readline();
        res = True if int(data.split(' ')[-1]) == 1 else False
        (V, E) = loadWeightedGraph(name)
        G = buildGraph(V+1, E)
        if is_chordal(G) == res:
            print("ok", end = ' - ')
        else:
            print("ERROR", end = ' - ')
        print(file)


test_is_chordal("graphs-lab4\chordal")
