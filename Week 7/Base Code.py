import networkx as nx
import matplotlib.pyplot as plt
# G = nx.erdos_renyi_graph(10,0.5)
# nx.write_gml(G,'random_graph.gml')

def set_all_B(G):
    for each in G.nodes():
        G._node[each]['label'] = 'B'

def set_A(G,list1):
    for each in list1:
        G._node[each]['label'] = 'A'
 
def get_colors(G):
    list1 = []
    for each in G.nodes():
        if G._node[each]['label'] == "B":
            list1.append('red')
        else:
            list1.append('green')   
    return list1         


G = nx.read_gml('random_graph.gml')
set_all_B(G)
list1 = [3,7]
set_A(G,list1)
colors = get_colors(G)

nx.draw(G,node_color = colors, node_size = 800)

plt.show()
















