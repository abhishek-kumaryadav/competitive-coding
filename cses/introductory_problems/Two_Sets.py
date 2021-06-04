import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from functools import lru_cache

sys.setrecursionlimit(100000000)

int_r = lambda: int(sys.stdin.readline())
str_r = lambda: sys.stdin.readline().strip()
intList_r = lambda: list(map(int, sys.stdin.readline().strip().split()))
strList_r = lambda: list(sys.stdin.readline().strip())
jn = lambda x, l: x.join(map(str, l))
mul = lambda: map(int, sys.stdin.readline().strip().split())
mulf = lambda: map(float, sys.stdin.readline().strip().split())
ceil = lambda x: int(x) if (x == int(x)) else int(x) + 1
ceildiv = lambda x, d: x // d if (x % d == 0) else x // d + 1
flush = lambda: stdout.flush()
outStr = lambda x: stdout.write(str(x))
mod = 1000000007


def main():
    n = int_r()
    # if (not (n & 1)) or (not ((n + 1) & 1)):
    #     outStr("YES")
    if (n * (n + 1) / 2) % 2:
        outStr("NO\n")
        return
    v1 = list()
    v2 = list()
    j = 0
    if n % 4:
        j = 3
        v1.append(1)
        v1.append(2)
        v2.append(3)
    else:
        j = 4
        v1.append(1)
        v1.append(4)
        v2.append(3)
        v2.append(2)
    # print(v1, v2)
    for i in range(0, (n - 1) // 4):
        v1.append(4 * i + 1 + j)
        v1.append(4 * i + 4 + j)
        v2.append(4 * i + 2 + j)
        v2.append(4 * i + 3 + j)
    outStr("YES\n")
    outStr("{}\n".format(len(v1)))
    str1 = " ".join([str(i) for i in v1])
    outStr("{}\n".format(str1))
    outStr("{}\n".format(len(v2)))
    str1 = " ".join([str(i) for i in v2])
    outStr("{}\n".format(str1))


if __name__ == "__main__":
    main()