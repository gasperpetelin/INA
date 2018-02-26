import networkx as nx
import matplotlib.pyplot as plt
G=nx.karate_club_graph()

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

nx.draw(G, with_labels=True)
plt.show()