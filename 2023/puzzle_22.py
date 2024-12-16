import re
import numpy as np

#with open('test/22.txt') as f:
with open('input/22.txt') as f:
    lines = f.readlines()

inp = list()
for line in lines:
    m = re.match('([0-9,]+)~([0-9,]+)', line)
    a1 = [int(x) for x in m[1].split(',')]
    a2 = [int(x)+1 for x in m[2].split(',')]
    inp.append((a1, a2))

xmin = min([x[0][0] for x in inp])
xmax = max([x[1][0] for x in inp])
ymin = min([x[0][1] for x in inp])
ymax = max([x[1][1] for x in inp])
zmin = min([x[0][2] for x in inp])
zmax = max([x[1][2] for x in inp])

bricks = {(i+2) : inp[i] for i in range(len(inp))}

idx = np.zeros((xmax, ymax, zmax))
idx[xmin:xmax, ymin:ymax, 0] = 1

#print(xmin)
#print(xmax)
#print(ymin)
#print(ymax)
#print(zmin)
#print(zmax)

for bid, b in bricks.items():
    idx[ b[0][0]:b[1][0],b[0][1]:b[1][1],b[0][2]:b[1][2] ] = bid

brickFell = True
while brickFell:
    brickFell = False
    for bid, b in bricks.items():
        if np.all(idx[ b[0][0]:b[1][0],b[0][1]:b[1][1],b[0][2]-1 ] == 0):
            idx[ b[0][0]:b[1][0],b[0][1]:b[1][1],b[0][2]:b[1][2] ] = 0
            b[0][2] -= 1
            b[1][2] -= 1
            idx[ b[0][0]:b[1][0],b[0][1]:b[1][1],b[0][2]:b[1][2] ] = bid
            brickFell = True

#print(np.flip(idx[:,0,].T))
#print(np.flip(idx[:,1,].T))

supports = dict()
supported_by = dict()
for k in range(1,zmax):
    for j in range(ymax):
        for i in range(xmax):
            l = idx[i,j,k-1]
            h = idx[i,j,k]
            if l != 0 and h != 0 and l != h:
                if not l in supports:
                    supports[l] = set()
                supports[l].add(h)
                if not h in supported_by:
                    supported_by[h] = set()
                supported_by[h].add(l)

#print(supports)
#print(supported_by)

answer = 0
for bid in bricks.keys():
    if not bid in supports:
        answer += 1
    else:
        canRemove = True
        for oid in supports[bid]:
            canRemove = canRemove and len(supported_by[oid]) > 1
        if canRemove:
            answer += 1

print(answer)


answer2 = 0
Nfall = dict()
for bid in bricks.keys():
    moves = set()
    mightmove = set()
    newmoves = set([bid])
    while len(newmoves) > 0:
        for nid in newmoves:
            mightmove = mightmove | supports.get(nid, set())
        moves = moves | newmoves
        mightmove = mightmove - moves
        newmoves = set()

        for mid in mightmove:
            if supported_by[mid] <= moves:
                newmoves.add(mid)

        mightmove = mightmove - newmoves

        #print(newmoves)
    #print(bid, len(moves)-1)
    answer2 += len(moves)-1

print(answer2)

