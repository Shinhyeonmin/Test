M = int(input())
N = int(input())
a = 0
b = 0
flag = 0
for i in range(1,100):
    c = i*i
    if(M<=c and c<=N):
        a = a+c
        if(flag == 0):
            b = c
            flag = flag+1
if (a == 0 or b == 0):
    print(-1)
else:
    print(a)
    print(b)