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


def running_sum(a):
    tot = 0
    for item in a:
        tot += item
        yield tot


def main():
    n, t = intList_r()
    arr = intList_r()
    cnf = list(running_sum(arr))
    cnf.insert(0, 0)
    print(cnf)
    # for i in range(len(cnf)):
    # print(bisect.bisect_left(cnf, 8))
    for i in range(n):
        print(bisect.bisect_left(cnf, t - cnf[i]))

    # maxbooks = -1
    # for i in range(len(arr)):
    #     books = 0
    #     sum = 0
    #     j = i
    #     while j < n and sum + arr[j] <= t:
    #         sum += arr[j]
    #         books += 1
    #         j += 1
    #     maxbooks = max(maxbooks, books)
    #     # print(i, sum, books)
    # outStr(maxbooks)


if __name__ == "__main__":
    main()