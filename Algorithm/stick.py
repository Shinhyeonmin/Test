a = int(input())

stick = []
large = 64
num = 0

if(a == 64):
    print(1)
elif(a<64):
    for i in range(a):
        if(a != large/2):
            large = large/2
            stick.append(large)

print(len(stick))
