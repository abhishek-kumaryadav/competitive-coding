x, y = [int(x) for x in input().split()]
newx = x * (abs(x) + abs(y)) / abs(x)
newy = y * (abs(x) + abs(y)) / abs(y)
if newx <= 0:
    print("{} 0 0 {}".format(int(newx), int(newy)))
else:
    print("0 {} {} 0".format(int(newy), int(newx)))
