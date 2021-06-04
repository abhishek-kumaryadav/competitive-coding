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
    n, x = intList_r()
    arr = intList_r()
    count = 0
    csum = [0]

    for i in arr:
        count += i
        csum.append(count)
    # print(csum)
    count = 0
    for i, it in enumerate(arr):
        j = i + 1
        # su = 0
        sfind = x + csum[i]
        # while j <= n:
        #     su = csum[j] - csum[i]
        #     # print(su, i, j - 1)
        #     if su == x:
        #         count += 1
        #         break
        #     elif su > x:
        #         break
        #     j += 1

        #  find if sfind is in CSUM
        inde = bisect.bisect_left(csum, sfind)
        # print(sfind, csum[i], inde)
        if inde != n + 1 and csum[inde] == sfind:
            count += 1
    outStr(count)


if __name__ == "__main__":
    main()