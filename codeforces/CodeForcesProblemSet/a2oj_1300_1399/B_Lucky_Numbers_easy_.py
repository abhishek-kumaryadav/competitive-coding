import sys


def is_suplucky(num):
    # return True
    # print(len(str(num)))
    # return True
    if len(str(num)) % 2 == 1:
        return False

    s4 = 0
    s7 = 0
    while num > 0:
        # print(num)
        # break
        g = num % 10
        if g == 4:
            s4 += 1
        elif g == 7:
            s7 += 1
        else:
            return False
        num = num / 10
    return True
    if s4 == s7:
        return True
    else:
        return False
    # print("RAAN")


def main():
    n = int(sys.stdin.readline())
    siz = len(list(str(n)))
    # flag = 0
    # while not flag:
    if siz % 2 == 0:
        if is_suplucky(n):
            sys.stdout.write("{}".format(n))
            # pass
        else:
            maxnum = ["7" if i < siz / 2 else "4" for i in range(siz)]
            if n < int("".join(maxnum)):
                while not is_suplucky(n):
                    n += 1
                sys.stdout.write(str(n))
                # pass
            else:
                siz += 2
                mynum = ["4" if i < siz / 2 else "7" for i in range(siz)]
                sys.stdout.write("".join(mynum))
            # mynum = 0
            # while n>=0:
            # for i in list(str(n)):
            # print(i)
            # digit = int(i)
            # if digit<=4:
    else:
        siz += 1
        mynum = 0
        for i in range(int(siz / 2)):
            mynum = mynum * 10 + 4
        mynum = ["4" if i < siz / 2 else "7" for i in range(siz)]
        sys.stdout.write("".join(mynum))
    # pass
    # n += 1


if __name__ == "__main__":
    main()
