a = int(input())
matrix = []
alpa =[]
for u in range(a):
    alpa.append(input())
for h in range(len(alpa)):
    s=int(alpa[h])
    if(s<4):
        if(s == 1):
            print(1)
        elif(s == 2):
            print(2)
        elif(s == 3):
            print(4)
    else:
        for i in range(s+1):
            matrix.append(0)
        matrix[0] = 1
        matrix[1] = 1
        matrix[2] = 2
        matrix[3] = 4
        for i in range(3,s+1):
            matrix[i] = matrix[i-1]+matrix[i-2]+matrix[i-3]
        print(matrix[s])