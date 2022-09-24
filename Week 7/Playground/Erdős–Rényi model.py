# cascade pay off
import networkx as nx
import matplotlib.pyplot as plt


def set_all_B(G):
	for i in G.nodes():
		G.nodes[i]['action'] = 'B'
	return G

def set_A(G, list1):
	for i in list1:
		G.nodes[i]['action'] = 'A'
	return G

def get_colors(G):
	color = []
	for i in G.nodes():
		if (G.nodes[i]['action'] == 'B'):
			color.append('red')
		else:
			color.append('blue')
	return color


G = nx.erdos_renyi_graph(100, 0.05)
nx.write_gml(G, "erdos_graph.gml")

G = nx.read_gml('erdos_graph.gml')
print(G.nodes())

G = set_all_B(G)

# initial adopters
# list1 = ['2', '1', '3','4','5','6','7']
def printValues(x):
	l = list()
	for i in range(1,x+1):
		l.append(str(i))
	return l
		
PV = printValues(5)

G = set_A(G,PV)
colors = get_colors(G)

nx.draw(G, with_labels=1, node_color=colors, node_size=800)
plt.show()

