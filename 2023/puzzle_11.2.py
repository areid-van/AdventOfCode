import re
import numpy as np

with open('input/11.txt') as f: lines = f.readlines()
#with open('test/11.txt') as f: lines = f.readlines()

image = [[float(c=='#') for c in line.strip()] for line in lines]
image = np.transpose(np.array(image))
nx, ny = image.shape

#print(image.T)

row_map = dict()
counter = 0
for i in range(nx):
    row_map[i] = counter
    row = image[i,:]
    if not row.any():
        counter +=1000000 
    else:
        counter += 1

col_map = dict()
counter = 0
for i in range(ny):
    col_map[i] = counter
    col = image[:,i]
    if not col.any():
        counter +=1000000 
    else:
        counter += 1

galaxies = np.where(image == 1)
distance = 0
count = 0
for i in range(galaxies[0].size):
    x = row_map[galaxies[0][i]]
    y = col_map[galaxies[1][i]]
    for j in range(i+1, galaxies[0].size):
        x2 = row_map[galaxies[0][j]]
        y2 = col_map[galaxies[1][j]]
        distance += abs(x2-x) + abs(y2-y)
        count += 1

print(distance)
