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
    sett = set()
    maxx = -1
    templist = list()
    for i, it in enumerate(arr):
        # print(templist, sett)
        if it in sett:
            index = 0
            while templist[index] != it:
                sett.discard(templist[index])
                index += 1

            if index + 1 < len(templist):
                templist = templist[index + 1 :]
            else:
                templist = []
        templist.append(it)
        maxx = max(len(templist), maxx)
        sett.add(it)
    outStr(maxx)


if __name__ == "__main__":
    main()