import numpy as np

directions = [(0,1),(0,-1),(1,0),(-1,0)]

with open('input/20.txt') as f:
    lines = f.readlines()

grid = np.array([list(x.strip()) for x in lines])

pos = tuple(np.argwhere(grid == 'S')[0])


distances = {pos: 0}
history = set()
distance = 0
while grid[pos] != 'E':
    for  step in directions:
        next_pos = tuple(np.array(pos) + step)
        if grid[next_pos] != '#' and not next_pos in history:
            pos = next_pos
            distance += 1
            distances[pos] = distance
            history.add(pos)
            break
    
cheats = []

for pos, distance in distances.items():
    for step in directions:
        jump = tuple(np.array(pos) + 2*np.array(step))
        if jump in distances and distances[jump] > distance+2:
            cheats.append(int(distances[jump] - distance - 2))

ans =np.sum(np.array(cheats) >= 100) 
print('Answer: ', ans)
