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


def factors(k):
    listt = list()
    i = 2
    while i < (ceil(k / 2) + 1):
        if k % i == 0:
            k /= i
            listt.append(i)
        else:
            i += 1
    listt.append(int(k))
    return listt


def main():
    testcases = int_r()
    for t_c in range(testcases):
        k = int_r()
        facs = factors(k)
        # facs.append(k)
        # print(facs)
        tot = 100
        for i in facs:
            if tot % i == 0:
                tot /= i
                k /= i
        outStr("{}\n".format(int(tot)))


if __name__ == "__main__":
    main()