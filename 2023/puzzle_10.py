import numpy as np

pipes = {'|' : [(0,1), (0,-1)],
         '-' : [(-1,0), (1,0)],
         'F' : [(0,1), (1,0)],
         'J' : [(-1,0), (0,-1)],
         '7' : [(-1,0), (0,1)],
         'L' : [(1,0), (0,-1)]}

with open('input/10.txt') as f:
    lines = f.readlines()

sketch = [[c for c in line.strip()] for line in lines]
sketch = np.transpose(np.array(sketch, dtype=str))

#find S and one connecting pipe
start = np.where(sketch == 'S')
nx,ny = sketch.shape

if start[0]>0:
    l = (start[0]-1, start[1])
    if sketch[l] in ['-', 'F', 'L']: loc = l
if start[0]<(nx-1):
    l = (start[0]+1, start[1])
    if sketch[l] in ['-', 'J', '7']: loc = l
if start[1]>0:
    l = (start[0], start[1]-1)
    if sketch[l] in ['|', 'J', 'L']: loc = l
if start[1]<(ny-1):
    l = (start[0], start[1]+1)
    if sketch[l] in ['|', 'F', '7']: loc = l

#follow pipes around loop
loop = np.zeros((nx,ny))
loop[start] = 1
previous = start
while loc != start:
    loop[loc] = 1
    for x in pipes[sketch[loc][0]]:
        nxt = (loc[0]+x[0], loc[1]+x[1])
        if nxt != previous: break
    previous = loc
    loc = nxt

answer1 = np.sum(loop)/2
print(answer1)

#check if number of vertical pipe crossings is even or odd along a ray 
vert_walls = np.logical_or(np.logical_or(sketch == '|', sketch == 'L'), sketch == 'J')
vert_walls = np.logical_and(vert_walls, loop)

answer2 = 0
for j in range(ny):
    for i in range(1,nx):
        if loop[i,j] == 0 and sum(vert_walls[0:i, j]) % 2 : answer2 += 1

print(answer2)
