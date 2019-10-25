temp = []

while(True):

    a = int(input())

    if(a == -1):
        break
    else:
        temp.append(a)
def measure(e,a):
    for j in range(1,int(e/2)+1):
        if(e%j == 0):
            a.append(j)
    return a

b=[]
for e in temp:
    a =[]
    a = measure(e,a)

    total = 0
    temp_str = []
    temp_str.append(str(e))
    temp_str.append(' = ')
    for i in a:
        total += i
        temp_str.append(str(i))
        temp_str.append(" + ")

    del temp_str[len(temp_str)-1]
    str1=''.join(temp_str)

    if(total == e):
        b.append(str1)
    else:
        b.append("%d is NOT perfect."%e)

for i in b:
    print(i)