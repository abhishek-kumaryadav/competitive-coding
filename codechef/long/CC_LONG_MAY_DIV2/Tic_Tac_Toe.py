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
        for k in range(3):
            for j in range(3):
                if arr[k][j] == "X":
                    count += 1
                elif arr[k][j] == "O":
                    count -= 1
        # print(count)
        bol = list()
        countt = {"X": 0, "O": 0}
        # print(countt["X"], countt["O"])
        for j in range(3):
            if arr[j][0] == arr[j][1] and arr[j][1] == arr[j][2]:
                bol.append((True, arr[j][0]))
                # print(countt[arr[j][]])
                try:
                    count[arr[j][0]] = countt[arr[j][0]] + 1
                except:
                    pass
            else:
                bol.append((False, ""))
        for j in range(3):
            if arr[0][j] == arr[1][j] and arr[1][j] == arr[2][j]:
                bol.append((True, arr[0][j]))
                try:
                    countt[arr[0][j]] = countt[arr[0][j]] + 1
                except:
                    pass
            else:
                bol.append((False, ""))
        if arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2]:
            bol.append((True, arr[0][0]))
            try:
                countt[arr[0][0]] = countt[arr[0][0]] + 1
            except:
                pass
        else:
            bol.append((False, ""))
        if arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0]:
            bol.append((True, arr[0][2]))
            try:
                countt[arr[0][2]] = countt[arr[0][2]] + 1
            except:
                pass
        else:
            bol.append((False, ""))
        print(bol)
        print(countt)
        print(count)


if __name__ == "__main__":
    main()