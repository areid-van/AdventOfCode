import numpy as np

direction_vectors = {'N': (-1,0),
                     'S': (1,0),
                     'E': (0,1),
                     'W': (0,-1)}

allowed_directions = {'N': ('N', 'E', 'W'),
                      'S': ('S', 'E', 'W'),
                      'E': ('E', 'N', 'S'),
                      'W': ('W', 'N', 'S')}

with open('input/16.txt') as f:
    lines = f.readlines()

grid = np.array([list(x.strip()) for x in lines])

start_pos = tuple(np.argwhere(grid=='S')[0])
end_pos = tuple(np.argwhere(grid=='E')[0])

paths = [(0,{start_pos},start_pos,'E')]
best = 109496 #output from part 1 
lowest_score = {(start_pos,'E'): 0}
best_tiles = {start_pos, end_pos}


while len(paths) > 0:
    new_paths = list()
    for path in paths:

        score = path[0]
        history = path[1]
        pos = path[2]
        d = path[3]

        for new_d in allowed_directions[d]:
            new_score = score+1 if new_d == d else score + 1001
            new_pos = tuple(np.array(pos) + direction_vectors[new_d])

            k = (new_pos, new_d)
            if k in lowest_score and lowest_score[k] < new_score:
                continue

            if not (new_pos in history) and (grid[new_pos] != '#'):
                if grid[new_pos] == 'E':
                    if new_score == best:
                        best_tiles = best_tiles.union(history)
                else:
                    new_history = history.copy()
                    new_history.add(new_pos)
                    new_paths.append((new_score, new_history, new_pos, new_d))
                    lowest_score[k] = new_score
    paths = new_paths

print('Answer: ', len(best_tiles))
