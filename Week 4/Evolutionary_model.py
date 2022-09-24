import networkx as nx
import matplotlib.pyplot as plt
import random



def create_graph():
    G = nx.Graph()
    # G.add_nodes_from(range(1,100))
    for i in range(1,101):
        G.add_node(i)
    return G

def visualize(G,labeldict,nodesize,color_arra):
    nx.draw(G,labels=labeldict,node_size = nodesize,node_color=color_arra)

    plt.show()

def assign_bmi(G):
    for each in G.nodes():
        G._node[each]['name'] = random.randint(15,40)
        G._node[each]['type'] = 'person'

def get_labels(G):
    dict1 = {}
    for each in G.nodes():
        dict1[each] = G._node[each]['name']
    return dict1

def get_size(G):
    array1=[]
    for each in G.nodes():
        # array1.append(G._node[each]['name'] * 20)
        if G._node[each]['type'] == 'person':
            array1.append(G._node[each]['name']*20)
        else:
            array1.append(1000)

def add_foci_nodes(G):
    n = G.number_of_nodes()
    i = n + 1
    foci_nodes=['gym','eatout','movie_club','karate_club','yoga_club']
    for j in range(0,5):
        G.add_node(i)
        G._node[i]['name'] = foci_nodes[j]
        G._node[i]['type'] = 'foci'
        i = i+1

def get_colors(G):
    c=[]
    for each in G.nodes():
        if G._node[each]['type'] == 'person':
            if G._node[each]['name'] == 15:
                c.append('green')
            elif G._node[each]['name'] == 40:
                c.append('yellow')
            else:
                c.append('blue')
        else:
            c.append('red')
    return c            

def get_foci_nodes():
    f = []
    for each in G.nodes():
        if G._node[each]['type'] == 'foci':
            f.append(each)
    return f    

def get_persons_nodes():
    p = []
    for each in G.nodes():
        if G._node[each]['type'] == 'person':
            f.append(each)
    return f    

def add_foci_edges():
    foci_nodes = get_foci_nodes()
    person_nodes= get_persons_nodes()
    for each in person_nodes:
        r = random.choice(foci_nodes)
        G.add_edge(each,r)

def homophily(G):
    pnodes = get_persons_nodes()
    for u in pnodes:
        for v in pnodes:
            if u != v:
                diff=abs(G._node[u]['name'] - G._node[v]['name'])
                p = float(1) / (diff+1000)
                r = random.uniform(0,1)
                if r < p:
                    G.add_edge(u,v)












G = create_graph()
assign_bmi(G)
add_foci_nodes(G)
labeldict = get_labels(G)
nodesize=get_size(G)
color_array= get_colors(G)
homophily(G)
add_foci_edges()
visualize(G,labeldict,nodesize,color_array)
# labeldict=get_labels(G,labeldict)
