import re

with open('input/5.txt') as f:
    lines = f.readlines()

rules = list()
updates = list()

for line in lines:
    match = re.match('([0-9]+)\\|([0-9]+)', line)
    if match:
        rules.append((int(match[1]), int(match[2])))
    else:
        try:
            updates.append([int(x.strip()) for x in line.split(',')])
        except ValueError:
            pass


def good_order(rules, update):

    accept = True 
    for rule in rules:
        l = rule[0]
        r = rule[1]
        if l in update and r in update and (update.index(l) > update.index(r)):
            return False

    return True


ans = 0
for update in updates:
    if good_order(rules, update):
        continue

    solutions = [[update.pop(0)]]
    while len(update):
        page = update.pop(0)

        new_solutions = []
        for solution in solutions:
            for j in range(0, len(solution)+1):
                trial = [x for x in solution]
                trial.insert(j, page)
                if good_order(rules, trial):
                    new_solutions.append(trial)
        solutions = new_solutions

    solution = solutions[0]
    ans += solution[len(solution)//2]

print('Answer: ', ans)
