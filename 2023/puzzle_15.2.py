import re

with open('input/15.txt') as f:
    text = f.read().strip()

def myhash(string):
    hsh = 0
    for c in string.strip():
        hsh += ord(c)
        hsh *= 17
        hsh = hsh % 256
    return hsh

boxes = {x: list() for x in range(256)}
for command in text.split(','):
    match = re.match('([a-z]+)([-=])([0-9]*)', command.strip())
    label = match[1]
    box = boxes[myhash(label)]
    op = match[2]
    if op == '=':
        focal = int(match[3])
        el = [x for x in box if x[0] == label]
        if len(el)==0:
            box.append((label, focal))
        elif len(el) == 1:
            i = box.index(el[0])
            box[i] = (label, focal)
        else:
            print('error, 2 lenses')
    if op == '-':
        el = [x for x in box if x[0] == label]
        if len(el)==1:
            box.remove(el[0])
        elif len(el)>1:
            print('error, 2 lenses s')

answer = 0
for i,box in boxes.items():
    for j in range(len(box)):
        answer += (i+1)*(j+1)*box[j][1]

print(answer)
