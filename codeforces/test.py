import sys

s = sys.stdin.readline()
n = len(s) - 1
m = int(sys.stdin.readline().strip())
arr = [int(i) for i in sys.stdin.readline().split()]
for i, it in enumerate(arr):
    # if it>(m/2):
    if it > n / 2:
        arr[i] = n - it + 1
# arr = sorted(arr)
# print(arr)
s = [i for i in s]
s = s[:-1]
# print(arr[:-1])

# for i, it in enumerate(m):
i = 0
while i < len(arr):
    # for i in range(len(arr)):
    if i + 1 < len(arr):
        # s[arr[i]:arr[i+1]]=s[a]
        rev = s[::-1]
        # print(rev)
        s[arr[i] - 1 : arr[i + 1] - 1] = rev[arr[i] - 1 : arr[i + 1] - 1]
        # print(s)
        s[n - arr[i + 1] + 1 : n - arr[i] + 1] = rev[
            n - arr[i + 1] + 1 : n - arr[i] + 1
        ]
        # print(s)
        # swap between [i and i+1)
        # pass
        i += 2
    else:
        rev = s[::-1]
        s[arr[i] - 1 : n - arr[i] + 1] = rev[arr[i] - 1 : n - arr[i] + 1]
        i += 1
        # pass
    # pass

print("".join(s))