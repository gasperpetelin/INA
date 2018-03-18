import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def build_graph(n, k):
    l = []
    for i in range(np.math.ceil(k)+1):
        for j in range(np.math.ceil(k)+1):
            if i<j:
                l.append((i,j))
    for h in range(n - np.math.ceil(k) - 1):
        for x,y in random.sample(l, np.math.ceil(k/2)):
           if bool(random.getrandbits(1)):
               l.append(("n"+str(h), x))
           else:
               l.append(("n" + str(h), y))

    G = nx.Graph()
    for x,y in l:
        G.add_edge(x, y)
    return G

G = build_graph(20, 4)
nx.draw(G, with_labels=True)
plt.show()

