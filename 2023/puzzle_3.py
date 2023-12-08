import re
import numpy as np

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

with open('input/3.txt') as f:
    lines = f.readlines()

line_size = len(lines[0].strip())
num_lines = len(lines)

numbers = list()
sym_map = list()
gears = list()
line_no = 0

for line in lines:
    end = 0
    for num in re.findall('[0-9]+', line):
        start = line.find(num,end)
        end = start + len(num)
        xmin = max(start-1, 0)
        xmax = min(end+1, line_size) 
        ymin = max(line_no - 1, 0)
        ymax = min(line_no + 2, num_lines) 
        numbers.append((int(num), xmin, xmax, ymin, ymax))

    sym_row = list()
    pos = 0
    for c in line.strip():
        sym_row.append(not c in digits)
        if c == '*':
            gears.append((pos, line_no))
        pos += 1

    sym_map.append(sym_row)

    line_no += 1

sym_map = np.stack(sym_map)

answer1 = 0
for num in numbers:
    if sym_map[num[3]:num[4],num[1]:num[2]].any(): answer1 += num[0]

print('Part 1: ', answer1)

answer2 = 0
for gear in gears:
    x = gear[0]
    y = gear[1]
    ratio = [n[0] for n in numbers if x>=n[1] and x<n[2] and y>=n[3] and y<n[4]]
    if len(ratio) == 2: answer2 += ratio[0]*ratio[1]

print('Part 2: ', answer2)
