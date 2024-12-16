import re
import numpy as np
import math

cmap = {'.': 0,
        '#': 1,
        'S': 2}

steps = [(-1, 0),
         (1, 0),
         (0, -1),
         (0, 1)]

#with open('test/21.txt') as f:
with open('input/21.txt') as f:
    lines = f.readlines()

grid = list()
for line in lines:
    match = re.match('[.#S]+', line)
    grid.append([cmap[x] for x in match[0]])

grid = np.stack(grid).T
nx, ny = grid.shape

start = np.where(grid == 2)
start = (start[0][0], start[1][0])
grid[start] = 0

positions = set([start])
for s in range(64):
    newpositions = set()
    for pos in positions:
        for step in steps:
            newpos = (pos[0]+step[0], pos[1]+step[1])
            if newpos[0] < 0 or  newpos[0] >= nx or newpos[1] < 0 or newpos[1] >= ny:
                continue
            if grid[newpos[0], newpos[1]] == 0:
                newpositions.add(newpos)
    positions = newpositions

print(len(positions))
