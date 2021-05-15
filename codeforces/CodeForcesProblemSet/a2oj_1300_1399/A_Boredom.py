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


def dfs(ar):
    # print(ar)
    # new = ar.copy()
    if len(ar) <= 1:
        return sum([val for c, val in ar.items()])
    else:
        maxx = -1
        # print(new)
        for i in ar:
            # print(i)
            neww = ar.copy()
            val = neww[i]
            # print(val)
            neww.pop(i)
            try:
                neww.pop(i - 1)
            except:
                pass
            try:
                neww.pop(i + 1)
            except:
                pass
            val += dfs(neww)
            maxx = max(maxx, val)
        return maxx


def main():
    n = int_r()
    arr = intList_r()
    dictt = dict()
    for i in arr:
        if i in dictt:
            dictt[i] += i
        else:
            dictt[i] = i
    # print(dictt)
    out = dfs(dictt)
    print(out)


if __name__ == "__main__":
    main()