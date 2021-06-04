import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from functools import lru_cache
from typing import Counter

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


def recur(arr, l, r, dic):
    # Calc map
    if l >= r:
        return 0
    value = 0
    for i, val in dic.items():
        value += val * (val - 1) / 2

    dicl = dic.copy()
    dicl[arr[l]] -= 1
    if dicl[arr[l]] == 0:
        dicl.pop(arr[l])
    left = recur(arr, l + 1, r, dicl)

    dicr = dic.copy()
    dicr[arr[r - 1]] -= 1
    if dicr[arr[r - 1]] == 0:
        dicr.pop(arr[r - 1])
    right = recur(arr, l, r - 1, dicr)
    return value + left + right


def sub_lists(l):
    lists = []
    for i in range(len(l) + 1):
        for j in range(i - 1):
            lists = l[j:i]
            yield lists
    # return lists


def main():
    testcases = int_r()
    for t_c in range(testcases):
        n = int_r()
        arr = intList_r()
        out = 0
        for sub_arr in sub_lists(arr):
            ctr = dict(Counter(sub_arr))
            for i, val in ctr.items():
                out += val * (val - 1) / 2
        outStr("{}\n".format(int(out)))
        # print(i)
        # print(sub_lists(arr))
        # ctr = dict(Counter(arr))
        # ctrl = ctr.copy()
        # ctrr = ctr.copy()
        # print(ctr)
        # outStr("{}\n".format(int(recur(arr, 0, len(arr), ctr))))


if __name__ == "__main__":
    main()