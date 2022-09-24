import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

def get_signs_of_tris(tris_list,G):
    # tris_list = [[1,2,3],[4,5,3]]
    # all_signs = [['+','-','+'], []]
    all_signs = []
    for i in range(len(tris_list)):
        temp = []
        temp.append(G[tris_list[i][0]][tris_list[i][1]]['sign'])
        temp.append(G[tris_list[i][1]][tris_list[i][2]]['sign'])
        temp.append(G[tris_list[i][2]][tris_list[i][0]]['sign'])
        all_signs.append(temp)
    return all_signs    



def count_unstable(all_signs):
    stable = 0
    unstable = 0
    for i in range(len(all_signs)):
        if all_signs[i].count('+') == 3 or all_signs[i].count('+') == 1:
            stable +=1
        elif all_signs[i].count('+') == 2 or all_signs[i].count('+') == 0:
            unstable +=1     
    print("Number of stable triangles out of", stable+unstable, "are", stable)
    print("Number of unstable triangles out of", stable+unstable, "are", unstable)    
    return unstable      

def move_a_tri_to_stable(G,tris_list,all_signs):
    found_unstable = False
    while(found_unstable == False):
        index = random.randint(0,len(tris_list) - 1)
        if all_signs[index].count('+') == 2 or all_signs[index].count('+') == 0:
            found_unstable = True
        else:
            continue

    # Moving the unstable triangle to a stable state
    #[1,2,3]
    r = random.randint(1,3)            
    if all_signs[index].count('+') == 2:
        if (r == 1):
            if (G[tris_list[index][0]][tris_list[index][1]]['sign']) == '+':
                (G[tris_list[index][0]][tris_list[index][1]]['sign']) == '-'
            elif (G[tris_list[index][0]][tris_list[index][1]]['sign']) == '-':
                (G[tris_list[index][0]][tris_list[index][1]]['sign']) == '+'
        elif (r == 2):    
            if (G[tris_list[index][1]][tris_list[index][2]]['sign']) == '+':
                (G[tris_list[index][1]][tris_list[index][2]]['sign']) == '-'   
            elif (G[tris_list[index][1]][tris_list[index][2]]['sign']) == '-':
                (G[tris_list[index][1]][tris_list[index][2]]['sign']) == '+'
        elif (r == 3):    
            if (G[tris_list[index][2]][tris_list[index][0]]['sign']) == '+':
                (G[tris_list[index][2]][tris_list[index][0]]['sign']) == '-'   
            elif (G[tris_list[index][2]][tris_list[index][0]]['sign']) == '-':
                (G[tris_list[index][2]][tris_list[index][0]]['sign']) == '+'   

    elif all_signs[index].count('+') == 0:
        if (r == 1):
            G[tris_list[index][0]][tris_list[index][1]]['sign'] == '+'
        elif (r == 2):
            G[tris_list[index][1]][tris_list[index][2]]['sign'] == '+'
        elif (r == 3):
            G[tris_list[index][2]][tris_list[index][0]]['sign'] == '+'

    return G        





# 1) Create a graph with n nodes, where the nodes are the countries

G = nx.Graph()
n = 5
G.add_nodes_from([i for i in range(1,n+1)])
mapping = {1:'India',2:'Bhutan',3:'Pakistan',4:'Argentina',5:'USA',6:'Canada',7:'Antartica',8:'Russia',9:'Egypt',10:'Sri Lanka',11:'Kazakhstan',12:'Morocco',13:'Sudan',14:'China',15:'Romania'}
G = nx.relabel_nodes(G,mapping)

# 2) Make it a complete graph by adding all possible edges. Also, assign '+' or '-' as weights to all the edges randomly.

signs = ['+','-']

for i in G.nodes():
    for j in G.nodes():
        if i != j:
            G.add_edge(i,j, sign = random.choice(signs))

# 3) Display the network

edge_labels = nx.get_edge_attributes(G,'sign')
pos = nx.circular_layout(G)
nx.draw(G,pos,node_size= 3000)
nx.draw_networkx_edge_labels(G,pos,edge_labels = edge_labels,font_size=20, font_color='red')
plt.show()

# 4.1) Get a list of all the triangles in the network

nodes = G.nodes()
tris_list = [list(x) for x in itertools.combinations(nodes,3)]

# 4.2) Store the sign details of all the triangles

all_signs = get_signs_of_tris(tris_list, G)

# 4.3) Count the number of unstable triangles in the network

unstable = count_unstable(all_signs)
unstable_track = [unstable]


# 5) While the number of unstable triangles is not zero, do the following
# 5.1) Choose a triangle in the graph that is unstable.
# 5.2) Make that triangle stable
# 5.3) Count the number of unstable triangles  

while (unstable != 0):
    G = move_a_tri_to_stable(G,tris_list,all_signs)
    all_signs = get_signs_of_tris(tris_list, G)
    print (all_signs)
    unstable = count_unstable(all_signs)
    unstable_track.append(unstable)

plt.bar([i for i in range(len(unstable_track))], unstable_track)
plt.show()




















