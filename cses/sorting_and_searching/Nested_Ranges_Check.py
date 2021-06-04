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
    arr1 = list()
    arr2 = list()
    for _ in range(n):
        t_a, t_b = intList_r()
        arr1.append(t_a)
        arr2.append(t_b)
    zipped = zip(arr1, arr2, [i for i in range(n)])
    zipped = sorted(
        zipped,
        key=lambda x: (x[0], n - x[1]),
    )
    # print(zipped[::-1])
    ma = -1
    contained = [0 for _ in range(n)]
    contains = [0 for _ in range(n)]
    for it in zipped:
        l, r, index = it
        if r <= ma:
            contained[index] = 1
        ma = max(ma, r)
    ma = int(1e9)
    for it in zipped[::-1]:
        # print(it, ma)
        l, r, index = it
        if r >= ma:
            # print("-- - -- ")
            contains[index] = 1
        ma = min(ma, r)
    outStr(" ".join([str(i) for i in contains]))
    outStr("\n")
    outStr(" ".join([str(i) for i in contained]))
    # out1 = [0 for _ in range(n)]
    # out2 = [0 for _ in range(n)]
    # # print(out)
    # # print(arr)
    # se = set()
    # for i, it in enumerate(arr):
    #     a, b = it
    #     # print(a, b, it)
    #     if it not in se:
    #         # print(it)
    #         # pass
    #         flag = 1
    #         for jit in se:
    #             l, r = jit
    #             if r >= b and l <= a:
    #                 out1[i] = 1

    #                 flag = 0
    #                 break
    #             # elif r >= b >= l and a <= l:
    #             #     flag = 0
    #             #     se.remove(jit)
    #             #     se.add((a, r))
    #             # elif b >= r >= a and l <= a:
    #             #     flag = 0
    #             #     se.remove(jit)
    #             #     se.add((l, b))
    #         if flag == 1:
    #             se.add((a, b))
    # print(se)


if __name__ == "__main__":
    main()