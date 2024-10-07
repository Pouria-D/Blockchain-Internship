
p = []
g = []
y = []
r = []
y1 = []
q = int(input())

for i in range(0, q):
    p.append(int(input()))
    g.append(int(input()))
    y.append(int(input()))
    y1.insert(i, int((y[i]*g[i]) % p[i]))

for i in range(0, q):
    # calculate b0:
    r.insert(i, pow(y[i], int((p[i]-1)/2), p[i]))
    if r[i] == 1:
        b0 = 0
    else:
        b0 = 1
    # calculate b1:
    if b0 == 1:
        r.insert(i, pow(y1[i], int((p[i] - 1) / 4), p[i]))
        if r[i] == 1:
            b1 = 1
        else:
            b1 = 0
    else:
        r.insert(i, pow(y[i], int((p[i] - 1) / 4), p[i]))
        if r[i] == 1:
            b1 = 0
        else:
            b1 = 1
    b = str(b1)+str(b0)
    print(b)
