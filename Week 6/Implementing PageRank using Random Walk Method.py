import networkx as nx
import random
import numpy as np



def add_edges(G,p):
    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                r = random.random()
                if r <= p:
                    G.add_edge(i,j)
                else:
                    continue
    return G

def get_nodes_sorted_by_RW(points):
    # nodes_sorted_by_RW = [points.index(x) for x in sorted(points, reve)]
    points_array = np.array(points)
    nodes_sorted_by_RW = np.argsort(-points_array)
    return nodes_sorted_by_RW

def random_walk(G):
    nodes = G.nodes()
    RW_points = [0 for i in range(G.number_of_nodes())]
    r = random.choice(nodes)
    RW_points[r] += 1
    out = G.out_edges(r)

    c = 0
    while (c != 10000):
        if (len(out)) == 0:
            focus = random.choice(nodes)
        else:
            rl = random.choice(out)    
            focus = rl[l]
        RW_points[focus] += 1
        out = G.out_edges(focus)     
        c += 1

    return RW_points    

def main():

    #1. Create / take a directed graph 
    
    G = nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    G = add_edges(G,0.3)

    #2. Perform a random walk
    RW_points = random_walk(G)


    #3. Get sorted nodes as per points accumulated during random walk

    nodes_sorted_by_RW=get_nodes_sorted_by_RW(RW_points)
    print("nodes_sorted_by_random_walk",nodes_sorted_by_RW)

    #4. Compare the ranks thus obtained  with the ranks obtained from the inbuil PageRnk Method. 

    pr = nx.pagerank(G)
    pr_sorted = sorted(pr.items(), key = lambda x:x[l], reverse = True)    
    for i in pr_sorted:
        print (i[0])

main()



























































