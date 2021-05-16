import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
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


def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    elif (n - 1) % 6 == 0 or (n + 1) % 6 == 0:
        count = 0
        for i in range(2, ceil(sqrt(n) + 1)):
            if n % i == 0:
                count += 1
                break
        if count == 0:
            return True
        else:
            return False
    else:
        return False


def main():
    n, m = intList_r()
    dictt = dict()
    prev = 100003
    for i in range(100000, 0, -1):
        if isPrime(i):
            prev = i
        dictt[i] = prev
    # for i in range(1, 100):
    #     print(dictt[i])
    # print(dictt[48])
    # print(isPrime(1))
    mat = list()
    for i in range(n):
        arr = intList_r()
        mat.append(arr)
    sum_min = 1000000
    for i in range(len(mat)):
        # print(mat[i])
        sum = 0
        for j in range(len(mat[0])):
            sum += dictt[mat[i][j]] - mat[i][j]
        sum_min = min(sum, sum_min)
        # print(i, j, sum_min)
    for j in range(len(mat[0])):
        sum = 0
        for i in range(len(mat)):
            sum += dictt[mat[i][j]] - mat[i][j]
        sum_min = min(sum, sum_min)
        # print(i, j, sum_min)
    outStr(sum_min)

    # print(mat)


if __name__ == "__main__":
    main()