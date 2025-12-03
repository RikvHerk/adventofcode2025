import numpy as np

with open("day2.txt", "r") as file:
    data = file.readline()

data = [i.split("-") for i in data.split(",")]

s = 0
for i in data:
    if len(i[0]) % 2 == 1 and len(i[0]) == len(i[1]):
        continue
    
    for x in np.arange(int(i[0]), int(i[1])+1):
        y = str(x)
        if y[0:int(len(y)/2)] == y[int(len(y)/2):]:
            s += x

print(s)