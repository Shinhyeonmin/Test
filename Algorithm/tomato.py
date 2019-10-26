import collections

queue = collections.deque()

a,b = map(int,input().split())

matrix = []
for c in range(b):
    d = list(map(int,input().split()))
    matrix.append(d)

for x in range(b):
    for y in range(a):
        if(matrix[x][y] == 1):
            queue.append((x,y,0))

arrow = [(0,1), (1,0),(-1,0),(0,-1)]
while(len(queue) != 0):
    x, y ,count= queue.popleft()
    for t_x,t_y in arrow:
        c_x = x+t_x
        c_y = y+t_y

        if(c_x <b and c_x>=0 and c_y <a and c_y>=0):

            if(matrix[c_x][c_y] != -1 and matrix[c_x][c_y] == 0):
                matrix[c_x][c_y] = 100
                queue.append((c_x, c_y,count+1))
flag = 0
for x in range(b):
    for y in range(a):
        if(matrix[x][y] == 0):
            flag = 1
            break
if(flag == 1):
    print(-1)
else:
    print(count)