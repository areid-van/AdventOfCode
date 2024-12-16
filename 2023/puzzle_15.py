import re

with open('input/15.txt') as f:
    text = f.read().strip()


answer = 0
for command in text.split(','):
    hsh = 0
    for c in command.strip():
        hsh += ord(c)
        hsh *= 17
        hsh = hsh % 256
    answer += hsh

print(answer)
