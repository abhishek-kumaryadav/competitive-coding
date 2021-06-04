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

ways = 0
reserved = [[True for j in range(8)] for i in range(8)]
cols = [False for i in range(8)]
diag1 = [False for i in range(16)]
diag2 = [False for i in range(16)]


def search(r):
    global cols
    global diag1
    global diag2
    global reserved
    global ways
    if r == 8:
        ways += 1
        return
    for c in range(8):
        if not (cols[c] or diag1[r + c] or diag2[r - c + 7] or reserved[r][c]):
            cols[c] = diag1[r + c] = diag2[r - c + 7] = True
            search(r + 1)
            cols[c] = diag1[r + c] = diag2[r - c + 7] = False


def main():
    global cols
    global diag1
    global diag2
    global reserved
    global ways
    r_string = list()

    for i in range(8):
        r_string.append(str_r())
        for j in range(8):
            reserved[i][j] = r_string[i][j] == "*"
    # print(r_string)
    # print(reserved)
    search(0)
    outStr(ways)


if __name__ == "__main__":
    main()