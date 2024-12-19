import re

with open('input/19.txt') as f:
    lines = f.readlines()

patterns = []
for line in lines:
    match = re.match('([wubrg,\\s]+)', line.strip())
    if match:
        if ',' in match[0]:
            towels = match[0].split(', ')
        else:
            patterns.append(match[0])

cache = {}

def is_possible(pattern):
    if pattern in cache:
        return cache[pattern]

    for towel in towels:
        if pattern.startswith(towel):
            if pattern == towel:
                cache[pattern] = True
                return True
            else:
                v = is_possible(pattern.replace(towel,'',1))
                if v:
                    cache[pattern] = True
                    return True
    cache[pattern] = False
    return False

possible = 0
for pattern in patterns:
    if is_possible(pattern):
        possible += 1

print('Answer: ', possible)
