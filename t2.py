import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd, Counter
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


al = [
    [[], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]],
    [[6], [5, 7, 11, 13, 17, 19, 23, 29]],
    [[10], [3, 7, 11, 13, 17, 19, 23, 29]],
    [[10, 21], [11, 13, 17, 19, 23, 29]],
    [[30], [7, 11, 13, 17, 19, 23, 29]],
    [[14], [3, 5, 11, 13, 17, 19, 23, 29]],
    [[14, 15], [11, 13, 17, 19, 23, 29]],
    [[22], [3, 5, 7, 13, 17, 19, 23, 29]],
    [[22, 15], [7, 13, 17, 19, 23, 29]],
    [[22, 21], [5, 13, 17, 19, 23, 29]],
    [[26], [3, 5, 7, 11, 17, 19, 23, 29]],
    [[26, 15], [7, 11, 17, 19, 23, 29]],
    [[26, 21], [5, 11, 17, 19, 23, 29]],
    [[15], [2, 7, 11, 13, 17, 19, 23, 29]],
    [[21], [2, 5, 11, 13, 17, 19, 23, 29]],
]
count = Counter()


def find(comp, n):
    global count
    ans = 1
    for i in comp:
        ans *= count[i]
    for i in n:
        ans *= count[i] + 1
    ans %= mod
    return ans


def main():
    global count
    testcases = int_r()
    for t_c in range(testcases):
        n = int_r()
        count = Counter(list(map(int, stdin.readline().split())))
    ans = -1
    for i, j in al:
        ans += find(i, j)
        ans %= mod
    print(ans)


if __name__ == "__main__":
    main()
