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
    n, m = intList_r()
    arr = intList_r()
    # query = list()
    # for _ in range(m):
    #     a, b = intList_r()
    #     query.append([a, b])
    zipped = zip(arr, [i for i in range(n)])
    zipped = sorted(zipped)
    # print(arr)
    # print(type(zipped))

    # print(zipped)
    _, zipped = map(list, zip(*zipped))
    # print(zipped)
    ans = 1
    for i in range(n - 1):
        ans += zipped[i] > zipped[i + 1]
    # print(zipped)
    for i in range(m):
        a, b = intList_r()
        # print(arr[a - 1], arr[b - 1])
        first_index = arr[a - 1] - 1
        second_index = arr[b - 1] - 1
        sett = set()
        if first_index + 1 < n:
            sett.add((first_index, first_index + 1))
        if first_index - 1 >= 0:
            sett.add((first_index - 1, first_index))
        if second_index + 1 < n:
            sett.add((second_index, second_index + 1))
        if second_index - 1 >= 0:
            sett.add((second_index - 1, second_index))
        for p in sett:
            l, r = p
            ans -= zipped[l] > zipped[r]

        temp = zipped[first_index]
        zipped[first_index] = zipped[second_index]
        zipped[second_index] = temp

        for p in sett:
            l, r = p
            ans += zipped[l] > zipped[r]
        outStr("{}\n".format(ans))
        # old_ans = 0
        # if abs(first_index - second_index) == 1:
        #     if first_index > second_index:
        #         temp = first_index
        #         first_index = second_index
        #         second_index = temp
        #     if first_index > 0 and zipped[first_index - 1] > zipped[first_index]:
        #         old_ans += 1
        #     if zipped[first_index] > zipped[second_index]:
        #         old_ans += 1
        #     if second_index < n - 1 and zipped[second_index] > zipped[second_index + 1]:
        #         old_ans += 1
        # else:
        #     if first_index > 0 and zipped[first_index - 1] > zipped[first_index]:
        #         old_ans += 1
        #     if first_index < n - 1 and zipped[first_index] > zipped[first_index + 1]:
        #         old_ans += 1
        #     if second_index > 0 and zipped[second_index - 1] > zipped[second_index]:
        #         old_ans += 1
        #     if second_index < n - 1 and zipped[second_index] > zipped[second_index + 1]:
        #         old_ans += 1
        # ans -= old_ans
        # # print(old_ans, zipped)

        # temp = zipped[first_index]
        # zipped[first_index] = zipped[second_index]
        # zipped[second_index] = temp
        # # print(zipped)
        # old_ans = 0
        # if abs(first_index - second_index) == 1:
        #     if first_index > second_index:
        #         temp = first_index
        #         first_index = second_index
        #         second_index = temp
        #     if first_index > 0 and zipped[first_index - 1] > zipped[first_index]:
        #         old_ans += 1
        #     if zipped[first_index] > zipped[second_index]:
        #         old_ans += 1
        #     if second_index < n - 1 and zipped[second_index] > zipped[second_index + 1]:
        #         old_ans += 1
        # else:
        #     if first_index > 0 and zipped[first_index - 1] > zipped[first_index]:
        #         old_ans += 1
        #     if first_index < n - 1 and zipped[first_index] > zipped[first_index + 1]:
        #         old_ans += 1
        #     if second_index > 0 and zipped[second_index - 1] > zipped[second_index]:
        #         old_ans += 1
        #     if second_index < n - 1 and zipped[second_index] > zipped[second_index + 1]:
        #         old_ans += 1
        # ans += old_ans
        #     # print(old_ans)
        #     ans += old_ans
        #     print(old_ans, zipped)
        #     print("")
        # ans = 1
        # for i in range(n - 1):
        #     if zipped[i] > zipped[i + 1]:
        #         ans += 1
        # outStr("{}\n".format(ans))
    # print(query)
    # print(zipped)
    # b = zip(zipped)
    # print(list(b))


if __name__ == "__main__":
    main()