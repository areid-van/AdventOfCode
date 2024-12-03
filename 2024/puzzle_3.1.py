import re

with open('input/3.txt') as f:
    memory = f.read()

instructions = re.findall('mul\\(([0-9]+),([0-9]+)\\)', memory)
ans = sum([int(x[0])*int(x[1]) for x in instructions])

print('Answer: ', ans)
