a, b, c = map(int, input().split())

if (a > b and a > c):
    if ((a * a) == (b * b) + (c * c)):
        print('right')
    elif ((a * a) < (b * b) + (c * c)):
        print('acute')
    else:
        print('obtuse')
elif (b > a and b > c):
    if ((b * b) == (a * a) + (c * c)):
        print('right')
    elif ((b * b) < (a * a) + (c * c)):
        print('acute')
    else:
        print('obtuse')
else:
    if ((c * c) == (b * b) + (a * a)):
        print('right')
    elif ((c * c) < (b * b) + (a * a)):
        print('acute')
    else:
        print('obtuse')