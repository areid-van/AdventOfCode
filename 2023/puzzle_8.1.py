import re

with open('input/8.txt') as f:
    lines = f.readlines()

dir_map = {'L': 0, 'R': 1}
match = re.match('[RL]+', lines[0])
dirs = [dir_map[x] for x in match[0]]

network = dict()
for line in lines[1::]:
    match = re.match('([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line)
    if match: network[match[1]] = (match[2], match[3])

pos = 'AAA'
steps = 0
i=0
while pos != 'ZZZ':
    steps += 1
    pos = network[pos][dirs[i]]
    i = (i + 1) % len(dirs)

print(steps)
