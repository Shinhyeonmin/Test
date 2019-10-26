import collections
queue = collections.deque()

def prime_num(a):
    a = 0
    for i in range(2, int(a/2)+1):
        if(a% i==0):
            a =1
            break
    return a
prime_list = []
b, c = map(int,input().split())
for h in range(b+1,c):
    d = prime_num(h)
    if(d == 0):
        prime_list.append(h)
prime_list.append(b)
prime_list.append(c)

def Calculate(b,c):
    e = b-(b%1000)
    f = b-e-(b%100)
    g = b-(e+f)-(b%10)
    h = b-e-f-g

    i = c-(c%1000)
    j = c-i-(c%100)
    k = c-(i+j)-(c%10)
    l = c-i-j-k

    count=0
    if (e == i):
        count +=1
    if (f == j):
        count += 1
    if (g == k):
        count += 1
    if (h == l):
        count += 1
    if(count >= 3):
        return True
    else:
        return False

matrix=[[b] for h in range(len(prime_list)+1)]
queue.append((0,0, matrix))

while(len(queue) != 0):
    index_num,count,start_point = queue.popleft()

    if(Calculate(prime_list[index_num], c)):
        matrix[start_point].append(c)
        print(matrix[start_point])
        break

    for i in range(index_num+1, len(prime_list)):
        if(Calculate(prime_list[index_num],prime_list[i])):
            if(index_num ==0):
                matrix[i].append(prime_list[i])
                queue.append((i,count+1,i))
            else:
                matrix[start_point].append(prime_list[i])
                queue.append((i,count+1,start_point))