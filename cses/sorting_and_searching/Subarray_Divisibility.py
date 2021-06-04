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
    arr = intList_r()
    count = 0
    csum = [0]
    cdiv = 0
    for i in arr:

        if i % n == 0:
            cdiv += 1
        else:
            count += i
            csum.append(count)
    # print(csum)
    count = 0
    for i, it in enumerate(arr):
        # sfind = x + csum[i]
        #  find if sfind is in CSUM
        # inde = bisect.bisect_left(csum, sfind)
        # print(sfind, csum[i], inde)
        # if inde != n + 1 and csum[inde] == sfind:
        # count += 1
        for j in range(i + 1, n + 1):
            if (csum[j] - csum[i]) % n == 0:
                count += 1
    cdiv = pow(2, cdiv) - 1
    if cdiv != 0:
        count *= cdiv
    outStr(count)


if __name__ == "__main__":
    main()