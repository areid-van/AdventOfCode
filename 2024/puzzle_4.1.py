import numpy as np

with open('input/4.txt') as f:
    lines = f.readlines()

lines = [list(x.strip()) for x in lines]
grid = np.array(lines)

word = np.array(['X', 'M', 'A', 'S'])

def count_horiz(grid):
    c=0
    shape = grid.shape
    for j in range(shape[1]):
        for i in range(shape[0]-3):
            t = grid[i:(i+4),j]
            if np.all(t==word):
                c+=1
    return c

def count_diag(grid):
    t = np.array(['', '', '', ''])
    c=0
    shape = grid.shape
    for j in range(shape[1]-3):
        for i in range(shape[0]-3):
            for k in range(4):
                t[k] = grid[i+k,j+k]
            if np.all(t==word):
                c+=1
    return c

ans=count_horiz(grid)
ans+=count_horiz(np.transpose(grid))
ans+=count_horiz(np.flip(grid, axis=0))
ans+=count_horiz(np.flip(np.transpose(grid), axis=0))
ans+=count_diag(grid)
ans+=count_diag(np.flip(grid, axis=0))
ans+=count_diag(np.flip(grid, axis=1))
ans+=count_diag(np.flip(np.flip(grid, axis=1), axis=0))

print('Answer: ', ans)
