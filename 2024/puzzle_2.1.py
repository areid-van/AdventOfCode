import re
import numpy as np


with open('input/2.txt') as f:
    lines = f.readlines()

reports = []
for line in lines:
    r = [int(x) for x in line.split(' ')]
    reports.append(np.array(r))

safe_count = 0
for report in reports:
    d = report[1:] - report[0:-1]
    asc = np.all(np.logical_and(d > 0, d <= 3))
    dec = np.all(np.logical_and(d < 0, d >= -3))
    if asc or dec : safe_count += 1

print(safe_count)
