import re

names = {'one': '1',
         'two': '2',
         'three': '3',
         'four': '4',
         'five': '5',
         'six': '6',
         'seven': '7',
         'eight': '8',
         'nine': '9'}

answer = 0
for line in open('input_1.txt').readlines():
    digits = re.findall('(?=([1-9]|%s))' % '|'.join(names.keys()), line)
    digits = [names.get(x,x) for x in digits]
    answer += int(digits[0]+digits[-1])

print(answer)
