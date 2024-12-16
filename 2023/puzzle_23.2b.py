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

paths = [((None, set([(1,0)])), (1,1))]

answer = 0
d = 1
while len(paths) > 0:
    newpaths = list()
    for path in paths:
        hist = path[0]
        pos = path[1]
        if len(hist[1]) >= 50:
            nh = set()
            nh.add(pos)
            newhist = (hist, nh)
        else:
            nh = hist[1].copy()
            nh.add(pos)
            newhist = (hist[0], nh)
        for step in steps.values():
            newpos = (pos[0]+step[0], pos[1]+step[1])
            if newpos[0] < 0 or newpos[0] >= nx or newpos[1]<0 or newpos[1]>=ny:
                answer = max(answer, d)
            elif (grid[newpos] != 1):
                isRepeat = False
                h = hist
                while not h is None:
                    if newpos in h[1]:
                        isRepeat = True
                        break
                    h = h[0]
                if not isRepeat:
                    newpaths.append((newhist, newpos))
    paths = newpaths
    print(d, answer, len(paths))
    d += 1

print(answer)
        

