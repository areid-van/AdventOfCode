import re
import numpy as np
import copy

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

def check_part(x,m,a,s):
    part = {'x': x, 'm': m, 'a': a, 's': s}
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
    answer = 0
    if wf == 'A':
        for x in part.values():
            answer += x
    return answer

def get_count(wf, constraints, workflows, history):
    rules = workflows[wf]
    count = 0
    cneg = copy.deepcopy(constraints)
    for rule in rules:
        cpos = copy.deepcopy(cneg)
        if rule[0]:
            q = rule[0][0]
            op = rule[0][1]
            thresh = rule[0][2]
            if op in cpos[q]:
                old = cpos[q][op]
                if op == '>':
                    cpos[q][op] = max(old, thresh)
                else:
                    cpos[q][op] = min(old, thresh)
            else:
                cpos[q][op] = thresh
            if op == '>':
                op = '<'
                thresh += 1
            else:
                op = '>'
                thresh -= 1
            if op in cneg[q]:
                old = cneg[q][op]
                if op == '>':
                    cneg[q][op] = max(old, thresh)
                else:
                    cneg[q][op] = min(old, thresh)
            else:
                cneg[q][op] = thresh

        if rule[1] == 'A':
            #print(history)
            #print(cpos)
            accum = 1
            for x in ['x', 'm', 'a', 's']:
                xmin = cpos[x].get('>',0)
                xmax = cpos[x].get('<',4001)
                accum *= xmax - xmin - 1
            #print(accum)
            count += accum
        elif rule[1] == 'R':
            continue
        else:
            history.append(rule[1])
            count += get_count(rule[1], cpos, workflows, history)
            history.pop()

    return count

wf = 'in'
constraints = {'x': dict(), 'm': dict(), 'a': dict(), 's': dict()}
history = ['in']
print(get_count(wf, constraints, workflows, history))

