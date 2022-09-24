import networkx as nx

def edge_to_remove(G):
    dict1 = nx.edge_betweenness_centrality(G)
    list_of_tuples = dict1.items()
    list_of_tuples.sort(key = lambda x:x[1], reverse = True)
    return list_of_tuples[0][0] #(a,b)
    

def girvan(G):
   c = nx.connected_component_subgraphs(G)
   l = len(c)
   print("The number of connected components are: " , l)

   while (l == 1):
        G.remove_edge(*edge_to_remove(G)) # ((a,b)) --> (a,b)
        c = nx.connected_components_subgraphs(G)
        # c = G.subgraph(c) for c in connected_components(G))
        l = len(c)
        print(" The number of connected components are" , l)
   return c     

G = nx.barbell_graph(5,0)
c = girvan(G)

for i in c:
    print(i.nodes())
    print("...........")

 # The problem with the above code is that networkx version 2.8.5 does not 
 # support  c = nx.connected_components_subgraphs(G) as it has been removed completely from the library
 # A way to get around this would be downgrading network version but
 # that results in another error as the inbuilt python library for fraction now no longer supports it




















