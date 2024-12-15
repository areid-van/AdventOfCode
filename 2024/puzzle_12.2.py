import numpy as np

with open('input/12.txt') as f:
    lines = f.readlines()

grid = np.array([list(x.strip()) for x in lines])

plants = {str(el) for el in np.nditer(grid)}

dirs = [(-1, 0), (1, 0), (0,-1), (0,1)]
dir_side = {(-1, 0) : (0, 1),
            (1,  0) : (0, 1),
            (0, -1) : (1, 0),
            (0,  1) : (1, 0)}

ans = 0
for plant in plants:
    adjacent_gardens = []
    garden_region = {}
    next_region = 0
    for garden in np.argwhere(grid == plant):
        garden_region[tuple(garden)] = next_region
        next_region += 1
        for d in dirs:
            p = garden + d
            if np.all(p>=0) and np.all(p<grid.shape) and grid[tuple(p)] == plant:
                adjacent_gardens.append((tuple(garden), tuple(p)))

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

        sides = 0
        for d in dirs:
            garden_side = {}
            next_side = 0
            for garden in gardens:
                p = np.array(garden)+d
                if np.any(p<0) or np.any(p>=grid.shape) or grid[tuple(p)] != plant:
                    garden_side[garden] = next_side
                    next_side += 1

            change = True
            while change:
                change = False
                for garden in gardens:
                    p = tuple(np.array(garden)+dir_side[d])
                    if garden in garden_side and p in garden_side and garden_side[garden] != garden_side[p]:
                        x = min(garden_side[garden], garden_side[p])
                        garden_side[garden] = x
                        garden_side[p] = x
                        change = True
            sides += len(set(garden_side.values()))
        ans += area*sides


print('Answer: ', ans)
