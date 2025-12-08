import numpy as np

with open("day3.txt", "r") as file:
    data = file.readlines()

data = [[int(j) for j in list(i)[:-1]] for i in data]

def find(b, a, i):
    if i == 12:
        return True
    if not b:
        return False
    for j in np.arange(9, -1, -1):
        for k in range(len(b)):
            if b[k] == j:
                r = b[k+1:]
                a[i] = j
                if find(r, a, i+1):
                    return True

s = 0
for l in data:
    j = [0]*12
    find(l, j, 0)

    for i in range(12):
        s += 10**(11-i) * j[i]

print(s)