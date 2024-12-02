import re
import numpy as np


with open('input/1.txt') as f:
#with open('test/1.txt') as f:
    lines = f.readlines()

left_list = []
right_list = []
for line in lines:
    match = re.match('([0-9]+)[ ]+([0-9]+)', line)
    if match:
        left_list.append(int(match[1]))
        right_list.append(int(match[2]))

right_list = np.array(right_list)

similarity = 0
for x in left_list:
    similarity += x * np.sum(right_list == x)

print(similarity)

