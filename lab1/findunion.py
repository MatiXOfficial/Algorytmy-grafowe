from sys import argv
from dimacs import *

(V, E) = loadWeightedGraph(argv[1])

def printEdges(E):
    for (x, y, c) in E:
        print(x, " -> ", y, " : ", c)

def sortEdges(E):
    E.sort(reverse = True, key = lambda x: x[2])

def makeSets(num):
    return [[i, 0] for i in range(num)]

def find(sets, i):
    if sets[i][0] == i:
        return i
    sets[i][0] = find(sets, sets[i][0])
    return sets[i][0]

def union(sets, i, j):
    i = find(sets, i)
    j = find(sets, j)
    if (sets[i][1] > sets[j][1]):
        sets[j][0] = i
    else:
        sets[i][0] = j
        if (sets[i][1] == sets[j][1]):
            sets[j][1] += 1

def guideProblemFU(V, E):
    s = 1
    t = 2
    sortEdges(E)
    sets = makeSets(V+1)

    i = 0
    while (find(sets, s) != find(sets, t) and i < len(E)):
        union(sets, E[i][0], E[i][1])
        i += 1

    return E[i-1][2]

#print(guideProblemFU(V, E))