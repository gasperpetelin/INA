import networkx as nx

#G=nx.read_pajek("test.net")

#print(G.number_of_nodes())

with open("test1.net") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

print(content)


num_of_ver = int(content[0].split(" ")[1])
print(num_of_ver)

main_array = [[] for x in range(num_of_ver)]

print(main_array)

edges = False
for line in content:
    if edges:
        spl = line.split(" ")
        from_edge = int(spl[0])
        to_edge = int(spl[1])

        print(from_edge-1, to_edge-1)

        main_array[from_edge - 1].append(to_edge - 1)
        main_array[to_edge - 1].append(from_edge - 1)


    if line.startswith("*arcs") or line.startswith("*edges"):
        edges = True

print(main_array)

def number_of_nodes(G):
    return len(G)

def number_of_edges(G):
    s = 0
    for a in G:
        s+=len(a)
    return s/2

def avarage_deg(G):
    s = 0
    for a in G:
        s+=len(a)
    return s/(2*len(G))

print(number_of_nodes(main_array))
print(number_of_edges(main_array))
print(avarage_deg(main_array))


def isolated(G):
    s = 0
    for a in G:
        if len(a)==0:
            s+=1
    return s

def pendent(G):
    s = 0
    for a in G:
        if len(a)==1:
            s+=1
    return s

def max(G):
    s = 0
    for a in G:
        if len(a)>s:
            s=len(a)
    return s


print(isolated(main_array))
print(pendent(main_array))
print(max(main_array))

def component(G, node):
    C = set()
    S = set()

    S.add(node)
    while len(S)!=0:
        break

