import numpy as np

with open('input/6.txt') as f:
    lines = f.readlines()

grid = np.array([list(x.strip()) for x in lines])
gridx = grid.shape[1]
gridy = grid.shape[0]

directions = [(-1,0), (0,1), (1,0), (0,-1)]

pos = np.where(grid == '^')
pos = (pos[0][0], pos[1][0])
direction = 0
visits = {pos}


while True:
    step = directions[direction]
    npos = (pos[0]+step[0], pos[1]+step[1])
    if npos[0] < 0 or npos[1] < 0 or npos[0] >= gridy or npos[1] >=gridx:
        break
    if grid[npos] == '#':
        direction = (direction + 1) % 4
    else:
        pos = npos
        visits.add(pos)

ans = len(visits)

print('Answer: ', ans)
