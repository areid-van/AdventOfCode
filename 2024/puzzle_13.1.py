import re
import numpy as np
from scipy import linalg

with open('input/13.txt') as f:
    lines = f.read()

matches = re.findall("Button A: X\\+([0-9]+), Y\\+([0-9]+)\\s*"
                        +"Button B: X\\+([0-9]+), Y\\+([0-9]+)\\s*"
                        +"Prize: X=([0-9]+), Y=([0-9]+)", lines)

ans = 0
for match in matches:
    A = np.array([[int(match[0]),int(match[2])], [int(match[1]),int(match[3])]])
    b = np.array([int(match[4]),int(match[5])])
    x = linalg.solve(A, b)

    if np.all(np.abs(np.round(x)-x)<0.0001):
        ans += 3*x[0] + x[1]

print('Answer: ', ans)
