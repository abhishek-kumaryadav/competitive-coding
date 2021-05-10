import sys


def main():
    rl = sys.stdin.readline
    wl = sys.stdout.write
    t = int(rl().strip())
    for i in range(t):
        arr = list()
        for j in range(3):
            temp = rl().split()[0]
            arr.append(temp)
        # print(arr[0][0])
        count = 0
        for i in range(3):
            for j in range(3):
                if arr[i][j] == "X":
                    count += 1
                elif arr[i][j] == "O":
                    count -= 1
        # print(count)
        


if __name__ == "__main__":
    main()