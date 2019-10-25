a = int(input())
number_list = input()
number_list = number_list.split(' ')
number = input()
number = number.split(' ')

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])
for y in range(len(number)):
    number[y] = int(number[y])

for i in range(len(number_list)):
    for j in range(len(number_list)-i-1):
        if(number_list[j]>number_list[j+1]):
            number_list[j],number_list[j+1] = number_list[j+1],number_list[j]

for u in range(len(number)):
    for v in range(len(number)-u-1):
        if(number[v]<number[v+1]):
            number[v],number[v+1] = number[v+1],number[v]

f = 0
for h in range(len(number_list)):
    z = number_list[h]*number[h]
    f = f+z
print(f)