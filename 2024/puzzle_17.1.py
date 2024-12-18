import re
import numpy as np

instructions = {0: 'adv',
                1: 'bxl',
                2: 'bst',
                3: 'jnz',
                4: 'bxc',
                5: 'out',
                6: 'bdv',
                7: 'cdv'}

combo_operands = ['adv', 'bst', 'out', 'bdv', 'cdv']

with open('input/17.txt') as f:
    lines = f.readlines()

registers = {}
for line in lines:
    match = re.match('Register (.):\\s+([0-9]+)|Program:\\s+([0-9,]+)', line.strip())
    if match:
        if match[1]:
            registers[match[1]] = int(match[2])
        else:
            program = [int(x) for x in match[3].split(',')]

def compute(A,B,C,program):
    ip = 0
    stdout = []
    while ip < len(program):
        inst = instructions[program[ip]]
        operand = program[ip+1]
        ip += 2
        if inst in combo_operands and operand > 3:
            if operand == 4:
                operand = A
            elif operand == 5:
                operand = B
            elif operand == 6:
                operand = C
            else:
                raise Exception('bad operand')

        if inst == 'adv':
            A = int(A/(2**operand))
        elif inst == 'bxl':
            B = B ^ operand
        elif inst == 'bst':
            B = operand % 8
        elif inst == 'jnz':
            if A != 0:
                ip = operand
        elif inst == 'bxc':
            B = B ^ C
        elif inst == 'out':
            stdout.append(operand % 8)
        elif inst == 'bdv':
            B = int(A/(2**operand))
        elif inst == 'cdv':
            C = int(A/(2**operand))
        else:
            raise Exception('bad instruction')

    return np.array(stdout)

A = registers['A']
B = registers['B']
C = registers['C']

out = compute(A, B, C, program)
print('Answer: ',','.join([str(x) for x in out]))
