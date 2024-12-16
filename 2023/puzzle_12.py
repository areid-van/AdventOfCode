import re

with open('input/12.txt') as f:
    lines = f.readlines()

field = list()
for line in lines:
    match = re.match('([?#.]+)[ ]+([0-9,]+)', line)
    tmp = [x for x in match[1]]
    mask=0
    bits=0
    i = 0
    for bit in tmp:
        if bit != '?':
            mask += 1<<i
            if bit == '.':
                bits += 1<<i
        i += 1

    contig = [int(x) for x in match[2].split(',')]
    for i in range(len(contig)-1):
        contig[i] += 1

    field.append((len(tmp), mask, bits, contig))

def get_seq(l, contig):
    if len(contig) == 0 :
        return [[l]]
    else:
        min_len = sum(contig) 
        r = list()
        for i in range(0, l - min_len +1):
            tmp = get_seq(l-i-contig[0], contig[1::])
            for t in tmp:
                r.append([i] + t)
        return r

count = 0

for row in field:
    cc = 0
    row_len  = row[0]
    mask = row[1]
    bits = row[2]
    contig = row[3]
    tmp = get_seq(row_len, contig)
    #print(tmp)
    for t in tmp:
        i = 0
        val = 0
        for j in range(len(contig)):
            for k in range(t[j]):
                val += 1 << i
                i+=1
            l = contig[j]-1 if j < len(contig)-1 else contig[j]
            i += l
            if j < len(contig)-1:
                val += 1 << i
                i+=1
        for k in range(t[-1]):
            val += 1 << i
            i+=1

        if val & mask == bits:
            cc += 1
        #print("{:016b}".format(val)) 
        #print("{:016b}".format(mask)) 
        #print("{:016b}".format(bits)) 
    print(cc)
    count += cc

print(count)


