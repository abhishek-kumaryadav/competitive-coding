import sys

readL = sys.stdin.readline
writeL = sys.stdout.write
n = int(readL().strip())
arr = [int(x) for x in readL().split()]
# print(n, arr)
dicto = {}
for i, it in enumerate(arr):
    if i != it:
        dicto[i] = it
# print(dicto)
flag = 1
if len(dicto) >= 2:
    for it in dicto:
        # print(it.values)
        # print(it, dicto[dicto[it]])
        if it == dicto[dicto[it]]:
            flag = 2
            break
    # flag = 1
else:
    flag = 0
writeL(str(flag + n - len(dicto)))
# flag=2
# print(i)
