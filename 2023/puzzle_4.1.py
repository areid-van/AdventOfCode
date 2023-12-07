import re

with open('input_4.txt') as f:
    lines = f.readlines()

answer = 0
for line in lines:
    match = re.match('Card[ ]*[0-9]+:([0-9 ]+)\|([0-9 ]+)',line)
    winning = [int(x) for x in match[1].strip().split()]
    mine = [int(x) for x in match[2].strip().split()]

    points = 0
    for num in mine:
        if num in winning:
            points = 2*points if points>0 else 1

    answer += points

print(answer)
