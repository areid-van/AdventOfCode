import re
import numpy as np


with open('input/1.txt') as f:
    lines = f.readlines()

left_list = []
right_list = []
for line in lines:
    match = re.match('([0-9]+)[ ]+([0-9]+)', line)
    if match:
        left_list.append(int(match[1]))
        right_list.append(int(match[2]))

left_list.sort()
right_list.sort()
distance = np.sum(np.abs(np.array(left_list) - np.array(right_list)))
print(distance)

