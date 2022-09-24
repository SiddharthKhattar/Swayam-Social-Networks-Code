import networkx as nx
import matplotlib.pyplot as plt 

def main():
    G = nx.read_edgelist('citation.txt', create_using = nx.DiGraph())

    deg = G.in_degree()
    pr = nx.pagerank(G)

    pr_values = []

    for i in deg.keys():
        pr_values.append(pr[i])

    plt.plot(deg.values(), pr_values, 'ro', markersize = 3)
    plt.xlabel('Degrees of the nodes')  
    plt.ylabel('Page Rank Values of the nodes')  

    plt.show()

main()







