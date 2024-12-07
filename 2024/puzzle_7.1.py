import re

equations = []
with open('input/7.txt') as f:
    for line in f.readlines():
        match = re.match('([0-9]+):(.*)', line)
        equations.append((int(match[1]), [int(x) for x in match[2].split()]))

ans = 0
for equation in equations:
    operands = equation[1]
    results = {operands.pop(0)}
    for operand2 in operands:
        new_results = set()
        for operand1 in results:
            new_results.add(operand1 * operand2)
            new_results.add(operand1 + operand2)

        results = new_results

    target = equation[0]
    if target in results:
        ans += target


print('Answer: ', ans)
