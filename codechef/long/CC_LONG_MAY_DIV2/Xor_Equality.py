import sys


def main():
    rl = sys.stdin.readline
    wl = sys.stdout.write
    t = int(rl().strip())
    for i in range(t):
        n = int(rl().strip())
        wl("{}\n".format((int)(pow(2, n - 1)) % int(1000000000 + 7)))
        # for k in range(100):
        # wl(str("{}: {:}\n".format(k, k ^ k + 1 == k + 2 ^ k + 3)))


if __name__ == "__main__":
    main()