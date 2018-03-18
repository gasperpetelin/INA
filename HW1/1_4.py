import networkx as nx

G = nx.Graph()

#G.add_node(1)
#G.add_node(2)
#G.add_node(3)
#G.add_node(4)
#G.add_node(5)
#G.add_node(6)
#G.add_node(7)
#
#G.add_edge(1,2)
#G.add_edge(2,3)
#G.add_edge(2,4)
#G.add_edge(2,5)
#G.add_edge(4,5)
#G.add_edge(4,6)
#G.add_edge(4,7)
#G.add_edge(5,7)

#G.add_node(1)
#G.add_node(2)
#G.add_edge(1,2)
#
#for x in range(2,200):
#    G.add_node(x)
#    G.add_edge(1, x)
#    G.add_edge(2, x)
#    print(nx.average_clustering(G), nx.transitivity(G))

G.add_node(1)

for x in range(2, 400, 2):
    #print(x, x+1)
    G.add_node(x)
    G.add_node(x+1)
    G.add_edge(1, x)
    G.add_edge(1, x+1)
    G.add_edge(x, x+1)
    print(nx.average_clustering(G), nx.transitivity(G))

