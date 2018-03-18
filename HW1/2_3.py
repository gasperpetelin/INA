import networkx as nx
import numpy as np
import random
import collections
import matplotlib.pyplot as plt
import scipy.misc

G = nx.read_pajek("C:\\Users\\Gasper\\Desktop\\INA\\HW1\\data\\facebook.net")
c = collections.Counter([y for x,y in G.degree()])
k_avg = np.mean([y for x,y in G.degree()])

G_1 = nx.gnm_random_graph(G.number_of_nodes(), G.number_of_edges())
c_1 = collections.Counter([y for x,y in G_1.degree()])

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

G_2 = build_graph(G.number_of_nodes(),k_avg)
c_3 = collections.Counter([y for x,y in G_2.degree()])
c_2 = np.arange(7, 50)

c1_ = np.array([f for k,f in c.items()])
c2_ = np.array([f for k,f in c_1.items()])
c3_ = np.array([f for k,f in c_3.items()])

plt.plot([k for k,f in c_3.items()],c3_/np.sum(c3_), 'o', label='Prefer. attac.')
plt.plot([k for k,f in c.items()],c1_/np.sum(c1_), 'o', label='Facebook')
plt.plot([k for k,f in c_1.items()],c2_/np.sum(c2_), 'o', label='Random')


vc = k_avg**c_2*np.exp(-k_avg)/scipy.misc.factorial(c_2)


plt.legend()
plt.plot(c_2, vc)
plt.yscale('log')
plt.xscale('log')
plt.xlabel("k")
plt.ylabel("pk")
plt.show()
