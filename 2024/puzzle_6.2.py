import numpy as np

with open('input/6.txt') as f:
    lines = f.readlines()

grid = np.array([list(x.strip()) for x in lines])
gridx = grid.shape[1]
gridy = grid.shape[0]

directions = [(-1,0), (0,1), (1,0), (0,-1)]

ipos = np.where(grid == '^')
ipos = (ipos[0][0], ipos[1][0])


def does_loop(grid):
    pos = ipos
    direction = 0
    track = {(pos,directions[direction])}

    while True:
        step = directions[direction]
        npos = (pos[0]+step[0], pos[1]+step[1])
        if npos[0] < 0 or npos[1] < 0 or npos[0] >= gridy or npos[1] >=gridx:
            return False
        if grid[npos] == '#':
            direction = (direction + 1) % 4
        else:
            pos = npos
            k = (pos,step)
            if k in track:
                return True
            track.add(k)

ans = 0
for i in range(gridy):
    for j in range(gridx):
        if grid[i,j] == '#' or grid[i,j] == '^':
            continue
        newgrid = np.array(grid)
        newgrid[i,j] = '#'
        if does_loop(newgrid):
            ans += 1

print('Answer: ', ans)
