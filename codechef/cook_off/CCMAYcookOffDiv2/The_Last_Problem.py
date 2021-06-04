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
    matx = list()
    first_val = 0
    for j in range(1, 1000 + 1):
        first_val += j

        xvals = list()
        temp_val = first_val
        for i in range(j, 1000 + j):
            xvals.append(temp_val)
            temp_val += i
        matx.append(xvals)
    # print(matx)
    testcases = int_r()
    for t_c in range(testcases):
        x1, y1, x2, y2 = intList_r()
        if x1 == x2 and y1 == y2:
            outStr("{}\n".format(matx[x1 - 1][y1 - 1]))
        else:
            summ = 0
            yinc = x1 + y1
            y_1 = matx[y1 - 1][x1 - 1]
            y_2 = matx[y2 - 1][x1 - 1]
            # print(y_1, y_2)
            while y_1 <= y_2:
                summ += y_1
                y_1 += yinc
                yinc += 1
            xinc = x1 + y2 - 1

            x_1 = matx[y2 - 1][x1 - 1]
            x_2 = matx[y2 - 1][x2 - 1]
            # print(x_1, x_2)

            while x_1 <= x_2:
                summ += x_1
                x_1 += xinc
                xinc += 1
            # outStr("{}\n".format(summ))

            # if x1 != x2 and y1 != y2:
            summ -= matx[y2 - 1][x1 - 1]
            outStr("{}\n".format(summ))

        # if y1 != y2:
        #     for y in range(y1, y2 + 1):
        #         summ += matx[y - 1][x1 - 1]
        # if x1 != x2:
        #     if y1 == y2:
        #         summ += matx[y2 - 1][x1 - 1]
        #     for x in range(x1 + 1, x2 + 1):
        #         summ += matx[y2 - 1][x - 1]
        # outStr("{}\n".format(summ))
        # summ = valx1
        # valx1 = xvals[x1]
        # while y1 + 1 < y2:
        #     summ += yinc1
        #     y1 += 1
        #     yinc1 = x1 + y1


if __name__ == "__main__":
    main()