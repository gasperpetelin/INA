import networkx as nx

#G = nx.read_edgelist("C:\\Users\\Gasper\\Desktop\\INA\\HW1\\data\\test_v.dpl", comments='#')
G = nx.read_pajek("C:\\Users\\Gasper\\Desktop\\INA\\HW1\\data\\enr_paj.net")


CC = list(nx.strongly_connected_components(G))
print(G.number_of_edges())

print(CC)
print(len(CC))
print([len(x) for x in CC if len(x)!=1])
print(max([len(x) for x in CC]))





