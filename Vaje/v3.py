from collections import defaultdict

import networkx as nx
import numpy as np
G = nx.read_pajek("C:\\Users\\Gasper\\Desktop\\INA\\Vaje\\collaboration_imdb.net")

print(G.number_of_nodes())


def print_d(G, m, n):
    l = [(v, k) for k, v in m(G).items()]
    l.sort(key=lambda x: x[0], reverse=True)
    for x in l[:n]:
        print(x)

#print_d(G, nx.eigenvector_centrality, 20)

#print(nx.triangles(G, nodes=['Boy, T.T.']))

def EC(G):
    E  = defaultdict(lambda: 1)#np.ones(G.number_of_nodes())
    for _ in range(300):
        U = defaultdict(lambda: 0)#np.zeros(G.number_of_nodes())
        for i in G.nodes():
            for j in G.neighbors(i):
                U[i] = U[i] + E[j]
        U_sum = np.mean([y for x,y in U.items()])
        for i in U.keys():
            U[i] = U[i]* G.number_of_nodes()/U_sum

        E = U
    return E




print_d(G, EC, 20)

