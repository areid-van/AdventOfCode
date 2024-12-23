from itertools import combinations

with open('input/23.txt') as f:
    lines = f.readlines()

computers = set()
connections = set()
for line in lines:
    cc = line.strip().split('-')
    cc.sort()
    computers.add(cc[0])
    computers.add(cc[1])
    connections.add(tuple(cc))

groups = 0
for triad in combinations(computers,3):

    if sum([x[0] == 't' for x in triad]) == 0:
        continue

    fully_connected = True
    for pair in combinations(triad,2):
        if not pair in connections and not pair[::-1] in connections:
            fully_connected = False
            break
            
    if fully_connected:
        groups += 1

print('Answer: ', groups)
