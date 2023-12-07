import re

cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
card_order = {cards[i]:i+1 for i in range(len(cards))}

with open('input_7.txt') as f: lines = f.readlines()

hands = list()
for line in lines:
    match = re.match('([%s]+) ([0-9]+)' % ''.join(cards), line)
    bid = int(match[2])
    hand = list()
    hist = dict()
    for c in match[1]:
        hand.append(card_order[c])
        hist[c] = hist.get(c,0) + 1

    wild = hist.pop('J', 0)
    counts = sorted(hist.values(), reverse=True)

    reps = counts[0] + wild if counts else wild

    if reps == 5:
        strength = 7
    elif reps == 4:
        strength = 6
    elif reps == 3:
        if counts[1] == 2:
            strength = 5
        else:
            strength = 4
    elif reps == 2:
        if counts[1] == 2:
            strength = 3
        else:
            strength = 2
    else:
        strength = 1

    hands.append((hand, bid, strength))

hands.sort(key = lambda x: tuple([x[2]] + x[0]))

answer = sum([(i+1)*hands[i][1] for i in range(len(hands))])
print(answer)
