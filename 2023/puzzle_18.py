import re
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=1000000, linewidth=1000)

steps = {'U': (0, -1),
         'D': (0, 1),
         'L': (-1, 0),
         'R': (1, 0)}

#with open('test/18.txt') as f:
with open('input/18.txt') as f:
    lines = f.readlines()

commands = list()
for line in lines:
    match = re.match('([UDLR]) ([0-9]+) \(#([0-9a-f]{6})\)', line)
    if match:
        commands.append((match[1], int(match[2]), match[3]))

path = [(0,0)]

for command in commands:
    step = steps[command[0]]
    for i in range(command[1]):
        pos = path[-1]
        path.append((pos[0]+step[0], pos[1]+step[1]))

xmin = min([x[0] for x in path])
xmax = max([x[0] for x in path]) - xmin + 1
ymin = min([x[1] for x in path])
ymax = max([x[1] for x in path]) - ymin + 1
path = [(x[0]-xmin, x[1]-ymin) for x in path]

mymap = np.zeros((xmax, ymax), dtype=int)
for x in path:
    mymap[x] = 1

history = set()
points = [(300,300)]

while len(points) > 0:
    newpoints = list()
    for point in points:
        for step in steps.values():
            newpos = (point[0]+step[0], point[1]+step[1])
            if newpos[0] < 0 or newpos[0]>=xmax or newpos[1] < 0 or newpos[1] >= ymax:
                continue
            if not newpos in history and not mymap[newpos]:
                mymap[newpos] = 1
                newpoints.append(newpos)
    points = newpoints


print(np.sum(mymap))
#print([np.sum(mymap[:,i]) for i in range(ymax)])
