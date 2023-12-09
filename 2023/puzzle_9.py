import re
import numpy as np

with open('input/9.txt') as f:
    lines = f.readlines()

histories = list()
for line in lines:
    histories.append([int(x) for x in re.findall('[\-0-9]+', line)])

answer1 = 0
answer2 = 0

for seq in histories:
    seqs = list()
    while np.any(seq):
        seqs.append(seq)
        seq = [ seq[i]-seq[i-1] for i in range(1,len(seq)) ]

    last = 0
    first = 0
    for seq in reversed(seqs): 
        last += seq[-1]
        first = seq[0] - first

    answer1 += last
    answer2 += first

print(answer1)
print(answer2)
