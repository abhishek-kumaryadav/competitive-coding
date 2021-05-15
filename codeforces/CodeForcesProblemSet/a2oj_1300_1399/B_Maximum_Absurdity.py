import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sin, sqrt, log
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


# carr = list()


def main():
    global carr
    n, k = intList_r()
    arr = intList_r()
    carr = list(running_sum(arr))
    carr.insert(0, 0)
    # print(carr)
    smaxabsur = -1
    sindex = -1
    total = -1
    indexes = list()
    for i in range(n - 2 * k, -1, -1):
        # print(i, sindex)
        absur = carr[i + k] - carr[i]
        sec_absur = carr[i + 2 * k] - carr[i + k]
        # print(sec_absur, smaxabsur)
        if sec_absur >= smaxabsur:
            # print("shouldnt go here")
            smaxabsur = sec_absur
            sindex = i + k
        if total <= absur + smaxabsur:
            total = absur + smaxabsur
            # print(i, sindex)
            indexes = [str(i + 1), str(sindex + 1)]
    # max_absurdy = -1

    # for i in range(n - 2 * k + 1):
    #     absur = carr[i + k] - carr[i]
    #     index, max_absur = findmaxinrange(i + k, n - k + 1, k)
    #     # pass
    #     if index > 0 and absur + max_absur > max_absurdy:
    #         max_absurdy = absur + max_absur
    # indexes = [str(i + 1), str(index + 1)]
    outStr(" ".join(indexes))


if __name__ == "__main__":
    main()