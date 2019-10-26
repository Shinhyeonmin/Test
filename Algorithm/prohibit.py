a = input()
temp='CAMBRIDGE'
b = []
c = 0
for u in range(len(a)):
    c=0
    for i in range(len(temp)):
        if(a[u]==temp[i]):
            c = 1
    if(c == 0):
        b.append(a[u])
b = ''.join(b)
print(b)