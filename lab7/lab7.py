import networkx as nx
from networkx.algorithms.components import strongly_connected_components
from networkx.algorithms.dag import topological_sort
from dimacs import *

(V,F) = loadCNFFormula("sat\\sat\\sat100_100")

G = nx.DiGraph()

for [a, b] in F:
    G.add_edges_from([[-a, b], [-b, a]])

def is_valid(G):
    SCC = strongly_connected_components(G)
    for S in SCC:
        for u in S:
            if -u in G.nodes():
                return False
    return True

def find_validity(G):
    H = nx.DiGraph()
    SCC = strongly_connected_components(G)
    SCC = [S for S in SCC]
    H.add_nodes_from([i for i in range(len(SCC))])
    for i in range(len(SCC)):
        for j in range(len(SCC)):
            if i == j: continue
            for u in SCC[i]:
                for v in SCC[j]:
                    if G.has_edge(u, v):
                        H.add_edge(i, j)
    O = topological_sort(H)
    validity = {node : None for node in G.nodes() if node > 0}
    for i in O:
        for u in SCC[i]:
            if u > 0 and validity[u] == None:
                validity[u] = False
            if u < 0 and validity[-u] == None:
                validity[-u] = True
    return validity
        
def is_validity_good(G, validity):
    for [a, b] in G.edges():
        if a > 0:
            a = validity[a]
        else:
            a = not validity[-a]
        if b > 0:
            b = validity[b]
        else:
            b = not validity[-b]
        if a == True and b == False:
            return False
    return True

print(is_validity_good(G, find_validity(G)))