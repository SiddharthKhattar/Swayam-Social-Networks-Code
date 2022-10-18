# Import required modules
import networkx as nx
import matplotlib.pyplot as plt
import random  
import numpy as np



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
G = nx.Graph()
G.add_edges_from(
    [(1, 2), (1, 9), (3, 13), (4, 6),
     (5, 6), (5, 7), (5, 8), (5, 9), 
     (5, 10), (5, 11), (5, 12), (10, 12), 
     (10, 13), (11, 14), (12, 14), 
     (12, 15), (13, 14), (13, 15), 
     (13, 17), (14, 15), (15, 16)])
  
seed = [3,8]

dict_deg = {}
dict_cl = {}
dict_bw = {}
dict_cr = {}

for each in G.nodes():
    dict_deg[each] = G.degree(each)
    dict_cl[each] = nx.closeness_centrality(G,each)
    dict_bw[each] = nx.betweenness_centrality(G,each)
    dict_cr[each] = nx.core_number(G)[each]

dict_cascade= {}

for each in G.nodes():
    c = []
    for num in range(0,1000):
        seed = [each]
        i = ic(G,seed)
        c.append(len(i))
    dict_cascade[each] = np.average(c)    

sorted_dict_cascade = sorted(dict_cascade,key=dict_cascade.get,reverse=True)
sorted_dict_deg = sorted(dict_deg,key=dict_deg.get,reverse=True)
sorted_dict_cl = sorted(dict_cl,key=dict_cl.get,reverse=True)
sorted_dict_bw = sorted(dict_bw,key=dict_bw.get,reverse=True)
sorted_dict_cr = sorted(dict_cr,key=dict_cr.get,reverse=True)
print("Nodes sorted according to degree")
print(sorted_dict_deg)
print("Nodes sorted according to closeness")

print(sorted_dict_cl)
print("Nodes sorted according to betweeness")

print(sorted_dict_bw)
print("Nodes sorted according to cr")

print(sorted_dict_cr)
print("Nodes sorted according to cascade")

print(sorted_dict_cascade)

# ic(G,seed)
