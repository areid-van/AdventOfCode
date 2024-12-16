import re
import numpy as np

with open('input/19.txt') as f:
#with open('test/19.txt') as f:
    lines = f.readlines()

workflows = dict()
for i in range(len(lines)):
    if len(lines[i].strip()) < 1:
        break
    match = re.match('([a-z]+)\{(.*)\}', lines[i])
    if match:
        name = match[1]
        rules = list()
        for rule in match[2].split(','):
            m2 = re.match('(([xmas])([<>])([0-9]+):)?([a-zAR]+)',rule)
            if m2[2]:
                q = m2[2]
                op = m2[3]
                val = int(m2[4])
                cond = (q, op, val)
            else:
                cond = None

            target = m2[5]
            rules.append((cond, target))
        workflows[name] = rules

objs = list()
for i in range(i+1, len(lines)):
    line = lines[i][1:-2]
    segs = line.split(',')
    t = dict()
    for seg in segs:
        t[seg[0]] = int(seg[2::])
    objs.append(t)

answer = 0
for part in objs:
    wf = 'in'
    while wf != 'A' and wf != 'R':
        for rule in workflows[wf]:
            if rule[0]:
                val = part[rule[0][0]]
                op = rule[0][1]
                thresh = rule[0][2]
                if op == '<':
                    if val < thresh:
                        wf = rule[1]
                        break
                else:
                    if val > thresh:
                        wf = rule[1]
                        break
            else:
                wf = rule[1]
                break
    if wf == 'A':
        for x in part.values():
            answer += x

print(answer)
