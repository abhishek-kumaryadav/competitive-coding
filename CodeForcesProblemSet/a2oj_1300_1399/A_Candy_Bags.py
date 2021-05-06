n = int(input())
sqr = pow(n, 2)
perperson = sqr / (2 * n)
for i in range(1, int(sqr / 2 + 1)):
    print(" ".join([str(i), str(sqr - i + 1)]), end=" ")
    if i % perperson == 0:
        print("")