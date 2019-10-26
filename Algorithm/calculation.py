number = []
for i in range(8):
    a = int(input())
    number.append(a)

b = 0
number_1 = []
d = []
for y in range(5):
    c = 0
    for u in range(8):
        if(number[c]<number[u]):
            c = u
    number_1.append(c+1)
    b += number[c]
    number[c] = 0

print(b)
number_1.sort()
print(number_1)

for i in range(5):
    print()
'''   print(number_1[i], end=' ')'''