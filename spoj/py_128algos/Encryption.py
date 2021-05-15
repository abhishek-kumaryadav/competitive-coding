import sys

# from collections import Counter
vowels = dict()
conso = dict()
for i, it in enumerate(list("aeiou")):
    vowels[it] = i + 1
r_vowels = {value: key for (key, value) in vowels.items()}
for i, it in enumerate(list("bcdfghjklmnpqrstvwxyz")):
    conso[it] = i + 1
r_conso = {value: key for (key, value) in conso.items()}
# print(vowels, r_vowels, conso, r_conso)


t = int(sys.stdin.readline().strip())
for tc in range(t):
    s = list(sys.stdin.readline().strip().split()[0])
    # print(s)
    dictto = dict()
    rlist = list()
    for ch in s:
        if ch in dictto:
            dictto[ch] += 1
        else:
            dictto[ch] = 0
        if ch in "aeiou":
            occ = 5 * dictto[ch] + vowels[ch]
            occ %= 21
            if occ == 0:
                occ = 21
            # print(occ, r_conso[occ])
            rlist.append(r_conso[occ])
            # print(occ)
        else:
            occ = 21 * dictto[ch] + conso[ch]
            occ %= 5
            if occ == 0:
                occ = 5
            # print(occ, r_vowels[occ])
            rlist.append(r_vowels[occ])
            # pass
            # print(occ)
    # ctr=Counter(s)
    rlist.append("\n")
    sys.stdout.write("".join(rlist))