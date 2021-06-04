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
    n, x = intList_r()
    # print(index)
    arr = intList_r()
    if n > 3:
        dic = dict()
        dic[arr[0] + arr[1]] = (0, 1)
        for i in range(2, n - 1):

            j = i + 1
            while j < n:
                psum = x - arr[i] - arr[j]
                if psum in dic:
                    flag = 1
                    outStr(
                        "{} {} {} {}".format(
                            i + 1, j + 1, dic[psum][0] + 1, dic[psum][1] + 1
                        )
                    )
                    return
                j += 1
            for m in range(0, i):
                dic[arr[m] + arr[i]] = (m, i)
    outStr("IMPOSSIBLE")


if __name__ == "__main__":
    main()