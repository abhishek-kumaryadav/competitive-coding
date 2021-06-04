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
    # count2 = 0
    count5 = 0
    i = 5
    while i <= n:

        # for i in range(5, n + 1, 5):
        #     while not (int(i) & 1):
        #         i /= 2
        #         count2 += 1
        # while i % 10 == 0 or i % 10 == 5:
        # i /= 5
        # count5 += 1
        count5 += n // i
        # print(count5)
        i *= 5
    outStr(int(count5))


if __name__ == "__main__":
    main()