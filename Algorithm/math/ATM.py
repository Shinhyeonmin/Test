a = int(input())

number_list = input()
number_list = number_list.split(' ')

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])

for i in range(len(number_list)):

    for j in range(len(number_list)-i-1):
        if(number_list[j]>number_list[j+1]):
            number_list[j],number_list[j+1] = number_list[j+1],number_list[j]

total =0
stack = 0
for i in range(len(number_list)):
    stack = number_list[i] + stack
    total = total +stack

print(total)
