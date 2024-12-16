import re
from concurrent.futures import ProcessPoolExecutor

def solve(vertices, ii, ymin, ymax, s):
    volume = 0
    k = 0;
    N = ymax+1-ymin
    for y in range(ymin+ii, ymax+1, s):
        #print("y", y)
        intercepts = list()
        for i in range(1,len(vertices)):
            v1 = vertices[i-1]
            v2 = vertices[i]
            v3 = vertices[(i+1) % len(vertices)]
            if y > min(v1[1], v2[1]) and y < max(v1[1], v2[1]):
                intercepts.append((v1[0],0))
            if v2[1] == y:
                if max(v1[1], v3[1]) > y:
                    intercepts.append((v2[0],1))
                else:
                    intercepts.append((v2[0],-1))

        intercepts.sort(key = lambda x:x[0])

        inside = False
        inedge = False
        last = None
        vol = 0 
        for i in range(len(intercepts)):
            nxt = intercepts[i]
            if inside and not inedge:
                vol += nxt[0] - last[0] - 1
            if nxt[1] == 0:
                vol += 1
                inedge = False
                inside = not inside
            if nxt[1] != 0:
                if inedge:
                    if nxt[1] != last[1]:
                        inside = not inside
                    inedge = False
                    vol += nxt[0] - last[0] + 1
                else:
                    inedge = True
            #print(nxt, inside, inedge, vol)
            last = nxt
        volume += vol
        k += 1
        if ii ==0 and k % 10000 == 0:
            print(k/N*1000)

    return volume
    #print(vol)
    #print(vol, compare[k])
    #if vol != compare[k]:
    #    print(intercepts)
    #    break
         
if __name__ == "__main__":


    steps = {'U': (0, -1),
             'D': (0, 1),
             'L': (-1, 0),
             'R': (1, 0)}

    trans = {'0': 'R',
             '1': 'D',
             '2': 'L',
             '3': 'U'}

    #with open('test/18.txt') as f:
    with open('input/18.txt') as f:
        lines = f.readlines()

    commands = list()
    for line in lines:
        match = re.match('([UDLR]) ([0-9]+) \(#([0-9a-f]{6})\)', line)
        if match:
            commands.append((match[1], int(match[2]), match[3]))

    last = (0,0)
    vertices = [last]

    for command in commands:
        a = trans[command[2][5]]
        step = steps[a]
        d = int(command[2][0:5], 16)
        print(a, d)
        nxt = (last[0]+d*step[0], last[1]+d*step[1])
        vertices.append(nxt)
        last = nxt


    xmin = min([x[0] for x in vertices])
    xmax = max([x[0] for x in vertices]) 
    ymin = min([x[1] for x in vertices])
    ymax = max([x[1] for x in vertices])

    volume = 0
    with ProcessPoolExecutor(max_workers=10) as executor:
        results = list()
        for i in range(10):
            results.append(executor.submit(solve, vertices, i, ymin, ymax, 10))

        for result in results:
            x = result.result()
            volume += x

    print(volume)
