import re
import numpy as np

dmap = {'<' : (0,-1),
        '>' : (0,1),
        '^' : (-1,0),
        'v' : (1,0)}

with open('input/15.txt') as f:
    lines = f.readlines()

grid = list()
directions = list()
for line in lines:
    match = re.match('([#.O@]+)|([<>^v]+)', line.strip())
    if match:
        if match[1]:
            grid.append(list(match[1]))
        else:
            directions += list(match[2])

grid = np.array(grid)
pos = np.argwhere(grid == '@')[0]

for step in directions:
    d = dmap[step]
    newpos = pos + d
    if grid[tuple(newpos)] == '#':
        continue
    if grid[tuple(newpos)] == '.':
        grid[tuple(pos)] = '.'
        pos = newpos
        grid[tuple(pos)] = '@'
        continue
    
    spacepos = newpos
    while True:
        spacepos = spacepos + d
        if grid[tuple(spacepos)] == '#':
            break
        elif grid[tuple(spacepos)] == '.':
            grid[tuple(spacepos)] = 'O'
            grid[tuple(pos)] = '.'
            pos = newpos
            grid[tuple(pos)] = '@'
            break

ans = 0
for box in np.argwhere(grid=='O'):
    ans += 100*box[0] + box[1]

print('Answer: ', ans)
