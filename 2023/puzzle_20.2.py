import re
import math


with open('input/20.txt') as f:
    lines = f.readlines()

modules = dict()
for line in lines:
    match = re.match('([%&]?)([a-z]+) -> ([a-z, ]+)', line)
    typ = match[1] if len(match[1]) > 0 else None
    name = match[2]
    dests = [x.strip() for x in match[3].split(',')]
    if typ == '&':
        value = dict()
    else:
        value = False
    modules[name] = {'type': typ, 'value': value, 'dst' : dests}

for n,v in modules.items():
    for d in v['dst']:
        if d in modules and modules[d]['type'] == '&':
            modules[d]['value'][n] = False
    
ans = dict()
for i in range(1,9000):
    receivers = [('button', 'broadcaster', False)]

    while len(receivers) > 0:
        newreceivers = list()

        for x in receivers:
            sender  = x[0]
            receiver = x[1]
            pulse = x[2]
            if receiver in modules:
                module = modules[receiver]
                typ = module['type']
                val = module['value']
                if typ:
                    if typ == '%':
                        if not pulse:
                            module['value'] = not val
                            pulse = not val
                        else:
                            pulse = None
                    else:
                        val[sender] = pulse
                        pulse = True
                        for v in val.values():
                            pulse = pulse and v
                        pulse = not pulse

                if not pulse is None:
                    for d in module['dst']:
                        newreceivers.append((receiver, d, pulse))

                if receiver == 'rm':
                    for kk, vv in val.items():
                        if vv:
                            yy = ans.get(kk,(None, None))
                            last = yy[0]
                            if last and last == i:
                                continue
                            delta = yy[1]
                            if last:
                                ans[kk] = (i, i-last)
                            else:
                                ans[kk] = (i, None)

        receivers = newreceivers

answer = 1
for x in ans.values():
    answer = math.lcm(answer, x[1])
print(answer)
