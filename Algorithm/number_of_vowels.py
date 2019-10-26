a =input()
list=['a','e','i','o','u']
b=0
for u in range(len(list)):
    for i in range(len(a)):
        if(a[i]==list[u]):
            b = b+1
print(b)