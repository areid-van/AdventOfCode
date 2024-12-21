import re
import numpy as np

with open('input/21.txt') as f:
    lines = f.readlines()

codes = []
for line in lines:
    match = re.match('[0-9A]*', line.strip())
    if match:
        codes.append(list(match[0]))

numeric_positions = {'0': (1,0),
                     'A': (2,0),
                     '1': (0,1),
                     '2': (1,1),
                     '3': (2,1),
                     '4': (0,2),
                     '5': (1,2),
                     '6': (2,2),
                     '7': (0,3),
                     '8': (1,3),
                     '9': (2,3)}

directional_positions = {'<': (0,0),
                         'v': (1,0),
                         '>': (2,0),
                         '^': (1,1),
                         'A': (2,1)}

directional_key_movement = {'<': (-1,0),
                            '>': (1,0),
                            '^': (0,1),
                            'v': (0,-1)}

def shortest_sequences(code, button_positions):
    pos = button_positions['A']
    sequences = [[]]
    for key in code:
        new_pos = button_positions[key]
        dx = new_pos[0] - pos[0]
        dy = new_pos[1] - pos[1]
        hbutton = '>' if dx>0 else '<'
        vbutton = '^' if dy>0 else 'v'
        seq = []
        for i in range(abs(dx)):
            seq.append(hbutton)
        for i in range(abs(dy)):
            seq.append(vbutton)

        seqs = [seq]
        if len(seq) > 1 and seq[0] != seq[-1]:
            seq2 = list(seq)
            seq.reverse()
            seqs.append(seq2)

        new_sequences = []
        for path in sequences:
            for s in seqs:
                bad = False
                p = np.array(pos)
                for step in s:
                    p = p + directional_key_movement[step]
                    if not tuple(p) in button_positions.values():
                        bad = True
                if not bad:
                    new_sequences.append(path + s + ['A'])

        sequences = new_sequences    
        pos = new_pos

    return sequences



ans = 0
for code in codes:
    shortest = 2**60
    for path in shortest_sequences(code, numeric_positions):
        for path2 in shortest_sequences(path, directional_positions):
            for path3 in shortest_sequences(path2, directional_positions):
                shortest = min(shortest, len(path3))
    numeric_part = int(''.join(code[0:-1]))
    ans += shortest * numeric_part


print('Answer: ', ans)
