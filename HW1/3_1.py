import networkx as nx
import numpy as np
import random
import collections
import matplotlib.pyplot as plt
import scipy.misc

G = nx.read_adjlist("path")

def read_real_values():
    with open("path", encoding="UTF-8") as f:
        lines = [x.strip() for x in f.readlines() if x.startswith("#")]
        for l in lines:
            h = l.split("\"")
            yield h[0][1:].strip(), float(h[2].strip())

vals = list(read_real_values())

c1 = [(int(x),y) for x,y in nx.clustering(G).items()]
c1.sort()


c2 = [(int(x), y) for x,y in nx.degree(G)]
c2.sort()


c3 = [(int(x), y) for x,y in nx.closeness_centrality(G).items()]
c3.sort()


c4 = [(int(x), y) for x,y in nx.betweenness_centrality(G).items()]
c4.sort()


c5 = [(int(x), y) for x,y in nx.pagerank(G).items()]
c5.sort()




c2_cor = np.corrcoef([y for x,y in vals], [y for x,y in c2])[0,1]
c3_cor = np.corrcoef([y for x,y in vals], [y for x,y in c3])[0,1]
c4_cor = np.corrcoef([y for x,y in vals], [y for x,y in c4])[0,1]
c5_cor = np.corrcoef([y for x,y in vals], [y for x,y in c5])[0,1]

print(c2_cor)
print(c3_cor)
print(c4_cor)
print(c5_cor)





#nx.draw(G, with_labels=True)
#plt.show()