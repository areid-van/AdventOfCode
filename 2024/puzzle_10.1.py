import numpy as np

with open('input/10.txt') as f:
    lines = f.readlines()

grid = np.array([[int(el) for el in list(line.strip())] for line in lines])

trailheads = np.argwhere(grid==0)

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

ans = 0
for trailhead in trailheads:
    trails = [trailhead]
    for nxt in range(1,10):
        new_trails = []
        for trail in trails:
            for d in dirs:
                newpos = trail + d
                if np.all(newpos>=0) and np.all(newpos < grid.shape) and grid[tuple(newpos)] == nxt:
                    new_trails.append(newpos)
        trails = new_trails
    ans += len(set([tuple(x) for x in trails]))

print('Answer: ', ans)
