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

def get_energy(grid, loc, vec):
    nx, ny = grid.shape
    energy = np.zeros(grid.shape)
    sources = [(loc, vec)]
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

    return np.sum(energy)

nx, ny = grid.shape
answer = 0
for i in range(nx):
    loc = (i, -1)
    vec = (0, 1)
    answer = max(answer, get_energy(grid, loc, vec))
    loc = (i, ny)
    vec = (0, -1)
    answer = max(answer, get_energy(grid, loc, vec))

for i in range(ny):
    loc = (-1, i)
    vec = (1, 0)
    answer = max(answer, get_energy(grid, loc, vec))
    loc = (nx, i)
    vec = (-1, 0)
    answer = max(answer, get_energy(grid, loc, vec))

print(answer)
