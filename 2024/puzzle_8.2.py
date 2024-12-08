import numpy as np

with open('input/8.txt') as f:
    lines = f.readlines()

grid = np.array([list(x.strip()) for x in lines])
gridy = grid.shape[0]
gridx = grid.shape[1]

frequencies = {str(v) for v in np.nditer(grid) if v != '.'}

nodes = np.zeros(grid.shape)
for freq in frequencies:
    index = np.where(grid == freq)
    N = index[0].size
    for j in range(N):
        for i in range(j+1,N):
            ax = index[1][i]
            ay = index[0][i]
            bx = index[1][j]
            by = index[0][j]
            m = (by - ay)/(bx - ax)
            b = ay - m*ax
            for x in range(gridx):
                yy = m*x+b
                y = round(yy)
                if abs(yy - y)<0.00001 and y >= 0 and y < gridy:
                    nodes[y,x] = 1

print('Answer: ', np.sum(nodes))
