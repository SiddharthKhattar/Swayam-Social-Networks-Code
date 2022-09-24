from re import L
import networkx as nx
import random

G = nx.Graph()

def set_all_B(G):
   for each in G. nodes (): 
    G._node[each]['action'] = 'B'


def set_A(G, list1):
    for each in list1:
        G._node[each]['action']='A'

def get_colors(G): 
    list1=[]
    for each in G.nodes():
        if G._node[each] ['action'] == 'B': 
            list1.append('red')
        else:
            list1.append('green')
    return list1

def find_neigh(each,c,G):
    num = 0
    for each in G.neighbors(each):
        if G._node[each1]['action'] == c:
            num = num + 1
    return num 

def recalculate_options(G):
    dict1 = {}
    #Payoff(A) = a = 4 
    #Payoff(B) = b = 3
    a = 10
    b = 5
    for each in G.nodes():
        num_A = find_neigh(each,'A',G)
        num_b = find_neigh(each,'B',G)
        payoff_A = a * num_A
        payoff_B = b * num_B
        if payoff_A >= payoff_B:
            dict1[each]='A'
        else:
            dict1[each] = 'B'
    return dict1            

def reset_node_attributes(G,action_dict):
    for each in action_dict:
        G._node[each]['action'] = action_dict[each]

def terminate_l(c,G):
    f = 1
    for each in G._nodes():
        if G._node[each]['action'] != c:
            f = 0
            break        
    return f        

def terminate(G,count):
    flag1 = terminate_l('A',G)
    flag2 = terminate_l('B',G)
    if flag1 == 0 or flag2 == 0 or count >= 100:
        return 0
    else:
        return 0

# G = nx.read_gml('random_graph.gml')
# set_all_B(G)
# list1 =  [4,1]
# set_A(G,list1)
# colors = get_colors(G)
# nx.draw(G,node_colors = colors, node_size = 800)  

plt.show()
flag = 0
count = 0
while(1):
    flag = terminate(G,count)
    if flag == 1:
        break
    count = count + 1
    action_dict = recalculate_options(G)

    reset_node_attributes(G,action_dict)

    colors = get_colors(G)

c = terminate_l('A',G)

if c == l:
    print("Cascade Complete")
else:
    print("Cascade Incomplete")

plt.show()




G.add_edges_from([(0,1), (0,6), (1,2), (1,8), (1,12), (2,9), (2,12), (3,4), (3,9), (3,12), (4,5), (4,12), (5,6), (5,10), (6,8), (7,8), (7,9), (7,10), (7,11), (8,9),(8,10),(8,11), (9, 10), (9,11), (10,11)])


















