import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, log10, sqrt, log
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


def get_digits(q):
    ini = 9
    j = 1
    i = 10
    prev = 0
    while ini < q:
        # print(ini, q)
        prev = ini
        j += 1
        ini = 9 * j * i + ini
        i *= 10
    return j, prev


def main():
    queries = int_r()
    arr = list()
    for i in range(queries):
        arr.append(int_r())
    # print(arr)
    for q in arr:
        digits, minus = get_digits(q)
        # print(digits, minus)
        c = 1
        p = 9
        while True:
            if q - p <= 0:
                break
            q -= p
            c += 1
            p = 9 * (10 ** (c - 1)) * c
        q -= 1
        x = q // c
        y = q % c
        ans = 10 ** (c - 1) + x
        outStr("{}\n".format(str(ans)[y]))
        # q -= minus
        # st = ""
        # ctr = 10 ** (digits - 1)

        # while len(st) < q:
        #     st += str(ctr)
        #     ctr += 1
        # print(st, q)
        # ctr = 10 ** (digits - 1)
        # mod = q % digits
        # if mod == 0:
        #     mod = digits
        # q = ceil(q / digits)
        # print(ctr - 1, mod, q)
        # print(str((ctr - 1) + q)[mod - 1])
        # outStr("{}\n".format(st[q - 1]))
        # print(q)
        # print(digits, q % digits, q / digits)
        # print(10**(digits-1)+10/10)
    # print(len(st), len(st2), len(st3))
    # print(st3[:50])
    # maxx = int(1e3)
    # num = 1
    # i = 2
    # while floor(log10(num)) <= maxx:
    #     num = num * (10 ** (floor(log10(i) + 1))) + i
    #     i += 1


if __name__ == "__main__":
    main()