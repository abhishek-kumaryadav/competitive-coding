str1 = input().strip()
str2 = input().strip()
a = []
# count=0
if len(str1) == len(str2):
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            a.append(str1[i])
            a.append(str2[i])
        # b=str2[i]
        # count+=1
    # pass
if len(a) == 4 and a[0] == a[3] and a[1] == a[2]:
    print("YES")
else:
    print("NO")