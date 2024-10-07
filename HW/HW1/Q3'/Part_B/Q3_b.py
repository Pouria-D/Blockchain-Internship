import hashlib
import math
h1 = {}
h2 = {}
h3 = {}
h4 = {}
h5 = {}
for i in range(1, 21):
    h1[i] = input()
m = int(input())
for i in range(1, 11):
    h2[i] = (hashlib.sha256((str(h1[2 * i - 1]) + str(h1[2 * i])).encode()).hexdigest())
for i in range(1, 6):
    h3[i] = (hashlib.sha256((str(h2[2 * i - 1]) + str(h2[2 * i])).encode()).hexdigest())
h3[6] = h3[5]
for i in range(1, 4):
    h4[i] = (hashlib.sha256((str(h3[2 * i - 1]) + str(h3[2 * i])).encode()).hexdigest())
h4[4] = h4[3]
for i in range(1, 3):
    h5[i] = (hashlib.sha256((str(h4[2 * i - 1]) + str(h4[2 * i])).encode()).hexdigest())

h = hashlib.sha256((str(h5[1]) + str(h5[2])).encode()).hexdigest()
print(h)
if m % 2 == 0:
    print(h1[m-1])
else:
    print(h1[m+1])

if math.ceil(m / 2) % 2 == 0:
    print(h2[math.ceil(m / 2) - 1])
else:
    print(h2[math.ceil(m / 2) + 1])

if math.ceil(m / 4) % 2 == 0:
    print(h3[math.ceil(m / 4) - 1])
else:
    print(h3[math.ceil(m / 4) + 1])

if math.ceil(m / 8) % 2 == 0:
    print(h4[math.ceil(m / 8) - 1])
else:
    print(h4[math.ceil(m / 8) + 1])

if math.ceil(m / 16) % 2 == 0:
    print(h5[math.ceil(m / 16) - 1])
else:
    print(h5[math.ceil(m / 16) + 1])

