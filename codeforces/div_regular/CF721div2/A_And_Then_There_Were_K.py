import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, log10, log2, sqrt, log
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
    testcases = int_r()
    for t_c in range(testcases):
        n = int_r()
        # for i in range(1, 100):
        if n == 2:
            print(1)
        else:
            print(2 ** (floor(log2(n))) - 1)


if __name__ == "__main__":
    main()