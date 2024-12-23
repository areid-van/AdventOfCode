with open('input/22.txt') as f:
    secrets = [int(line.strip()) for line in f.readlines()]

def next_number(x):
    y = (x^(x*64)) % 16777216
    y = (y^(y//32)) % 16777216
    y = (y^(y*2048)) % 16777216
    return y

ans = 0
total_prices = {}
for secret in secrets:
    changes = []
    prices = []
    for i in range(2000):
        new_secret = next_number(secret)
        changes.append((new_secret%10) - (secret%10))
        prices.append(new_secret%10)
        secret = new_secret

    sequence_history = set() 
    for i in range(3, len(changes)):
        k = tuple(changes[(i-3):(i+1)])
        if not (k in sequence_history):
            sequence_history.add(k)
            total_prices[k] = total_prices.get(k,0) + prices[i]

print('Answer: ', max(total_prices.values()))
