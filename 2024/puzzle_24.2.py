import re

gates = []
with open('input/24.txt') as f:
    for line in f.readlines():
        match = re.match('(...)\\s(AND|OR|XOR)\\s(...)\\s->\\s(...)', line.strip())
        if match:
            gates.append({'op': match[2],'inputs': (match[1],match[3]), 'output': match[4]})

swap = []
for bit in range(1,45):
    x_bit_wire = 'x' + str(bit).zfill(2)
    z_bit_wire = 'z' + str(bit).zfill(2)

    for gate in (x for x in gates if x_bit_wire in x['inputs']):
        if gate['op'] == 'XOR':
            bit_sum_wire = gate['output']
            found_xor = False
            for gate2 in (x for x in gates if bit_sum_wire in x['inputs']):
                if gate2['op'] == 'XOR':
                    found_xor = True
                    sum_wire = gate2['output']
                    if sum_wire != z_bit_wire:
                        swap.append(z_bit_wire)
                        swap.append(sum_wire)

            if not found_xor:
                swap.append(bit_sum_wire) 
                xor_gate = [x for x in  gates if x['output'] == z_bit_wire][0]
                for xor_input in xor_gate['inputs']:
                    gate2 = [x for x in gates if x['output'] == xor_input][0]
                    if gate2['op'] != 'OR':
                        swap.append(xor_input)

swap.sort()
print('Answer: ', ','.join(swap))
