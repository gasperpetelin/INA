import numpy as np
import networkx as nx

G = nx.gnm_random_graph(int(876252), int(13668320))

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Average degree: ", np.mean([d for id,d in G.degree()]))


pr = nx.pagerank(G, alpha=0.9)
items = list(pr.items())
items.sort(key=lambda x: x[1], reverse=True)

print(items)

for x,y in items[:10]:
    print(x, y)

print(np.sum([y for x,y in items]))

