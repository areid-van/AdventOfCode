import re

with open('input/24.txt') as f:
    lines = f.readlines()

init = []
gates = []
for line in lines:
    match = re.match('([xy][0-9][0-9]): ([01])|(...)\\s(AND|OR|XOR)\\s(...)\\s->\\s(...)', line.strip())
    if match:
        if match[1]:
            init.append((match[1], int(match[2])==1))
        else:
            gates.append((match[4],match[3],match[5],match[6]))

wires_to_gates = {}
for i in range(len(gates)):
    gate = gates[i]

    for j in [1,2]:
        inpt = gate[j]
        if not inpt in wires_to_gates:
            wires_to_gates[inpt] = []
        wires_to_gates[inpt].append(i)

wires = {}

def update(wire, value):

    wires[wire] = value

    if wire in wires_to_gates:
      for i in wires_to_gates[wire]:
          gate = gates[i]
          op = gate[0]
          input0 = gate[1]
          input1 = gate[2]
          output = gate[3]
          if input0 in wires and input1 in wires:
              if op == 'AND':
                  update(output, wires[input0] and wires[input1])
              elif op == 'OR':
                  update(output, wires[input0] or wires[input1])
              elif op == 'XOR':
                  update(output, wires[input0] != wires[input1])

for wire, value in init:
    update(wire, value)

ans = sum([2**int(wire[1:]) for wire, value in wires.items() if wire[0] == 'z' and value])
print('Answer: ', ans)
