import sys


def main():
    rl = sys.stdin.readline
    wl = sys.stdout.write

    n, v = [int(i) for i in rl().split()]
    ripel = list()
    numl = list()
    for i in range(n):
        arg1, arg2 = [int(i) for i in rl().split()]
        ripel.append(arg1)
        numl.append(arg2)
    # print(ripel)
    # print(numl)
    zipped = zip(ripel, numl)
    zipped = sorted(zipped)
    # print(type(zipped))
    nripel = list()
    nnuml = list()
    for i in range(len(zipped)):
        sum = zipped[i][1]
        while i < len(zipped) - 1 and zipped[i][0] == zipped[i + 1][0]:
            sum += zipped[i + 1][1]
            i += 1
        nripel.append(zipped[i][0])
        nnuml.append(sum)
    zipped = zip(nripel, nnuml)
    # print(zipped)
    # sett = set(ripel)
    # if len(sett) != len(ripel):
    #     print("Duplicate elements found")
    #     return
    # print(zipped)
    curday = 0
    carry = 0
    sum = 0
    for i in zipped:
        # print(i[0])
        # curday = max(curday, i[0])
        # print("{} {} {} {} {}".format(curday, carry, sum, i[0], i[1]))
        if curday < i[0]:
            sum += min(carry, v)
            # carry = 0
            # curday = i[0]
            sum += min(v, i[1])
            carry = max(0, i[1] - v)
            curday = i[0] + 1
        else:
            # pickedtoday = carry - v
            if carry <= v:
                sum += carry
                left = v - carry
                if left >= i[1]:
                    sum += i[1]
                    carry = 0
                else:
                    sum += left
                    carry = i[1] - left
                # carry = i[1] - (v - carry)
                # curday += 1
                # pass
            else:
                sum += v
                carry = i[1]
                # curday += 1
            curday += 1
    sum += min(carry, v)
    wl("{}".format(sum))


if __name__ == "__main__":
    main()