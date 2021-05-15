import sys
import math
import bisect
from sys import modules, stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

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


def dfs(n, k, d):
    count = 0
    if n <= 0:
        return False, 0
    for i in range(k):
        bal, ways = dfs(n - i - 1, k, d)
        if bal == True:
            count += ways
            count %= mod


def main():
    n, k, d = intList_r()
    bal, ways = dfs(n, k, d)


if __name__ == "__main__":
    main()