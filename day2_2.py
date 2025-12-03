import numpy as np

with open("day2.txt", "r") as file:
    data = file.readline()

data = [i.split("-") for i in data.split(",")]

s = 0
for i in data:  
    for x in np.arange(int(i[0]), int(i[1])+1):
        y = str(x)
        for j in np.arange(2, len(y)+1):
            if len(y) % j == 0:
                l = int(len(y)/j)
                if len(set([y[k*l:(k+1)*l] for k in range(int(len(y)/l))])) == 1:
                    s += x
                    break
print(s)