import re

with open('input/5.txt') as f:
    text = f.read()

match = re.match('seeds:([ 0-9]+)', text)
seeds = [int(x) for x in match[1].split()]

match = re.findall('([a-z]+)-to-([a-z]+) map:([\s0-9]+)', text)

maps = dict()
for newmap in match:
    src = newmap[0]
    dst = newmap[1]
    data = newmap[2].split()
    maps[src] = dict()
    maps[src]['destination'] = dst
    maps[src]['ranges'] = list()
    for i in range(0, len(data), 3):
        sstart = int(data[i+1])
        rng = int(data[i+2])
        dstart = int(data[i])
        maps[src]['ranges'].append({'start':sstart,
                                    'end': sstart+rng,
                                    'offset': dstart-sstart})

locations = list()
for seed in seeds:
    src = 'seed'
    num = seed
    while src != 'location':
        mp = maps[src]
        ranges = [x for x in mp['ranges'] if num >= x['start'] and num < x['end']]
        if len(ranges) : num += ranges[0]['offset']
        src = mp['destination']
    locations.append(num)

print(min(locations))

