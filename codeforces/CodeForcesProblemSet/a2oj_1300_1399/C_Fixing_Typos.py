import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from functools import lru_cache
from collections import Counter

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
    s = str_r()
    # ctr = Counter(s)
    # print(dict(ctr))
    ctr = list()
    prev = s[0]
    ctr.append([s[0], 1])
    inde = 0
    # ctr.update(s[0]:1)
    for i in range(1, len(s)):
        if prev == s[i]:
            ctr[inde] = [ctr[inde][0], ctr[inde][1] + 1]
        else:
            ctr.append([s[i], 1])
            prev = s[i]
            inde += 1
    ctr = [[c, 2] if v > 2 else [c, v] for c, v in ctr]
    i = 0
    while i < len(ctr) - 1:
        if ctr[i][1] == 2 and ctr[i + 1][1] == 2:
            ctr[i + 1][1] = 1
            i += 1
        i += 1
    str = ""
    for c, v in ctr:
        for i in range(v):
            str = str + c
    outStr(str)


if __name__ == "__main__":
    main()