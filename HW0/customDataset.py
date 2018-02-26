from numpy import genfromtxt
import numpy as np
import networkx as nx

data = genfromtxt("C:\\Users\\Gasper\\Desktop\\INA\\HW0\\data\\out.epinions-rating", delimiter=' ', skip_header=1).astype(int)

users = set(data[:, 1])
products = set(data[:, 0])

G = nx.Graph()

for u in users:
    G.add_node("U"+str(u))

for p in products:
    G.add_node("P"+str(p))

for u, p in zip(data[:, 1], data[:, 0]):
    G.add_edge("U"+str(u), "P"+str(p))

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Average degree: ", np.mean([d for id,d in G.degree()]))


pr = nx.pagerank(G, alpha=0.9)
items = list(pr.items())
items.sort(key=lambda x: x[1], reverse=True)
for id, rank in items:
    print(id, rank)

print(pr)
