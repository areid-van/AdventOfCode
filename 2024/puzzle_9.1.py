with open('input/9.txt') as f:
    line = f.read()

disk_map = [int(x) for x in list(line.strip())]

memory = []
nextid = 0
dofile = True
spaces = []
for el in disk_map:
    if dofile:
        for i in range(el):
            memory.append(nextid)
        nextid += 1
    else:
        for i in range(el):
            spaces.append(len(memory))
            memory.append(-1)
    dofile = not dofile

for space in spaces:
    while memory[-1] == -1:
        memory.pop()
    if space < len(memory):
        memory[space] = memory.pop()

ans = sum([x*memory[x] for x in range(len(memory)) if memory[x] > 0])

print('Answer: ', ans)
