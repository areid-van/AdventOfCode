import re
import numpy as np

dmap = {'<' : (0,-1),
        '>' : (0,1),
        '^' : (-1,0),
        'v' : (1,0)}

def can_move(grid, pos, d):
    newpos = pos + d
    if grid[tuple(newpos)] == '#':
        return False
    elif grid[tuple(newpos)] == '.':
        return True
    else:
        if d == dmap['^'] or d == dmap['v']:
            sibling = (0,1) if grid[tuple(newpos)] == '[' else (0,-1)
            return can_move(grid, newpos, d) and can_move(grid, newpos+sibling, d)
        else:
            return can_move(grid, newpos, d)

def do_move(grid, pos, d):
    newpos = pos + d
    if grid[tuple(newpos)] != '.':
        if d == dmap['^'] or d == dmap['v']:
            sibling = (0,1) if grid[tuple(newpos)] == '[' else (0,-1)
            do_move(grid, newpos+sibling, d)
        do_move(grid, newpos, d)
    grid[tuple(newpos)] = grid[tuple(pos)]
    grid[tuple(pos)] = '.'

with open('input/15.txt') as f:
    lines = f.readlines()

grid = list()
directions = list()
for line in lines:
    match = re.match('([#.O@]+)|([<>^v]+)', line.strip())
    if match:
        if match[1]:
            newmatch = match[1].replace('O','[]').replace('#','##').replace('.','..').replace('@','@.')
            grid.append(list(newmatch))
        else:
            directions += list(match[2])

grid = np.array(grid)
pos = np.argwhere(grid == '@')[0]

for step in directions:
    d = dmap[step]

    if can_move(grid, pos, d):
        do_move(grid, pos, d)
        pos += d


ans = 0
for box in np.argwhere(grid=='['):
    ans += 100*box[0] + box[1]

print('Answer: ', ans)
