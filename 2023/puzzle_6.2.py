import re
import math

with open('input/6.txt') as f: text = f.read()

match = re.match('Time:([0-9\s]+)Distance:([0-9\s]+)', text)

t = int(match[1].strip().replace(' ',''))
d = int(match[2].strip().replace(' ',''))
sd = math.sqrt(t*t-4.*d)/2
h = math.ceil(t/2. + sd - 1)
l = math.floor(t/2. - sd + 1)
print(h - l + 1)
