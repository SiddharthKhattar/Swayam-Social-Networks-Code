import networkx as nx
import itertools



def communities_brute(G):
    nodes = G.nodes()
    n = G.number_of_nodes()

    first_community = []
    for i in range(1, n/2 + 1):
        comb = [list(x) for x in itertools.combinations(nodes, i)]
        first_community.extend(comb)

    second_community = []

    for i in range(len(first_community)):
        l = list(set(nodes) - set(first_community[i]))
        second_community.append(l)

    #which division is the best?
    num_intra_edges1 = []
    num_intra_edges2 = []
    num_inter_edges = []
    ratio = [] # ratio of number of intra/number of inter community edges

    for i in range(len(first_community)):
        num_intra_edges1(G.subgraph(first_community[i]).number_of_edges())

    for i in range(len(first_community)):
        num_intra_edges2(G.subgraph(second_community[i]).number_of_edges())\

    e = G.number_of_edges()   

    for i in range(len(first_community)):     
        num_inter_edges.append( - num_intra_edges1[i] - num_intra_edges2[i])

    # Find the ratio

    for i in range(len(first_community)):
        ratio.append((float)(num_intra_edges1[i] + num_intra_edges2[i])/num_inter_edges[i])

    max_value = max(ratio)
    max_index = ratio.index(max_value)

    print ("(" , first_community[max_index] , "),(" , second_community[max_index] , ")" )


G = nx.barbell_graph(15,15)
nx.draw(G)
import matplotlib.pyplot as plt
plt.show() 



# for i in itertools.combinations([1,2,3,4],2):
#     print (i)
# for i in itertools.combinations([1,2,3,4],3):
#     print (list(i))






