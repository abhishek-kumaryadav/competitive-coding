import sys

rl = sys.stdin.readline
n = int(rl())
arr = [int(x) for x in rl().split()]
# print(n, arr)
maxcount = -1
for i in range(n):
    count = 0
    for j in range(i, n):
        if arr[j] == 0:
            count += 1
        else:
            count -= 1
        # print(count)
        maxcount = max(maxcount, count)
    # print("\n")

sys.stdout.write(str(maxcount + sum(arr)))
