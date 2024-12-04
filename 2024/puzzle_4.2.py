import numpy as np

with open('input/4.txt') as f:
    lines = f.readlines()

lines = [list(x.strip()) for x in lines]
grid = np.array(lines)

ans = 0

word = np.array(['M', 'A', 'S'])
word2 = np.array(['S', 'A', 'M'])

ans = 0

t = np.array(['', '', ''])
t2 = np.array(['', '', ''])
shape = grid.shape
for j in range(shape[1]-2):
    for i in range(shape[0]-2):
        for k in range(3):
            t[k] = grid[i+k,j+k]
            t2[k] = grid[i+2-k,j+k]
        if np.all(t==word) and np.all(t2==word): ans+=1
        if np.all(t==word2) and np.all(t2==word): ans+=1
        if np.all(t==word) and np.all(t2==word2): ans+=1
        if np.all(t==word2) and np.all(t2==word2): ans+=1

print('Answer: ', ans)
