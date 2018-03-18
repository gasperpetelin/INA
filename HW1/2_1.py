import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(2,5)
G.add_edge(4,5)
G.add_edge(4,6)
G.add_edge(4,7)
G.add_edge(5,7)

l = 8*[0]
print(l)

for _ in range(100000):
    x,y = random.sample(G.edges(), 1)[0]
    r = 0
    if bool(random.getrandbits(1)):
        r = x
    else:
        r = y
    l[r]+=1

d = np.array(l)/np.array(l).sum()
print(d, np.sum(d))
nx.draw(G, with_labels=True)


x = np.array([1,4,1,4,3,1,2])/16
print(x, np.sum(x))
