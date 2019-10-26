T = int(input())

number_list = []

for i in range(T):
    b,c=map(int,input().split(' '))
    number_list.append([b,c])

for u in range(T):
    print(number_list[u][1]-number_list[u][0]+2)
