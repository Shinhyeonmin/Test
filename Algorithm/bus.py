a = int(input())

temp = []
for i in range(a):
    temp.append(int(input()))
b=[1]
for i in range(1,31):
    value = 1
    for j in range(i):
        value=value*2
    b.append(b[i-1]+value)
for i in range(len(temp)):
    c = temp[i]
    print(b[c-1])

'''
class Baekjoon():
    def __init__(self):
        self.a =0
        self.temp = []
        self.b=[1]

    def input_value(self):
        self.a = int(input())
        for i in range(self.a):
            c = int(input())
            self.temp.append(c)

    def problem_solve(self):
        for i in range(1,32):
            value =1

            for j in range(i):
                value=value*2
            self.b.append(self.b[i-1]+value)
    def print_value(self):
        for i in range(len(self.temp)):
            c = self.temp[i]
            print(self.b[c-1])

x = Baekjoon()
x.input_value()
x.problem_solve()
x.print_value()
'''