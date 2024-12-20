import numpy as np

directions = [(0,1),(0,-1),(1,0),(-1,0)]

with open('input/20.txt') as f:
    lines = f.readlines()

grid = np.array([list(x.strip()) for x in lines])

pos = tuple(np.argwhere(grid == 'S')[0])

distances = [(pos, 0)]
history = set()
distance = 0
while grid[pos] != 'E':
    for  step in directions:
        next_pos = tuple(np.array(pos) + step)
        if grid[next_pos] != '#' and not next_pos in history:
            pos = next_pos
            distance += 1
            distances.append((pos, distance))
            history.add(pos)
            break
    
cheats = []

for i in range(len(distances)):
    pos = distances[i][0]
    distance = distances[i][1]
    for j in range(i+100,len(distances)):
        jump_pos = distances[j][0]
        jump_distance = distances[j][1]
        jump_time = abs(jump_pos[0]-pos[0]) + abs(jump_pos[1]-pos[1])
        if jump_time <= 20:
            saving = int(jump_distance - distance - jump_time)
            if saving > 0:
                cheats.append(saving)

ans = np.sum(np.array(cheats) >= 100)
print('Answer: ', ans)
