import re
import math

with open('input_6.txt') as f: text = f.read()

match = re.match('Time:([0-9\s]+)Distance:([0-9\s]+)', text)

times = [int(x) for x in match[1].split()]
distances = [int(x) for x in match[2].split()]

answer = 1
for i in range(0,len(times)):
    t = times[i]
    d = distances[i]
    sd = math.sqrt(t*t-4.*d)/2.
    h = math.ceil(t/2. + sd - 1)
    l = math.floor(t/2. - sd + 1)
    answer *= h - l + 1

print(answer)
