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


def main():
    st = str_r()
    # print(st)
    ctr = dict(Counter(st))
    count = 0
    index = -1
    strr = ""
    for i in ctr:
        if ctr[i] & 1:
            count += 1
            if count == 2:
                break
            index = i
        else:
            strr += str(i) * (ctr[i] // 2)

    # ctr.pop(index)
    if count > 1:
        outStr("NO SOLUTION")
    else:
        if index != -1:
            a, b = index, ctr[index]
            strr = strr + str(a) * b + strr[::-1]
        else:
            strr = strr + strr[::-1]
        outStr(strr)


if __name__ == "__main__":
    main()