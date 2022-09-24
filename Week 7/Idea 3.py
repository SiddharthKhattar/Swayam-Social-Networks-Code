# This doesn't work properly in this state

import networkx as nx
# import random
import matplotlib.pyplot as plt


# cascade key people

# G = nx.erdos_renyi_graph(10, 0.5)
# nx.write_gml(G, "erdos_graph.gml")

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
			color.append('green')
	return color


def recalculate(G):
	dict1 = {}
	
	# payoff(A)=a=4
	# payoff(B)=b=3
	a = 10
	b = 5
	for i in G.nodes():
		neigh = G.neighbors(i)
		count_A = 0
		count_B = 0

		for j in neigh:
			if (G.nodes[j]['action'] == 'A'):
				count_A += 1
			else:
				count_B += 1

		payoff_A = a * count_A
		payoff_B = b * count_B

		if (payoff_A >= payoff_B):
			dict1[i] = 'A'
		else:
			dict1[i] = 'B'

	return dict1


def reset_node_attributes(G, action_dict):
	
	for i in action_dict:
		G.nodes[i]['action'] = action_dict[i]
	return G


def Calculate(G):
	continuee = True
	count = 0
	c = 0

	while (continuee and count < 100):
		count += 1
		
		# action_dict will hold a dictionary
		action_dict = recalculate(G)
		G = reset_node_attributes(G, action_dict)
		colors = get_colors(G)
		
		if (colors.count('red') == len(colors) or colors.count('green') == len(colors)):
			continuee = False
			if (colors.count('green') == len(colors)):
				c = 1

	if (c == 1):
		print('cascade complete')
	else:
		print('cascade incomplete')


G = nx.read_gml('random_graph_with_communities.gml')

for i in G.nodes():
	for j in G.nodes():
		if (i < j):
			list1 = []
			list1.append(i)
			list1.append(j)
			print(list1, ':', end="")

			G = set_all_B(G)
			G = set_A(G, list1)
			colors = get_colors(G)
			Calculate(G)
			list1=[0,1]
	nx.draw(G,node_color=colors,with_labels=1)
	plt.show()






# def create_first_community(G):
#     for i in range(0,10):
#         G.add_node(i)
#     for i in range(0,10):
#         for j in range(0,10):
#             if i < j:
#                 r = random.uniform(0,1)
#                 if r < 0.5:
#                     G.add_edge(i,j)

# def create_second_community(G):
#     for i in range(11,20):
#         G.add_node(i)
#     for i in range(11,20):
#         for j in range(11,20):
#             if i < j:
#                 r = random.uniform(0,1)
#                 if r < 0.5:
#                     G.add_edge(i,j)



# G = nx.Graph()
# create_first_community(G)
# create_second_community(G)
# G.add_edge(5,15)



# nx.write_gml(G,'random_graph_with_communities.gml')





