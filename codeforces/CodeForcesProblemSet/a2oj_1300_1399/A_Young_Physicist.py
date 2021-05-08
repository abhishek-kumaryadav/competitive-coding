x = int(input())
sumx = 0
sumy = 0
sumz = 0
for i in range(0, x):
    m, n, o = [int(z) for z in input().split()]
    # print(m, n, o)
    sumx += m
    sumy += n
    sumz += o
if sumx == 0 and sumy == 0 and sumz == 0:
    print("YES")
else:
    print("NO")
