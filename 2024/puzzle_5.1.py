import re

with open('input/5.txt') as f:
    lines = f.readlines()

rules = list()
updates = list()

for line in lines:
    match = re.match('([0-9]+)\\|([0-9]+)', line)
    if match:
        rules.append((int(match[1]), int(match[2])))
    else:
        try:
            updates.append([int(x.strip()) for x in line.split(',')])
        except ValueError:
            pass

ans = 0
for update in updates:

    accept = True 
    for rule in rules:
        l = rule[0]
        r = rule[1]
        if l in update and r in update and (update.index(l) > update.index(r)):
            accept = False
            break

    if accept:
        ans += update[len(update)//2]

print('Answer: ', ans)
