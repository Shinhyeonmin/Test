a, b = map(int, input().split())
c = 0
print("%d %d" % (a, b), end=' ')
while (True):
    c = a - b
    if (c >= 0):
        a = b
        b = c

    if (c <= -1):
        break
    print("%d " % c, end='')