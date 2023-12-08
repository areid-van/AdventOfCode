import re

answer = 0
for line in open('input/1.txt').readlines():
    digits = re.findall('[0-9]', line)
    answer += int(digits[0]+digits[-1])

print(answer)
