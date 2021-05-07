import sys

rl = sys.stdin.readline
b = []

N, k = map(int, rl().split())
for i in range(N):
    b.append(int(rl()))
n = len([x / x for x in b if ((x % k) == 0)])

sys.stdout.write(str(n))
