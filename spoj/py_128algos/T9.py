import sys
import math
import bisect
from sys import prefix, stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from functools import lru_cache

sys.setrecursionlimit(100000000)

int_r = lambda: int(sys.stdin.readline())
str_r = lambda: sys.stdin.readline().strip()
intList_r = lambda: list(map(int, sys.stdin.readline().strip().split()))
strList_r = lambda: list(sys.stdin.readline().strip())
jn = lambda x, l: x.join(map(str, l))
mul = lambda: map(int, sys.stdin.readline().strip().split())
mulf = lambda: map(float, sys.stdin.readline().strip().split())
ceil = lambda x: int(x) if (x == int(x)) else int(x) + 1
ceildiv = lambda x, d: x // d if (x % d == 0) else x // d + 1
flush = lambda: stdout.flush()
outStr = lambda x: stdout.write(str(x))
mod = 1000000007


t9 = list("22233344455566677778889999")


def letter_to_digit(x):
    assert "a" <= x <= "z"
    # print(ord["a"])
    return t9[ord(x) - ord("a")]


def word_to_digits(word):
    return "".join(map(letter_to_digit, word))


def predict_text(dic):
    total_weights = dict()
    for word, weight in dic.items():
        prefix = ""
        for x in word:
            prefix += x
            if prefix in total_weights:
                total_weights[prefix] += weight
            else:
                total_weights[prefix] = weight
    code_to_prefix = dict()
    for prefix in total_weights:
        code = word_to_digits(prefix)
        # Select one for every code
        if (
            code not in code_to_prefix
            or total_weights[code_to_prefix[code]] < total_weights[prefix]
        ):
            code_to_prefix[code] = prefix
    return code_to_prefix


def main():
    testcases = int_r()

    for t_c in range(testcases):
        words_weight = {}
        # query = []
        w = int_r()
        for _ in range(w):
            x, y = str_r().split()
            words_weight[x] = y
        code_to_prefix = predict_text(words_weight)
        m = int_r()
        # print(code_to_prefix)
        # outStr("Scenario #1:\n")
        for _ in range(m):
            query = str_r()
            # print(query)
            if query[:-1] in code_to_prefix:
                outStr("{}\n".format(code_to_prefix[query[:-1]]))
            else:
                outStr("MANUALLY\n")
            # query.append(int(str_r()))

        # print(words_weight, query)


if __name__ == "__main__":
    main()