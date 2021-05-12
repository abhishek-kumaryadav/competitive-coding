import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = [int(i) for i in sys.stdin.readline().split()]
    out = n - 1
    for i in range(2, n):
        for j in range(i + 1, n + 1):
            if (m % i) % j == (m % j) % i:
                print(i, j)
            if (m // i) // j == (m // j) // i:
                print(i, j, 0)
                out += 1
            print("\n")
    sys.stdout.write("{}\n".format(out))
