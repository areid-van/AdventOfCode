import networkx as nx

with open('input/23.txt') as f:
    lines = f.readlines()

G = nx.Graph()
for line in lines:
    edge = line.strip().split('-')
    G.add_edge(edge[0], edge[1])

x = nx.approximation.max_clique(G)
x = list(x)
x.sort()
ans = ','.join(x)
print('Answer: ', ans)
