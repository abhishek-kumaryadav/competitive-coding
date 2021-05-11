import sys


def main():
    rl = sys.stdin.readline
    wl = sys.stdout.write
    t = int(rl().strip())
    modulo = int(1e9) + 7
    arr = list()
    val = 1
    arr.append(1)
    for i in range(int(1e5)):
        val *= 2
        val %= modulo
        arr.append(val)
    for i in range(t):
        n = int(rl().strip())
        # out = 1
        # for j in range(n - 1):
        #     out *= 2
        #     out %= modulo
        # p = 200
        # while n > p:
        #     out *= pow(2, p)
        #     out %= modulo
        #     n -= p
        # out *= pow(2, n - 1)
        # out %= modulo
        # wl("{}\n".format((int)(pow(2, n - 1)) % int(1000000000 + 7)))
        wl("{}\n".format(int(arr[n - 1])))
        # for k in range(100):
        # wl(str("{}: {:}\n".format(k, k ^ k + 1 == k + 2 ^ k + 3)))


if __name__ == "__main__":
    main()