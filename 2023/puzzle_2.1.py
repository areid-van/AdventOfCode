import re
import numpy as np

cmap = {'red': 0,
        'green': 1,
        'blue': 2}

cubes = np.array([12,13,14])

lines = open('input_2.txt').readlines()

answer = 0

for line in lines:
    match = re.match('Game ([0-9]+):(.*)', line)
    game = int(match[1])
    trials = list() 
    for trial in match[2].split(';'):
        rgb = np.zeros(3)
        for color in trial.split(','):
            cpair = color.split()
            rgb[cmap[cpair[1]]] = int(cpair[0])
        trials.append(rgb)
    trials_table = np.stack(trials)
    shown = trials_table.max(axis=0)
    if (shown<=cubes).all(): answer += game

print(answer)
