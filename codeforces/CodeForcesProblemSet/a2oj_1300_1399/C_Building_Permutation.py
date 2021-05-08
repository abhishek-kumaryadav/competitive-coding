import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
count = 0
for i, it in enumerate(sorted(arr)):
    count += abs(i + 1 - it)
sys.stdout.write(str(count))