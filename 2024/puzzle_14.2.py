import re
import numpy as np
import matplotlib.pyplot as plt

with open('input/14.txt') as f:
    lines = f.read()

matches = re.findall('p\\=([\\-0-9]+),([\\-0-9]+) v\\=([\\-0-9]+),([\\-0-9]+)', lines)
robots = [(np.array((int(m[1]),int(m[0]))), np.array((int(m[3]),int(m[2])))) for m in matches]

t = 0
while t < 103*101:
    grid = np.zeros((103, 101))
    for robot in robots:
        p = robot[0]
        v = robot[1]
        x = np.mod(p + v*t, (103, 101))
        grid[tuple(x)] = 1
    
    a = np.sum(grid[0:51,:])/np.sum(grid[51:103,:])
    b = np.sum(grid[:,0:50])/np.sum(grid[:, 50:101])
    if a < 0.327 and b < 0.92:
        print(t)
        plt.pcolor(grid)
        plt.show()
    t += 1
