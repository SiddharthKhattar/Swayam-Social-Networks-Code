# Import required modules
import networkx as nx
import matplotlib.pyplot as plt
import random  

def ic(G,s):
    print(s)
    jst_inf = list(s)
    infected = list(s)
    while(1):
        print(jst_inf,infected)
        if len(jst_inf) == 0:
            print(infected)
            return infected
        tmp = []
        for each in jst_inf:
            for each1 in G.neighbors(each):
                r = random.uniform(0,1)
                if r < 0.5 and each1 not in infected and each1 not in tmp:
                    tmp.append(each1)
                for each in tmp: 
                    infected.append(each)
                jst_inf = list(tmp)

  
# Check if there is any node left with degree d
def check(h, d):
    f = 0  # there is no node of deg <= d
    for i in h.nodes():
        if (h.degree(i) <= d):
            f = 1
            break
    return f
  
  
# Find list of nodes with particular degree
def find_nodes(h, it):
    set1 = []
    for i in h.nodes():
        if (h.degree(i) <= it):
            set1.append(i)
    return set1
  
  
# Create graph object and add nodes
g = nx.Graph()
g.add_edges_from(
    [(1, 2), (1, 9), (3, 13), (4, 6),
     (5, 6), (5, 7), (5, 8), (5, 9), 
     (5, 10), (5, 11), (5, 12), (10, 12), 
     (10, 13), (11, 14), (12, 14), 
     (12, 15), (13, 14), (13, 15), 
     (13, 17), (14, 15), (15, 16)])
  
seed = [3,8]

ic(g,seed)
