import networkx as nx
import numpy as np
G = nx.Graph()

G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)
G.add_node(10)
G.add_node(11)
G.add_node(12)

G.add_edge(0, 1)
G.add_edge(0, 5)
G.add_edge(2, 0)
G.add_edge(2, 3)
G.add_edge(3, 2)
G.add_edge(3, 5)
G.add_edge(4, 2)
G.add_edge(4, 3)
G.add_edge(5, 4)
G.add_edge(6, 0)
G.add_edge(6, 4)
G.add_edge(6, 8)
G.add_edge(6, 9)
G.add_edge(7, 6)
G.add_edge(7, 9)
G.add_edge(8, 6)
G.add_edge(9, 10)
G.add_edge(9, 11)
G.add_edge(10, 12)
G.add_edge(11, 4)
G.add_edge(11, 12)
G.add_edge(12, 9)

def first_DFS(node, G, visit_order, visited):
    if node in visited:
        return
    visited.add(node)
    for n in G.neighbors(node):
        first_DFS(n, G, visit_order, visited)
    visit_order.insert(0, node)

def get_init_order(G):
    visit_order = []
    visited = set()
    for node in G.nodes():
        first_DFS(node, G, visit_order, visited)
    return visit_order

def second_DFS(node, G, result, label):
    if node in  result:
        return
    result[node] = label
    for n in G.neighbors(node):
        second_DFS(n, G, result, label)

def compute_components(G):
    order = get_init_order(G.reverse())
    dc = dict()
    i = 0
    for node in order:
        second_DFS(node, G, dc, i)
        i+=1
    return dc

#CC = nx.strongly_connected_components(G)
#print(G.number_of_edges())

#print(list(CC))

G = nx.read_pajek("karate_club.net")


print(nx.number_connected_components(G))
print(np.max([len(x) for x in nx.connected_components(G)]))

#def weak(G, N, i):
#    C = []
#    S = set()
#    N.remove(i)
#    while len(S)!=0:
#        i =
#        c.append()

ls = []
p = list(nx.all_pairs_shortest_path_length(G))
for x in p:
    n, d = x
    for i,j in d.items():
        ls.append(j)
print(np.mean(ls))

print(nx.average_shortest_path_length(G))

