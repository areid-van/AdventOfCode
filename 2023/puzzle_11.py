import re
import numpy as np

with open('input/11.txt') as f: lines = f.readlines()
#with open('test/11.txt') as f: lines = f.readlines()

image = [[float(c=='#') for c in line.strip()] for line in lines]
image = np.transpose(np.array(image))
nx, ny = image.shape

#print(image.T)

expanded = list()
for i in range(nx):
    row = image[i,:]
    expanded.append(row)
    if not row.any():
        expanded.append(np.zeros((ny)))

image = np.stack(expanded)
nx, ny = image.shape

expanded = list()
for i in range(ny):
    col = image[:,i]
    expanded.append(col)
    if not col.any():
        expanded.append(np.zeros((nx)))

image = np.stack(expanded)
#print(image)

galaxies = np.where(image == 1)
distance = 0
count = 0
for i in range(galaxies[0].size):
    x = galaxies[0][i]
    y = galaxies[1][i]
    for j in range(i+1, galaxies[0].size):
        x2 = galaxies[0][j]
        y2 = galaxies[1][j]
        distance += abs(x2-x) + abs(y2-y)
        count += 1

print(distance)
