import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community

#with open('test/25.txt') as f:
with open('input/25.txt') as f:
    lines = f.readlines()

vertices = set()
edges = set()
for line in lines:
    t = line.split(':')
    start = t[0].strip()
    vertices.add(start)
    ends = [x.strip() for x in t[1].split()]
    for end in ends:
        edges.add((start,end))
        vertices.add(end)

vertices = list(vertices)
vertices.sort()
edges = list(edges)
vmap = {vertices[i]: i for i in range(len(vertices))}
edges = [(vmap[x[0]], vmap[x[1]]) for x in edges]
vertices = [vmap[x] for x in vertices]

G = nx.from_edgelist(edges)

#r = community.kernighan_lin_bisection(G)
#subset = list()
#for edge in edges:
#    count = 0
#    for i in range(2):
#        if edge[i] in r[0]:
#            count += 1
#    if count == 1:
#        print('split')

pos = nx.spring_layout(G, seed=1245643244)

v1 = [k for k,v in pos.items() if v[0] < 0]
v2 = [k for k,v in pos.items() if v[0] >= 0]

for edge in edges:
    count = 0
    for i in range(2):
        if edge[i] in v1:
            count += 1
    if count == 1:
        print('split')
nx.draw(G, pos=pos)
plt.show()

print(len(vertices), len(v1) + len(v2))
answer = len(v1)*len(v2)
print(answer)
