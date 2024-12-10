with open('input/9.txt') as f:
    line = f.read()

disk_map = [int(x) for x in list(line.strip())]

memory = []
next_id = 0
is_file = True
spaces = []
files = []

for seg_len in disk_map:
    if is_file:
        files.append((len(memory), seg_len, next_id))
        b = next_id
        next_id += 1
    else:
        spaces.append((len(memory), seg_len))
        b = -1

    for i in range(seg_len):
        memory.append(b)

    is_file = not is_file

files.reverse()
for f in files:
    file_pos = f[0]
    file_len = f[1]
    file_id = f[2]

    for spos in range(len(spaces)):
        space_pos = spaces[spos][0]
        space_len = spaces[spos][1]
        if space_len >= file_len and space_pos < file_pos:

            for i in range(file_len):
                memory[space_pos+i] = file_id
                memory[file_pos+i] = -1

            spaces[spos] = (space_pos+file_len, space_len-file_len)
            break

ans = sum([x*memory[x] for x in range(len(memory)) if memory[x]>0])
print('Answer: ', ans)
