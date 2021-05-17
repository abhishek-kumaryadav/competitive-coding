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


def sieveOfEra(n):
    prime = [True for i in range(n + 1)]
    for i in range(2, ceil(sqrt(n)) + 1):
        if prime[i] == True:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return prime


def main():
    n = int_r()
    arr = intList_r()
    primes = sieveOfEra(int(1e6))
    primes[0] = False
    primes[1] = False
    for i in arr:
        sq = sqrt(i)
        if ceil(sq) == floor(sq) and primes[int(sq)]:
            outStr("YES\n")
        else:
            outStr("NO\n")
    # for i in arr:
    # outStr("YES\n" if isPrime(i) else "NO\n")
    # print(sieveOfEra(20))


if __name__ == "__main__":
    main()