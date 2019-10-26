room_num = input()

b = [0,1,2,3,4,5,6,7,8,9]
matrix = [0 for i in range(10)]


for i in range(len(room_num)):
    if(room_num[i] == '0'):
        matrix[0] = matrix[0]+1
    elif(room_num[i] == '1'):
        matrix[1] = matrix[1] + 1
    elif (room_num[i] == '2'):
        matrix[2] = matrix[2] + 1
    elif (room_num[i] == '3'):
        matrix[3] = matrix[3] + 1
    elif (room_num[i] == '4'):
        matrix[4] = matrix[4] + 1
    elif (room_num[i] == '5'):
        matrix[5] = matrix[5] + 1
    elif (room_num[i] == '6'):
        matrix[6] = matrix[6] + 1
    elif (room_num[i] == '7'):
        matrix[7] = matrix[7] + 1
    elif (room_num[i] == '8'):
        matrix[8] = matrix[8] + 1
    elif (room_num[i] == '9'):
        matrix[9] = matrix[9] + 1

matrix[6] = int((matrix[6]+matrix[9])/2+0.5)
matrix[9] = 0

max = matrix[0]
for u in range(len(matrix)):
    if(matrix[u]>max):
        max = matrix[u]
print(max)