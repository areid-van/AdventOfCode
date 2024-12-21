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

direction_key_movement = {'<': (-1,0),
                          '>': (1,0),
                          '^': (0,1),
                          'v': (0,-1)}

def make_sequence(start_pos, end_pos, reverse, button_positions):

    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    hbutton = '>' if dx>0 else '<'
    vbutton = '^' if dy>0 else 'v'

    sequence = []

    for i in range(abs(dx)):
        sequence.append(hbutton)
    for i in range(abs(dy)):
        sequence.append(vbutton)

    if reverse:
        if len(sequence) == 0 or sequence[0] == sequence[-1]:
            return None
        else:
            sequence.reverse()

    p = np.array(start_pos)
    for step in sequence:
        p = p + direction_key_movement[step]
        if not tuple(p) in button_positions.values():
            return None

    sequence.append('A')
    return sequence

def make_sequences(button_positions):

    button_sequences = {}

    for start_key, start_pos in button_positions.items():
        for end_key, end_pos in button_positions.items():
        
            sequences = [make_sequence(start_pos, end_pos, reverse, button_positions)
                         for reverse in [True, False]]

            button_sequences[(start_key, end_key)] = [x for x in sequences if x != None]
        
    return button_sequences

numeric_sequences = make_sequences(numeric_positions)
directional_sequences = make_sequences(directional_positions)

shortest_sequence_cache = {}

def shortest_sequence(code, depth):

    k = (tuple(code), depth)
    if k in shortest_sequence_cache:
        return shortest_sequence_cache[k]

    if(depth == 26):
        shortest_sequence_cache[k] = len(code)
        return len(code)
    else:
        button_sequences = directional_sequences if depth > 0 else numeric_sequences

        key = 'A'
        code_len = 0
        for next_key in code:
            code_len += min([shortest_sequence(segment, depth+1) 
                             for segment in button_sequences[(key, next_key)]])
            key = next_key
        shortest_sequence_cache[k] = code_len
        return code_len


ans = 0
for code in codes:
    shortest = shortest_sequence(code,0)
    numeric_part = int(''.join(code[0:-1]))
    ans += shortest * numeric_part


print('Answer: ', ans)
