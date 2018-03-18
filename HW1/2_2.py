import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()

l = [np.random.rand() for x in range(130)]

for i, x in enumerate(l):
    G.add_node(i)

for x in range(len(l)):
    for y in range(len(l)):
        if x<y and np.random.rand()<l[x]*l[y]:
            G.add_edge(x,y)

print(G.number_of_edges())
degs = [y for x,y in G.degree()]


#for i, li in enumerate(l):
#    c = li * (np.sum(l)-li)
#    print(li, c, degs[i], degs[i]-c)
print(l)
for x in range(len(l)):
    for y in range(len(l)):
        if x < y:
            print(x, y, l[x]*l[y], (G.degree(x)*G.degree(y))/(np.sum(degs)))


#nx.draw(G, with_labels=True)
#plt.show()

#degs.sort(reverse=True)
#print(degs)