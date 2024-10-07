
p = []
g = []
y = []
r = []
b = {}
f = {}
x = {}
q = int(input())

for i in range(0, q):
    p.append(int(input()))
    g.append(int(input()))
    y.append(int(input()))

for i in range(0, q):
    n = 0
    s = p[i] - 1
    while s > 1:
        s = s / 2
        n = n + 1
    f[i] = 0
    for j in range(0, n):
        base = y[i]*pow(g[i], p[i] - 1 - f[i], p[i])
        r.insert(i, pow(base, int((p[i]-1)/pow(2, j+1)), p[i]))
        if r[i] == 1:
            b[j] = 0
        else:
            b[j] = 1
        f[i] = f[i] + pow(2, j)*b[j]
    if f[i] == 0:
        f[i] = p[i] - 1
    print(f[i])

