import re
import numpy as np

with open('input/13.txt') as f:
    lines = f.readlines()

patterns = list()
buffer = list()
for line in lines:
    match = re.match('[#.]+', line)
    if match:
        buffer.append([float(x == '.') for x in match[0]])
    else:
        patterns.append(np.stack(buffer))
        buffer = list()

count = 0
for pattern in patterns:
    ny, nx = pattern.shape
    for i in range(1, nx):
        ll = 0
        lh = i
        rl = i
        rh = nx
        if lh - ll > rh - rl:
            ll = lh - rh + rl
        if rh - rl > lh - ll:
            rh = rl + lh - ll

        if np.all(pattern[:,ll:lh] == np.flip(pattern[:,rl:rh],axis=1)):
            count += i
    for i in range(1, ny):
        ll = 0
        lh = i
        rl = i
        rh = ny
        if lh - ll > rh - rl:
            ll = lh - rh + rl
        if rh - rl > lh - ll:
            rh = rl + lh - ll

        if np.all(pattern[ll:lh,:] == np.flip(pattern[rl:rh,:],axis=0)):
            count += 100*i

print(count)
