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

paths = [[[(1,0)], (1,1), None, 0]]

cache = dict()

while len(paths) > 0:
    #print(len(paths))
    hist = paths[-1][0]
    pos = paths[-1][1]
    tookStep = False
    key = (frozenset(sorted(hist)), pos)
    if key in cache:
        print('hit')
        paths[-1][3] = cache[(hist, pos)]
    else:
        newhist = hist + [pos]
        me = len(paths)-1
        for step in steps.values():
            newpos = (pos[0]+step[0], pos[1]+step[1])
            if newpos[0] < 0 or newpos[0] >= nx or newpos[1]<0 or newpos[1]>=ny:
                d = len(hist)
                parent = paths[-1][2]
                paths[parent][3] = max(d, paths[parent][3])
            elif (grid[newpos] != 1) and newpos not in hist:
                paths.append([newhist, newpos, me, 0])
                tookStep = True

    if not tookStep:
        dp = len(hist)
        paths.pop()
        while len(paths) > 0 and len(paths[-1][0])<dp:
            parent = paths[-1][2]
            d = paths[-1][3]
            if parent is not None:
                paths[parent][3] = max(d, paths[parent][3])
            else:
                print(d)
            dp = len(paths[-1][0])
            cache[(frozenset(sorted(paths[-1][0])), paths[-1][1])] = paths[-1][3]
            print(len(cache))
            paths.pop()
            
