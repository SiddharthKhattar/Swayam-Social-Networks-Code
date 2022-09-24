from itertools import count
import networkx as nx
import matplotlib.pyplot as plt

# G= nx.read_edgelist('Data_sets/facebook_combined.txt')
# G= nx.read_pajek ('Data_sets/football.net')
# G= nx.read_pajek ('Data_sets/karate.paj ')
G= nx.read_gml('Data_sets/karate.gml',label="id")

# def plot_deg_dist(G):
#     all_degrees= nx.degree(G)
#     unique_degrees = list(set(all_degrees))

#     count_of_degrees = []

#     for i in unique_degrees:
#         x = all_degrees.count(i)
#         count_of_degrees.append(x)

#     plt.plot(unique_degrees, count_of_degrees)    
#     plt.show()



# print (nx.info(G))
# print (nx.number_of_nodes(G))
# print (nx.is_directed(G))
# nx.draw(G)
# print (nx.degree(G) )
# my_degrees=G.degree()
# degree_values = [v for k, v in my_degrees]
# print (my_degrees())
# plt.show()


# plot_deg_dist(G)

# for i in nx.clustering(G).items():
#     print (i)


# print (nx.average_clustering(G))
print (nx.diameter(G))