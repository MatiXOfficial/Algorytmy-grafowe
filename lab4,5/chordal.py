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

def find_biggest_clique(G):
    V = len(G)
    vs = lexBFS(G)
    result = 0
    for i in range(1, V - 1):
        u = vs[i]
        RN = find_RN(G, vs, i)
        if len(RN) + 1 > result:
            result = len(RN) + 1
    return result

def find_chromatic_number(G):
    V = len(G)
    color = [0] * (V)
    vs = lexBFS(G)
    for v in vs:
        N = G[v].out;
        used = {color[u] for u in N}
        for c in range(1, V):
            if not c in used:
                color[v] = c
                break
    return max(color)

def find_vcover(G):
    vs = lexBFS(G)
    vs.reverse()
    I = set()
    for v in vs:
        N = G[v].out;
        if not I & N:
            I.add(v)
    return len(G) - len(I)