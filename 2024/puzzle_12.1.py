import numpy as np

dirs = [(-1, 0), (1, 0), (0,-1), (0,1)]

with open('input/12.txt') as f:
    lines = f.readlines()

grid = np.array([list(x.strip()) for x in lines])

plants = {str(el) for el in np.nditer(grid)}

ans = 0
for plant in plants:
    adjacent_gardens = []
    garden_region = {}
    next_region = 0
    for pos in np.argwhere(grid == plant):
        garden_region[tuple(pos)] = next_region
        next_region += 1
        for d in dirs:
            p = pos+d
            if np.all(p>=0) and np.all(p<grid.shape) and grid[tuple(p)] == plant:
                adjacent_gardens.append((tuple(pos), tuple(p)))

    change = True
    while change:
        change = False
        for adjacency in adjacent_gardens:
            if garden_region[adjacency[0]] != garden_region[adjacency[1]]:
                x = min(garden_region[adjacency[0]],garden_region[adjacency[1]])
                garden_region[adjacency[0]] = x
                garden_region[adjacency[1]] = x
                change = True

    for region in set(garden_region.values()):
        gardens = [g for g,r in garden_region.items() if r == region]
        area = len(gardens)
        perimiter = 0
        for garden in gardens:
            for d in dirs:
                p = np.array(garden)+d
                if np.any(p<0) or np.any(p>=grid.shape) or grid[tuple(p)] != plant:
                    perimiter += 1
        ans += area*perimiter

print('Answer: ', ans)
