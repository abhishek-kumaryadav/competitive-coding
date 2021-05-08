import sys
import math

n, k = [int(x) for x in (sys.stdin.readline().split())]

while n % 200 == 0:
    n = n / 200
    k -= 1

while k > 1:
    n = n * 5 + 1
    k -= 2

if k == 1:
    n = n * 1000 + 200

sys.stdout.write(str(int(n)))