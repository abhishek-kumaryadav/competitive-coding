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
    index = [i + 1 for i in range(n)]
    # print(index)
    arr = sorted(zip(intList_r(), index))
    # print(arr)
    flag = 0
    for i in range(n):
        j = i + 1
        k = n - 1
        while j < k:
            # print(i, j, k)
            sum = arr[i][0] + arr[j][0] + arr[k][0]
            if sum == x:
                outStr("{} {} {}".format(arr[i][1], arr[j][1], arr[k][1]))
                flag = 1
                break
            elif sum > x:
                k -= 1
            else:
                j += 1
        if flag:
            break
    if not flag:
        outStr("IMPOSSIBLE")


if __name__ == "__main__":
    main()