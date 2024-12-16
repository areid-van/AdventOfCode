import re
import numpy as np

cmap = {'.' : 0,
        '#' : 1,
        '<' : 2,
        '>' : 3,
        '^' : 4,
        'v' : 5}

steps = {2 : (-1, 0),
         3 : (1, 0),
         4 : (0, -1),
         5 : (0, 1)}

#with open('test/23.txt') as f:
with open('input/23.txt') as f:
    lines = f.readlines()

rows = list()
for line in lines:
    rows.append([cmap[x] for x in line.strip()])

grid = np.stack(rows).T
nx, ny = grid.shape

paths = [(set([(1,0)]), (1,1), 1)]

answer = 0
while len(paths) > 0:
    newpaths = list()
    for path in paths:
        hist = path[0]
        pos = path[1]
        d = path[2]
        newhist = hist | set([pos])
        for step in steps.values():
            newpos = (pos[0]+step[0], pos[1]+step[1])
            if newpos[0] < 0 or newpos[0] >= nx or newpos[1]<0 or newpos[1]>=ny:
                answer = max(answer, d)
                print('finish', answer)
            elif (grid[newpos] != 1) and (not newpos in hist):
                newpaths.append((newhist, newpos, d+1))
    paths = newpaths
    print(len(paths))

print(answer)
        

