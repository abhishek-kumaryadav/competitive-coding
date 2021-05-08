import sys

n = int(sys.stdin.readline())
arr = [int(x) % 200 for x in (sys.stdin.readline().split())]
count = 0
for i, it in enumerate(arr):
    for j in range(i + 1, n):
        if abs(arr[i] - arr[j]) % 200 == 0:
            count += 1
sys.stdout.write(str(count))