import re
import numpy as np

with open('input/18.txt') as f:
    lines = f.readlines()

coords = list()
for line in lines:
    match = re.match('([0-9]+),([0-9]+)', line.strip())
    if match:
        coords.append((int(match[2]),int(match[1])))


grid = np.zeros((71,71))
for i in range(1024):
    grid[coords[i]] = 1
grid[70,70] = 2

pos = (0,0)
paths = [(0,{pos},pos)]
best = 9999999999999999
lowest_steps = {pos: 0}

directions = [(0,1),(0,-1),(1,0),(-1,0)]

while len(paths) > 0:
    new_paths = list()
    for path in paths:

        steps = path[0]
        history = path[1]
        pos = path[2]

        for step in directions:
            new_steps = steps+1 
            new_pos_array = np.array(pos) + step
            new_pos = tuple(new_pos_array)

            if new_steps >= best or np.any(new_pos_array < 0) or np.any(new_pos_array >= grid.shape):
                continue

            if new_pos in lowest_steps and lowest_steps[new_pos] <= new_steps:
                continue

            if not (new_pos in history) and (grid[new_pos] != 1):
                if grid[new_pos] == 2:
                    best = min(best, new_steps)
                else:
                    new_history = history.copy()
                    new_history.add(new_pos)
                    new_paths.append((new_steps, new_history, new_pos))
                    lowest_steps[new_pos] = new_steps
    paths = new_paths

print('Answer: ', best)
