import re

with open('input/24.txt') as f:
    lines = f.readlines()

gates = []
for line in lines:
    match = re.match('([xy][0-9][0-9]): ([01])|(...)\\s(AND|OR|XOR)\\s(...)\\s->\\s(...)', line.strip())
    if match and not match[1]:
        gates.append([match[4],match[3],match[5],match[6]])

wires_to_gates = {}
for i in range(len(gates)):
    gate = gates[i]

    for j in [1,2]:
        inpt = gate[j]
        if not inpt in wires_to_gates:
            wires_to_gates[inpt] = []
        wires_to_gates[inpt].append(i)

outputs_to_gates = {}
for i in range(len(gates)):
    gate = gates[i]
    outputs_to_gates[gate[3]] = i

swap = []

for bit in range(1,45):
    wire = 'x' + str(bit).zfill(2)
    target = 'z' + str(bit).zfill(2)
    gs = wires_to_gates[wire]
    for g in gs:
        gate = gates[g]
        if gate[0] == 'XOR':
            out = gate[3]
            gs2 = wires_to_gates[out]
            found_xor = False
            for g2 in gs2:
                gate2 = gates[g2]
                if gate2[0] == 'XOR':
                    found_xor = True
                    out2 = gate2[3]
                    if out2 != target:
                        swap.append(target)
                        swap.append(out2)
            if not found_xor:
                swap.append(out) 
                xor_gate = gates[outputs_to_gates[target]]
                for j in [1,2]:
                    inpt = xor_gate[j]
                    gate3 = gates[outputs_to_gates[inpt]]
                    if gate3[0] != 'OR':
                        swap.append(inpt)

swap.sort()
ans = ','.join(swap)
print('Answer: ', ans)
