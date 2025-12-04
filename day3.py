with open("day3.txt", "r") as file:
    data = file.readlines()

data = [[int(j) for j in list(i)[:-1]] for i in data]

def find(b, m):
    for i in range(len(b)):
        if b[i] == m:
            r = b[i+1:]
            if not r:
                return find(b, m-1)
            return m, max(r)
s = 0
for l in data:
    m, n = find(l, max(l))
    s += 10*m + n

print(s)