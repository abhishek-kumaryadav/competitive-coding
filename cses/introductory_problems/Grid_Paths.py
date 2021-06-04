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

# int vis[7][7]={};
vis = [[0 for j in range(7)] for i in range(7)]
ways = 0
st = ""
visited = 0
reserved = [0] * 49


def search(r, c):
    global ways
    global vis
    global visited
    global st
    global reserved

    if r == 6 and c == 0:
        if visited == 48:
            ways += 1
            # print(ways)
        return

    t = (
        vis[r][c]
        or (
            (
                ((r == 0 and vis[r + 1][c]) or (r == 6 and vis[r - 1][c]))
                and c > 0
                and c < 6
                and (not vis[r][c + 1])
                and (not vis[r][c - 1])
            )
            or (
                ((c == 0 and vis[r][c + 1]) or (c == 6 and vis[r][c - 1]))
                and r > 0
                and r < 6
                and (not vis[r + 1][c])
                and (not vis[r - 1][c])
            )
        )
        or (
            r > 0
            and r < 6
            and c > 0
            and c < 6
            and vis[r - 1][c]
            and vis[r + 1][c]
            and (not vis[r][c - 1])
            and (not vis[r][c + 1])
        )
        or (
            r > 0
            and r < 6
            and c > 0
            and c < 6
            and vis[r][c - 1]
            and vis[r][c + 1]
            and (not vis[r - 1][c])
            and (not vis[r + 1][c])
        )
    )
    if t:
        return
    vis[r][c] = 1
    if reserved[visited] != -1:
        if reserved[visited] == 0:
            if r > 0 and (not vis[r - 1][c]):
                visited += 1
                search(r - 1, c)
                visited -= 1
        elif reserved[visited] == 2:
            if r < 6 and (not vis[r + 1][c]):
                visited += 1
                search(r + 1, c)
                visited -= 1
        elif reserved[visited] == 3:
            if c > 0 and (not vis[r][c - 1]):
                visited += 1
                search(r, c - 1)
                visited -= 1
        elif reserved[visited] == 1:
            if c < 6 and (not vis[r][c + 1]):
                visited += 1
                search(r, c + 1)
                visited -= 1
        vis[r][c] = 0
        return
    if r > 0 and (not vis[r - 1][c]):
        visited += 1
        search(r - 1, c)
        visited -= 1
    if r < 6 and (not vis[r + 1][c]):
        visited += 1
        search(r + 1, c)
        visited -= 1
    if c > 0 and (not vis[r][c - 1]):
        visited += 1
        search(r, c - 1)
        visited -= 1
    if c < 6 and (not vis[r][c + 1]):
        visited += 1
        search(r - 1, c + 1)
        visited -= 1
    vis[r][c] = 0


def main():
    global st
    global reserved
    st = str_r()
    for i in range(len(st)):
        if st[i] == "?":
            reserved[i] = -1
        elif st[i] == "U":
            reserved[i] = 0
        elif st[i] == "R":
            reserved[i] = 1
        elif st[i] == "D":
            reserved[i] = 2
        elif st[i] == "L":
            reserved[i] = 3
    # print(reserved)
    search(0, 0)
    print(ways)


if __name__ == "__main__":
    main()