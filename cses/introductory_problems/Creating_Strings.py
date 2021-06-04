import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from itertools import permutations
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


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def main():
    st = str_r()
    ctr = dict(Counter(st))
    total = factorial(len(st))
    for _, val in ctr.items():
        if val > 1:
            total = total // factorial(val)
    outStr("{}\n".format(total))
    outStr("\n".join(sorted(set(["".join(p) for p in permutations(st)]))))

    # print(st, total)


if __name__ == "__main__":
    main()