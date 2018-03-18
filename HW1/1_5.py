from queue import Queue

import networkx as nx
import numpy as np

G = nx.read_edgelist("C:\\Users\\Gasper\\Desktop\\INA\\HW1\\data\\aps_2010_2013")
print(np.mean([x for y,x in G.degree()]))
#G = nx.Graph()
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

#print(G.number_of_nodes(), G.number_of_edges())

#print(nx.single_source_shortest_path_length(G, 1))

#G.nodes()

#G = nx.circular_ladder_graph(400)
#print(G.number_of_nodes())
#print(nx.is_directed(G))

#def DFS(G, node):
#    D = dict()
#    Q = Queue()
#    Q.put(node)
#    D[node] = 0
#    while not Q.empty():
#        i = Q.get()
#        for j in G.neighbors(i):
#            if j not in D and len(D)<0.9*G.number_of_nodes():
#                D[j] = D[i] + 1
#                Q.put(j)
#    return D
#
#def diameter(G):
#    max_d = 0
#    c = 0
#    for n in G.nodes():
#        print(c)
#        c+=1
#        max_d = max(max_d, np.max([y for x,y in  DFS(G, n).items()]))
#    return max_d

#print(diameter(G))
#print(nx.diameter(G))


