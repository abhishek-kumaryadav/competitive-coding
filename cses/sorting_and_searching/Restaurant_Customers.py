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


def main():
    n = int_r()
    a = list()
    for _ in range(n):
        t1, t2 = intList_r()
        a.append((t1, True))
        a.append((t2, False))
    # zipped = sorted(a)
    a.sort()
    cur = 0
    maxx = 0
    for it in a:
        if it[1] == True:
            cur += 1
            maxx = max(cur, maxx)
        else:
            cur -= 1
    outStr(maxx)
    # print(zipped)


if __name__ == "__main__":
    main()