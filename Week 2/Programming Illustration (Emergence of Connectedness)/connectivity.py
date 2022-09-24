import networkx as nx
import random

G = nx.Graph()


#Adding n number of nodes in the graph & returning it
def add_nodes(n):
    G.add_nodes_from(range(n))
    return G

#Add one random edge
def add_random_edge(G):
    v1 = random.choice(G.nodes())
    v2 = random.choice(G.nodes())
    G.add_edge(v1,v2)
    return G

G = add_nodes(5)
print (add_random_edge(G))

print (G.edges())

