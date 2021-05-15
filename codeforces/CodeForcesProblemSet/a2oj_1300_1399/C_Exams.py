# from _typeshed import OpenTextModeUpdating
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
    a = list()
    b = list()
    for i in range(n):
        tempa, tempb = intList_r()
        a.append(tempa)
        b.append(tempb)
    zipped = zip(a, b)
    zipped = sorted(zipped)
    # print(zipped)
    # zipped = [i for i in zip(*zipped)]
    # bol = True
    # for i in range(len(zipped[1]) - 1):
    #     if zipped[1][i] > zipped[1][i + 1]:
    #         bol = False
    #         break
    # outStr(zipped[1][-1] if bol else zipped[0][-1])
    # print(zipped)
    # print(a, b)
    prev = -1
    # last = -1
    for a, b in zipped:
        # print(a, b)
        if b >= prev:
            # last = max(last, b)
            prev = b
            # prev = b
        else:
            # last = max(last, a)
            prev = a
    print(prev)
    # prev=


if __name__ == "__main__":
    main()