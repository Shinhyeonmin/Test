s = input()

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y','z']
answer = []
for i in range(len(alphabet)):
    for u in range(len(s)):
        if(s[i] == alphabet[u]):
            alphabet[u] = u-1
            
        else:
            alphabet[u] = -1
    print(alphabet)