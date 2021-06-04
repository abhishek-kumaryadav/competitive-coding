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
mod = 100000000


@lru_cache(maxsize=None)
def dp(n1, n2, k1, k2, c1, c2):
    if n1 + n2 == 0:
        return 1
    dpl = 0
    dpr = 0
    if c1 < k1 and n1 > 0:
        dpl = dp(n1 - 1, n2, k1, k2, c1 + 1, 0)
    if c2 < k2 and n2 > 0:
        dpr = dp(n1, n2 - 1, k1, k2, 0, c2 + 1)
    return (dpl % mod + dpr % mod) % mod


def main():
    n1, n2, k1, k2 = intList_r()
    outStr(dp(n1, n2, k1, k2, 0, 0) % mod)


if __name__ == "__main__":
    main()