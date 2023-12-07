import re

with open('input_4.txt') as f:
    lines = f.readlines()

cards = dict()
for line in lines:
    match = re.match('Card[ ]*([0-9]+):([0-9 ]+)\|([0-9 ]+)',line)
    card = int(match[1])
    winning = [int(x) for x in match[2].strip().split()]
    mine = [int(x) for x in match[3].strip().split()]

    wins = len([x for x in mine if x in winning])
    cards[card] = {'wins': wins, 'copies': 1}

for card_num, card in cards.items():
    for i in range(card['wins']):
        cards[card_num+1+i]['copies'] += card['copies']

answer = sum([v['copies'] for k, v in cards.items()])
print(answer)
