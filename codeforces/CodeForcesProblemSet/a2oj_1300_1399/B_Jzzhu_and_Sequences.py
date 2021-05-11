import sys

modulo = int(1e9) + 7
x, y = [int(i) % modulo for i in sys.stdin.readline().split()]
n = int(sys.stdin.readline().strip())
out = x
# if x == 0 or y == 0:
#     out = (x + y) % modulo
# pass

# else:
if n == 2:
    out = y
    out %= modulo
elif n > 2:
    while n > 2:
        if x == 0 or y == 0:
            out = (x + y) % modulo
            break
        out = y - x
        # if out < 0:
        #     out += modulo
        out %= modulo
        # print(out)
        # if out
        x = y % modulo
        y = out
        n -= 1
sys.stdout.write("{}".format(out))
