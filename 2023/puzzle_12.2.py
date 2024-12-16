import re
from concurrent.futures import ProcessPoolExecutor

def get_seq(l, mask, bits, contig, cpos, val, pos, depth):
    #pmask = 0
    #for i in range(pos):
    #    pmask += 1<<i

    #if val & mask & pmask != bits & pmask:
    #    return 0

    if cpos == len(contig):
        for k in range(l):
            val += 1 << pos
            pos+=1

        if val & mask == bits:
            return 1
        else:
            return 0
    else:
        min_len = sum(contig[cpos::]) 
        bl = contig[cpos]
        pmask = 0
        for j in range(bl):
            pmask += 1 << j
        pmask = pmask << pos
        block = 1 << (bl-1) if cpos < len(contig)-1 else 0
        block = block << pos
        
        count = 0
        for i in range(0, l - min_len +1):
            newval = val | block
            if block & mask == bits & pmask:
                count += get_seq(l-bl, mask, bits, contig, cpos+1, val|block, pos + bl, depth+1)
            block = (block << 1) + (1 << pos) 
            pmask = (pmask << 1) + (1 << pos)
            bl += 1
            #if depth < 3: print(depth, i, l-min_len+1)
        return count

def solve(i, row):
    row_len  = row[0]
    mask = row[1]
    bits = row[2]
    contig = row[3]
    cc = get_seq(row_len, mask, bits, contig, 0, 0, 0,0)
    with open('results/%d.txt' % i, "w") as f:
        f.write("%d" % cc)
    return cc

if __name__ == "__main__":
    with open('input/12.txt') as f:
    #with open('input/12.txt') as f:
        lines = f.readlines()
    
    field = list()
    for line in lines:
        match = re.match('([?#.]+)[ ]+([0-9,]+)', line)
        tmp = [x for x in match[1]]
        mask=0
        bits=0
        i = 0
        for j in range(1):
            for bit in tmp:
                if bit != '?':
                    mask += 1<<i
                    if bit == '.':
                        bits += 1<<i
                i += 1
            #if j < 4:
            #    i += 1
    
        contig = list()
        for j in range(1):
            contig += [int(x) for x in match[2].split(',')]
        for i in range(len(contig)-1):
            contig[i] += 1
    
        #field.append((5*len(tmp)+4, mask, bits, contig))
        field.append((len(tmp), mask, bits, contig))
    
    
    count = 0
    with ProcessPoolExecutor(max_workers=20) as executor:
        i=0
        results = list()
        for row in field:
            i += 1
            results.append(executor.submit(solve, i, row))
    
        for result in results:
            x = result.result()
            print(x)
            count += x
    
    print(count)
    
    
