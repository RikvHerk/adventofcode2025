with open("day1.txt", "r") as file:
    data = file.readlines()

data = [int(i.replace("L","-").replace("R","")) for i in data]

x = 50
password = 0
for i in data:
    x = (x + i) % 100
    if x == 0:
        password += 1

print(password)