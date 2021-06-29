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
    # print(func(n))
    arr = [0, 1, 2, 4, 8, 16, 32]
    if n <= 6:
        print(arr[n])
    else:
        summ = sum(arr)
        arr.append(summ)
        for i in range(8, n + 1):
            # print(arr[i - 1], arr[i - 7])
            out = (arr[i - 1] * 2 - arr[i - 7]) % mod
            arr.append(out)
            # arr.append(summ)
        print(arr[n])
        # print(arr[n])


if __name__ == "__main__":
    main()