import numpy as np
import re

#with open('test/16.txt') as f:
with open('input/16.txt') as f:
    lines = f.readlines()

charmap = {'.': 0,
           '-': 1,
           '|': 2,
           '\\': 3,
           '/': 4}
grid = list()
for line in lines:
    match = re.match("[.|\-/\\\]+", line)
    if match: grid.append([charmap[c] for c in match[0]])

grid = np.stack(grid).T
nx, ny = grid.shape
#print(grid.T)
energy = np.zeros(grid.shape)

sources = [((-1,0),(1,0))]
history = set()
while len(sources) > 0:
    loc, vec = sources.pop()
    while True:
        loc = (loc[0]+vec[0], loc[1]+vec[1])
        if loc[0] < 0 or loc[0] >= nx or loc[1]<0 or loc[1]>=ny:
            break
        energy[loc] = 1
        if grid[loc] == 1:
            if vec == (0,1) or vec == (0,-1):
                sources.insert(0,(loc, (-1, 0)))
                vec = (1,0)
        elif grid[loc] == 2:
            if vec == (1,0) or vec == (-1,0):
                sources.insert(0,(loc, (0,-1)))
                vec = (0,1)
        elif grid[loc] == 3:
            if vec == (1,0):
                vec = (0,1)
            elif vec == (-1,0):
                vec = (0,-1)
            elif vec == (0,1):
                vec = (1,0)
            elif vec == (0,-1):
                vec = (-1,0)
        elif grid[loc] == 4:
            if vec == (1,0):
                vec = (0,-1)
            elif vec == (-1,0):
                vec = (0,1)
            elif vec == (0,1):
                vec = (-1,0)
            elif vec == (0,-1):
                vec = (1,0)

        if (loc, vec) in history:
            break
        else:
            history.add((loc,vec))

#print(energy.T)
print(np.sum(energy))
