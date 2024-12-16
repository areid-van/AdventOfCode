import re
import numpy as np

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

with open("input/17.txt") as f:
    lines = f.readlines()

city = list()
for line in lines:
    match = re.match('[0-9]+', line)
    if match:
        row = [int(c) for c in match[0]]
        city.append(row)

city = np.stack(city).T
nx, ny = city.shape

history = dict()
history[((1,0), right, 0)] = 4
history[((0,1), down, 0)] = 3

positions = {((1,0), right, 0): 4,
             ((0,1), down, 0): 3}

best = 0
while len(positions) > 0:
    newpositions = dict()
    for position, loss in positions.items():
        oldpos =  position[0]
        laststep = position[1]
        lastcount = position[2]
        reverse = (-laststep[0], -laststep[1])
        for step in [up, down, left, right]:
            if step != laststep and lastcount < 3:
                continue
            newcount = 0
            if step == laststep:
                if lastcount == 9:
                    continue
                else:
                    newcount = lastcount+1
            if step == reverse:
                continue

            newpos = (oldpos[0]+step[0], oldpos[1]+step[1])
            if newpos[0] < 0 or newpos[0]>=nx or newpos[1] < 0 or newpos[1] >= ny:
                 continue

            newposition = (newpos, step, newcount)
            newloss = loss + city[newpos]

            if not newposition in history or history[newposition] > newloss:
                history[newposition] = newloss
                newpositions[newposition] = newloss

    positions = newpositions

finishers = [v for k,v in history.items() if k[0] == (nx-1, ny-1)]
print(min(finishers))
