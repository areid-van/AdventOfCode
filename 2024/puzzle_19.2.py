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

def combinations(pattern):
    if pattern in cache:
        return cache[pattern]

    count = 0
    for towel in towels:
        if pattern.startswith(towel):
            if pattern == towel:
                count += 1
            else:
                count += combinations(pattern.replace(towel,'',1))

    cache[pattern] = count
    return count


ans = 0
for pattern in patterns:
    ans += combinations(pattern)

print('Answer: ', ans)
