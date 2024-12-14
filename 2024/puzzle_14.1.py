import re
import numpy as np

with open('input/14.txt') as f:
    lines = f.read()

matches = re.findall('p\\=([\\-0-9]+),([\\-0-9]+) v\\=([\\-0-9]+),([\\-0-9]+)', lines)
robots = [(np.array((int(m[0]),int(m[1]))), np.array((int(m[2]),int(m[3])))) for m in matches]

q = np.zeros(4)
for robot in robots:
    p = robot[0]
    v = robot[1]
    x = np.mod(p+100*v, (101, 103))
    
    if x[0] < 50 and x[1] < 51:
        q[0] += 1
    if x[0] < 50 and x[1] > 51:
        q[1] += 1
    if x[0] > 50 and x[1] < 51:
        q[2] += 1
    if x[0] > 50 and x[1] > 51:
        q[3] += 1

ans =  np.prod(q)
print('Answer: ', ans)
