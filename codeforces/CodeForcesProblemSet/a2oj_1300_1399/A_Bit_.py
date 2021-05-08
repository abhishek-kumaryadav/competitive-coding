x = int(input())
val = 0
for i in range(0, x):
    strr = input()
    if "++" in strr:
        val = val + 1
    else:
        val = val - 1
print(val)