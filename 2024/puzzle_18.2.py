import re
import numpy as np

directions = [(0,1),(0,-1),(1,0),(-1,0)]

with open('input/18.txt') as f:
    lines = f.readlines()

coords = list()
for line in lines:
    match = re.match('([0-9]+),([0-9]+)', line.strip())
    if match:
        coords.append((int(match[2]),int(match[1])))


grid = np.zeros((71,71))
grid[70,70] = 2
for i in range(1024):
    grid[coords[i]] = 1

for N in range(1024,len(coords)):

    print(N,len(coords))
    grid[coords[N]] = 1

    pos = (0,0)
    paths = [(0,{pos},pos)]
    best = 9999999999999999
    lowest_score = {pos: 0}

    while len(paths) > 0:
        new_paths = list()
        for path in paths:

            score = path[0]
            history = path[1]
            pos = path[2]

            for step in directions:
                new_score = score+1 
                npa = np.array(pos) + step
                new_pos = tuple(npa)

                if new_score >= best or np.any(npa < 0) or np.any(npa >= grid.shape):
                    continue

                if new_pos in lowest_score and lowest_score[new_pos] <= new_score:
                    continue

                if not (new_pos in history) and (grid[new_pos] != 1):
                    if grid[new_pos] == 2:
                        best = min(best, new_score)
                    else:
                        new_history = history.copy()
                        new_history.add(new_pos)
                        new_paths.append((new_score, new_history, new_pos))
                        lowest_score[new_pos] = new_score
        paths = new_paths

    if best == 9999999999999999:
        ans = coords[N]
        break

print('Answer: ', '%d,%d'%(ans[1], ans[0]))
