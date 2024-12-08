import numpy as np

with open('input/8.txt') as f:
    lines = f.readlines()

grid = np.array([list(x.strip()) for x in lines])

grid = np.array(grid)
gridy = grid.shape[0]
gridx = grid.shape[1]

frequencies = {str(v) for v in np.nditer(grid) if v != '.'}

nodes = np.zeros(grid.shape)

for freq in frequencies:
    index = np.where(grid == freq)
    N = index[0].size
    for j in range(N):
        for i in range(j+1,N):

            a = np.array([v[i] for v in index])
            b = np.array([v[j] for v in index])

            for an in [2*a - b, 2*b - a]:
                if np.all(an>=0) and np.all(an < grid.shape):
                    nodes[tuple(an)] = 1

print('Answer: ', np.sum(nodes))
