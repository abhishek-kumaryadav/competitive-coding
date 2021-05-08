n = int(input())
numpass = 0
maxpass = -1
for i in range(0, n):
    a, b = [int(x) for x in input().split()]
    numpass = numpass - a + b
    maxpass = max(maxpass, numpass)
print(maxpass)
