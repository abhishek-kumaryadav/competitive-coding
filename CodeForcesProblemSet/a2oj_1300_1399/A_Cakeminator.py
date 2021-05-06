x, y = [int(m) for m in input().split()]
# print(x, y)
setx = {-1}
sety = {-1}
for i in range(0, x):
    row = input()
    for j in range(0, len(row)):
        if row[j] == "S":
            setx.add(i)
            sety.add(j)
print(x * y - (len(setx) - 1) * (len(sety) - 1))
