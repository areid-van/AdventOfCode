import re
import math

with open('input/8.txt') as f:
    lines = f.readlines()

dir_map = {'L': 0, 'R': 1}
match = re.match('[RL]+', lines[0])
dirs = [dir_map[x] for x in match[0]]

network = dict()
for line in lines[1::]:
    match = re.match('([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)', line)
    if match: network[match[1]] = (match[2], match[3])

starting_points = [x for x in network.keys() if x[2] == 'A']

first_z = list()
for pos in starting_points:
    steps = 0
    i=0
    while pos[2] != 'Z':
        steps += 1
        pos = network[pos][dirs[i]]
        i = (i + 1) % len(dirs)
    first_z.append(steps)

answer = 1
for x in first_z: answer = math.lcm(answer, x)
print(answer)
