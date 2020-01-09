from graph import *
from chordal import *

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

#test_lexBFS("graphs-lab4\chordal")

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

#test_is_chordal("graphs-lab4\chordal")

def test_find_biggest_clique(dir):
    for file in os.listdir(dir):
        name = dir + '\\' + file
        with open(name, 'r') as file2:
            data = file2.readline();
        res = int(data.split(' ')[-1])
        (V, E) = loadWeightedGraph(name)
        G = buildGraph(V+1, E)
        if find_biggest_clique(G) == res:
            print("ok", end = ' - ')
        else:
            print("ERROR", end = ' - ')
        print(file)

#test_find_biggest_clique("graphs-lab4\maxclique")

def test_find_chromatic_number(dir):
    for file in os.listdir(dir):
        name = dir + '\\' + file
        with open(name, 'r') as file2:
            data = file2.readline();
        res = int(data.split(' ')[-1])
        (V, E) = loadWeightedGraph(name)
        G = buildGraph(V+1, E)
        if find_chromatic_number(G) == res:
            print("ok", end = ' - ')
        else:
            print("ERROR", end = ' - ')
        print(file)

test_find_chromatic_number("graphs-lab4\\coloring")
