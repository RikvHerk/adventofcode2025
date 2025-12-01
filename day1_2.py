with open("day1.txt", "r") as file:
    data = file.readlines()

data = [int(i.replace("L","-").replace("R","")) for i in data]

x = 50
password = 0
for i in data:
    if i > 0:
        password += int((x + i)/100)
    if i < 0:
        password += int((100 - x - i)/100)
        if x == 0:
            password -= 1
    x = (x + i) % 100

print(password)