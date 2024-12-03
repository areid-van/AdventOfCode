import re

with open('input/3.txt') as f:
    memory = f.read()

instructions = re.findall("mul\\(([0-9]+),([0-9]+)\\)|(do\\(\\))|(don't\\(\\))", memory)

ans = 0
enabled = True
for instruction in instructions:
        if instruction[2] == 'do()':
            enabled = True
        elif instruction[3] == "don't()":
            enabled = False
        else:
            if enabled:
                ans += int(instruction[0])*int(instruction[1])

print('Answer: ', ans)
