import sys

rl = sys.stdin.readline
wl = sys.stdout.write
_str = rl().strip()
_list = list()
_list.append(0)
_count = 0
for i in range(len(_str) - 1):
    if _str[i] == _str[i + 1]:
        _count += 1
    _list.append(_count)
# print(_list)
m = int(rl())

for i in range(m):
    l, r = [int(i) for i in rl().split()]
    wl("".join([str(_list[r - 1] - _list[l - 1]), "\n"]))
