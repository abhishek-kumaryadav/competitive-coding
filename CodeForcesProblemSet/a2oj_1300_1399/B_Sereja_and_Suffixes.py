import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]

distt = 0
distinct = list()
sett = set()
for i in range(n):
    i = n - 1 - i
    if arr[i] not in sett:
        distt += 1
        sett.add(arr[i])
    distinct.append(distt)


for i in range(m):
    x = int(input().strip())
    sys.stdout.write("{}\n".format(distinct[n - 1 - (x - 1)]))
