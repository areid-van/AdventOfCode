import re
import numpy as np


with open('input/20.txt') as f:
#with open('test/20.txt') as f:
#with open('test/20.2.txt') as f:
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
    
#print(modules)
Nlow = 0
Nhigh = 0
for i in range(1000):
    receivers = [('button', 'broadcaster', False)]

    while len(receivers) > 0:
        for r in receivers:
            if r[2]:
                Nhigh += 1
            else:
                Nlow += 1

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

        receivers = newreceivers

print(Nhigh*Nlow)
