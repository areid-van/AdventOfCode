with open('input/22.txt') as f:
    secrets = [int(line.strip()) for line in f.readlines()]

def next_number(x):
    y = (x^(x*64)) % 16777216
    y = (y^(y//32)) % 16777216
    y = (y^(y*2048)) % 16777216
    return y

ans = 0
for secret in secrets:
    for i in range(2000):
        secret = next_number(secret)
    ans += secret

print('Answer: ', ans)
