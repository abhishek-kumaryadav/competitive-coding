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
    if n == 1:
        outStr("1")
    elif n <= 3:
        outStr("NO SOLUTION")
    elif n == 4:
        outStr("2 4 1 3")
    else:
        l = 1
        r = n
        mid = ceil((l + r) / 2)
        # 6
        # mid=4,l=1,r=6
        # 1 4 6 2 5 3
        outStr("{} {} {} ".format(l, mid, r))
        l += 1
        r -= 1
        while l < mid and r > mid:
            outStr("{} {} ".format(l, r))
            l += 1
            r -= 1
        outStr("{}".format(l))


if __name__ == "__main__":
    main()