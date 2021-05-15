import sys
import math
import bisect
from sys import stdin, stdout
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


def main():
    n, m = intList_r()
    sets = []
    for i in range(m):
        a, b = intList_r()
        flag = 0
        for se in sets:
            if a in se or b in se:
                se.add(a)
                se.add(b)
                flag = 1
        if not flag:
            newset = set()
            newset.add(a)
            newset.add(b)
            sets.append(newset)

    set4 = [i for i in sets if len(i) > 3]
    set3 = [i for i in sets if len(i) == 3]
    set2 = [i for i in sets if len(i) == 2]
    len4 = sum([len(i) for i in set4])
    len3 = sum([len(i) for i in set3])
    len2 = sum([len(i) for i in set2])
    # set1 = [i for i in sets if len(i) == 1]
    len1 = n - len2 - len3 - len4
    # print(sets)
    # print(set2)
    # print(set3)
    # print(set4)
    # print(len4)
    # print(len3)
    # print(len2)
    # print(len1)
    if int(len4 / 4) > 0 or int(len2 / 2) > len1 or (int(len1 - len2 / 2)) % 3 != 0:
        outStr(-1)
    else:
        allset = set()
        for i in set3:
            allset = allset.union(i)
        for i in set2:
            allset = allset.union(i)
        for i in set4:
            allset = allset.uniosn(i)
        set1 = set([i + 1 for i in range(n)]) - allset
        set1 = list(set1)
        set2 = list(set2)
        # print(set1)
        for i in set3:
            outStr(" ".join([str(j) for j in i]))
            outStr("\n")
        i = 0
        for it in set2:
            lissto = [str(j) for j in it]
            lissto.append(str(set1[i]))
            # .extend([str(set1[i])])
            # print(lissto)
            outStr(" ".join(lissto))
            outStr("\n")
            i += 1
        while i < len(set1):
            outStr(" ".join([str(set1[i]), str(set1[i + 1]), str(set1[i + 2])]))
            outStr("\n")
            i += 3


if __name__ == "__main__":
    main()