import sys
from collections import Counter

# print(s)


# def ispal(string, n):
#     for i in range(n // 2):
#         if string[i] != string[n - 1 - i]:
#             return False
#     return True


def main():
    s = [x for x in sys.stdin.readline().strip()]
    ctr = Counter(s)
    sett = set(s)
    n = len(s)
    elements = dict(ctr)
    # print(elements)
    sum = 0
    odds = {}
    for keys in elements:
        if elements[keys] % 2 == 0:
            sum += elements[keys]
            # elements.pop(keys)
        else:
            odds[keys] = elements[keys]
    # print(odds, sum)
    if len(odds) <= 1:
        print("First")
    else:
        sorodd = sorted(odds, key=odds.get)
        sum += 1
        for i in sorodd[2:]:
            sum += elements[i]
        if sum % 2 == 1:
            sys.stdout.write("Second")
        else:
            sys.stdout.write("First")


if __name__ == "__main__":
    main()