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
    testcases = int_r()
    for t_c in range(testcases):
        n = int_r()
        arr = intList_r()
        sett = list()
        arr = sorted(arr)
        for i in range(1, n):
            bisect.insort(sett, (abs(arr[i] - arr[i - 1]), i))
            # sett.insert(0, (abs(arr[i] - arr[i - 1]), i))
            # sett = sorted(sett)
            pair = sett[0]
            if pair[0] >= arr[i]:
                continue
            else:
                sett.pop(0)
        print(len(sett) + 1)
        #
        # BRUTE FORCE
        #
        # flag = False
        # size = 1
        # for i in range(n - 1):
        #     perm_list = [0 if tt < i else 1 for tt in range(n)]
        #     # perm_list = [1] * n
        #     # for j in range(i):
        #     #     perm_list[j] = 0
        #     # print(perm_list)
        #     # perms = set(list(permutations(perm_list)))
        #     sett = set()
        #     for _perm in permutations(perm_list):
        #         perm = tuple(_perm)
        #         if perm not in sett:
        #             sett.add(perm)
        #         else:
        #             continue
        #         arrt = [it for i, it in enumerate(arr) if perm[i]]

        #         # arrt = list(filter(("x").__ne__, arrt))
        #         flag2 = True
        #         maxx = max(arrt)
        #         # print(maxx)
        #         sz = len(arrt)
        #         for j in range(sz - 1):
        #             for k in range(j + 1, sz):
        #                 temp = abs(arrt[j] - arrt[k])
        #                 # print(temp)
        #                 if temp < maxx:
        #                     flag2 = False
        #                     break
        #             if not flag2:
        #                 break
        #         if flag2:
        #             # print(arrt)
        #             size = sz
        #             flag = True
        #             break
        #         # print(arrt)
        #     if flag:
        #         break
        # print(size)


if __name__ == "__main__":
    main()