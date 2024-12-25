import numpy as np

with open('input/25.txt') as f:
    lines = f.read()

blocks = []
for block in lines.split('\n\n'):
    blk = []
    for line in block.strip().split('\n'):
        blk.append(list(line.strip()))
    blocks.append(np.array(blk))

keys = []
locks = []
for block in blocks:
    if np.all(block[0,:] == '#'):
        locks.append(np.sum(block=='#', axis=0)-1)
    else:
        keys.append(np.sum(block=='#', axis=0)-1)

ans = 0
for lock in locks:
    for key in keys:
        if np.all((key+lock)<=5):
            ans += 1

print('Answer: ', ans)
