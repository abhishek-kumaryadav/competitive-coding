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
    wei = intList_r()
    i = 0
    j = n - 1
    ans = 0
    wei = sorted(wei)
    while i < j:
        # print(wei[j], x)
        if wei[j] > x:
            j -= 1
            continue
        elif wei[j] + wei[i] <= x:
            ans += 1
            j -= 1
            i += 1
        else:
            ans += 1
            j -= 1
    if i == j and wei[j] <= x:
        ans += 1
    outStr(ans)


if __name__ == "__main__":
    main()