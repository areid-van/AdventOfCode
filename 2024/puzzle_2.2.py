import re
import numpy as np


with open('input/2.txt') as f:
    lines = f.readlines()

reports = []
for line in lines:
    r = [int(x.strip()) for x in line.split(' ')]
    reports.append(np.array(r))

def is_safe(report):
    d = report[1:] - report[0:-1]
    asc = np.all(np.logical_and(d > 0, d <= 3))
    dec = np.all(np.logical_and(d < 0, d >= -3))
    return asc or dec

safe_count = 0
for report in reports:
    good = is_safe(report)

    for i in range(report.size):
        rr = np.delete(report, i)
        if is_safe(np.delete(report, i)):
            good = True
    
    if good: safe_count+=1

print(safe_count)
