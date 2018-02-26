import numpy as np
import networkx as nx
G=nx.karate_club_graph()
pr = nx.pagerank(G, alpha=0.9)

items = list(pr.items())
items.sort(key=lambda x: x[1], reverse=True)
for id, rank in items:
    print(id, rank)
