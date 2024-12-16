from sympy import nonlinsolve, solve, Symbol


with open('input/24.txt') as f:
    lines = f.readlines()

p = list()
v = list()
for line in lines:
    pv = line.split('@')
    p.append([float(x) for x in pv[0].split(',')])
    v.append([float(x) for x in pv[1].split(',')])

low = 200000000000000
high = 400000000000000

answer = 0
for i in range(len(p)):
    mi = v[i][1]/v[i][0]
    bi = p[i][1] - v[i][1]*p[i][0]/v[i][0]
    for j in range(i+1,len(p)):
        mj = v[j][1]/v[j][0]
        bj = p[j][1] - v[j][1]*p[j][0]/v[j][0]
        if mi == mj:
            continue
        else:
            x = (bj-bi)/(mi-mj)
            y = mi*x + bi
            ti = (x - p[i][0])/v[i][0]
            tj = (x - p[j][0])/v[j][0]
            if x >= low and x <= high and y >= low and y <= high and ti>0 and tj>0:
                answer += 1

print(answer)

v0 = list()
p0 = list()
t = list()
for i in range(3):
    v0.append(Symbol('v0%d'%i, real=True))
    p0.append(Symbol('p0%d'%i, real=True))
    t.append(Symbol('t%d'%i, real=True, positive=True))

eqns = list()
for i in range(3):
    for j in range(3):
        eqns.append(p[j][i] + v[j][i]*t[j] - p0[i] - v0[i]*t[j])

sol = nonlinsolve(eqns, p0+v0+t)
answer2 = sum(sol.args[0][0:3])
print(answer2)

