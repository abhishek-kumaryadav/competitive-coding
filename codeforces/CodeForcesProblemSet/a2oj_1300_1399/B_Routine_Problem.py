import sys

a, b, c, d = [int(i) for i in sys.stdin.readline().split()]

if c / d > a / b:
    val1 = int(b * c - d * a)
    val2 = int(b * c)
    if val1 == 0:
        val2 = 1
    i = 2
    while i < val2:
        if val1 % i == 0 and val2 % i == 0:
            val1 /= i
            val2 /= i
            i = 2
        else:
            i += 1
    # if val2%val1==0:

    sys.stdout.write("{}/{}".format(int(val1), int(val2)))
else:

    val1 = int(-b * c + d * a)
    val2 = int(a * d)
    if val1 == 0:
        val2 = 1
    i = 2
    while i < val2:
        if val1 % i == 0 and val2 % i == 0:
            val1 /= i
            val2 /= i
            i = 2
        else:
            i += 1
    sys.stdout.write("{}/{}".format(int(val1), int(val2)))
