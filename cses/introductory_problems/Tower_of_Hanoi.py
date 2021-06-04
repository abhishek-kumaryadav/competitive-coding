import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from itertools import permutations
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


# @lru_cache(maxsize=None)
def tower(a, b, c, n):
    if n == 0:
        return
    tower(a, c, b, n - 1)
    # a to b with c as auxilliary
    outStr("{} {}\n".format(a, c))
    # a to c
    tower(b, a, c, n - 1)
    # b to c with a as auxiliarry


def main():
    n = int_r()
    outStr("{}\n".format((1 << n) - 1))
    # outStr(tower(n))
    tower(1, 2, 3, n)


if __name__ == "__main__":
    main()