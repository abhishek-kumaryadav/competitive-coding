import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

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
    r, g, b = intList_r()
    sum = 0
    a = ceil(r / 3) - 1
    if a < 0:
        a = 0
    r -= a * 3
    sum += a
    a = ceil(g / 3) - 1
    if a < 0:
        a = 0
    g -= a * 3
    sum += a
    a = ceil(b / 3) - 1
    if a < 0:
        a = 0
    b -= a * 3
    sum += a
    # minn=min(a,b)
    mmin = min(r, min(g, b))
    sum += mmin
    r -= mmin
    g -= mmin
    b -= mmin
    sum += r // 3 + g // 3 + b // 3
    outStr(sum)


if __name__ == "__main__":
    main()