def solution(k, input_list):
    answer = []
    temp = []
    for i in range(k+1):
        answer.append(0)
    for y in range(len(input_list)):
        temp.append(0)
        if(answer[input_list[y]]==0):
            answer[input_list[y]]=1
            temp[y] = input_list[y]
        else:
            for j in range(1, len(answer)):
                if(answer[j] == 0):
                    print("j is value", j)
                    temp[y] = j
                    answer[j] = 1
                    break
    print(temp)
    return temp

solution(1, [1])