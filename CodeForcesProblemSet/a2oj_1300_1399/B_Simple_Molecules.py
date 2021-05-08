import sys
import math

lls = [int(x) for x in sys.stdin.readline().split()]
lls = zip(lls, [1, 2, 3])
# print(list(lls))
sor = sorted(lls)
# print(a, b, c, _)
# print(a[0], b[0], c)
minbonds = 0
liss = [x[0] for x in sor]
inde = [x[1] for x in sor]
a, b, c = [x for x in liss]
print(liss)
print(inde)
while a >= 2:
    if c == a + b:
        break
    else:
        minbonds += 1
        a, b, c = [x - 2 for x in [a, b, c]]

if c == a + b:
    a1, b1, c1 = [str(int(minbonds)), str(int(minbonds + b)), str(int(minbonds + a))]
    print(a1, b1, c1)
    print(inde)
    sor = sorted(zip(inde, [a1, b1, c1]))
    print(list(sor))
    sys.stdout.write(" ".join([sor[0][1], sor[1][1], sor[2][1]]))
else:
    sys.stdout.write("Impossible")
