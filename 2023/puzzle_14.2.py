import re
import numpy as np
import math

with open('input/14.txt') as f:
    lines = f.readlines()

buffer = list()
for line in lines:
    match = re.match('[O.#]+', line)
    if match:
        row = [0 if x =='.' else x for x in match[0]]
        row = [1 if x == 'O' else x for x in row]
        row = [2 if x == '#' else x for x in row]
        buffer.append(row)

platform = np.stack(buffer)
ny, nx = platform.shape

flats_col = list()
for i in range(nx):
    flat = np.where(platform[:,i] == 2)[0].tolist()
    flat.append(nx)
    flats_col.append(flat)

flats_row = list()
for i in range(ny):
    flat = np.where(platform[i,:] == 2)[0].tolist()
    flat.append(ny)
    flats_row.append(flat)

pos = -1
for k in range(1000000):
    for i in range(nx):
        last = 0
        for j in flats_col[i]:
            rnd = np.sum(platform[last:j,i])
            platform[last:(last+rnd),i] = 1
            platform[(last+rnd):j,i] = 0
            last = j+1

    for i in range(ny):
        last = 0
        for j in flats_row[i]:
            rnd = np.sum(platform[i,last:j])
            platform[i,last:(last+rnd)] = 1
            platform[i,(last+rnd):j] = 0
            last = j+1

    for i in range(nx):
        last = 0
        for j in flats_col[i]:
            rnd = np.sum(platform[last:j,i])
            platform[last:(j-rnd),i] = 0 
            platform[(j-rnd):j,i] = 1 
            last = j+1

    for i in range(ny):
        last = 0
        for j in flats_row[i]:
            rnd = np.sum(platform[i,last:j])
            platform[i,last:(j-rnd)] = 0
            platform[i,(j-rnd):j] = 1
            last = j+1
    
    answer = 0
    for j in range(ny):
        for i in range(nx):
            if platform[j,i] == 1:
                answer += ny-j

    if k == 300:
        a300 = answer 

    if k > 300 and answer == a300:
        pattern_len = k-300
        pos = ((1000000000 - k - 1) % pattern_len) + k

    if k == pos:
        print(answer)
        break


