import re

with open('input_5.txt') as f: text = f.read()

match = re.match('seeds:([ 0-9]+)', text)
sranges = [int(x) for x in match[1].split()]
seeds = [(sranges[i], sranges[i]+sranges[i+1]) for i in range(0, len(sranges), 2)]

match = re.findall('([a-z]+)-to-([a-z]+) map:([\s0-9]+)', text)
maps = dict()
for newmap in match:
    src = newmap[0]
    dst = newmap[1]
    data = newmap[2].split()
    maps[src] = dict()
    maps[src]['destination'] = dst
    maps[src]['intervals'] = list()
    for i in range(0, len(data), 3):
        sstart = int(data[i+1])
        rng = int(data[i+2])
        dstart = int(data[i])
        maps[src]['intervals'].append({'interval': (sstart, sstart+rng),
                                    'offset': dstart-sstart})

def split_interval(src_interval, map_intervals):
    b = src_interval[0]
    e = src_interval[1]-1
    iv = [x for x in map_intervals if b>=x['interval'][0] and b<x['interval'][1]]

    if len(iv) == 1:
        offset = iv[0]['offset']
        iend = iv[0]['interval'][1]
        if e < iend:
            return [(b+offset, e+offset+1)]
        else:
            remainder = split_interval((iend, e+1), map_intervals)
            remainder.append((b+offset, iend+offset))
            return remainder
    else:
        iv = [x['interval'][0] for x in map_intervals if b<x['interval'][0]]
        if len(iv) > 0:
            istart = min(iv)
            remainder = split_interval((istart, e+1), map_intervals)
            remainder.append((b, istart))
            return remainder
        else:
            return [src_interval]

def min_location(src_intervals, src_map, maps):
    locations = list()
    for src_interval in src_intervals:
        dst_map = maps[src_map]['destination']
        dst_intervals = split_interval(src_interval, maps[src_map]['intervals'])
        if dst_map == 'location':
            locations.append(min([x[0] for x in dst_intervals]))
        else:
            locations.append(min_location(dst_intervals, dst_map, maps))
    return min(locations)

print(min_location(seeds, 'seed', maps))
