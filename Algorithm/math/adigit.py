a, b, c, d, e, f, g = map(int, input().split())
h = [a, b, c, d, e, f, g]

i = 0
j = 0
k = 0

for t in range(len(h)):

    if (h[t] < 10):
        i = i + h[t]
    elif (h[t] >= 10 and h[t] < 100):
        j = j + h[t]
    elif (h[t] >= 100 and h[t] < 1000):
        k = k + h[t]
print(i, j, k)