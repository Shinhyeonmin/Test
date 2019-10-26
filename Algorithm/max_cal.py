def solution(arr):
    answer = 1
    temp = []
    i = 0

    while(True):
        if(i>=len(arr)):
            break

        if(arr[i] == 1):

            if(i==0):
                temp.append(arr[0]+arr[1])
                i += 2
            elif(i == len(arr)-1):
                temp[len(temp)-1] = temp[len(temp)-1]+arr[i]
                i += 1
            else:

                if(temp[len(temp)-1]<arr[i+1]):
                    temp[len(temp)-1] = temp[len(temp)-1]+arr[i]
                    i += 1
                else:
                    temp.append(arr[i]+arr[i+1])
                    i += 2

        else:
            temp.append(arr[i])
            i += 1
    print(arr)
    print(temp)
    for num in temp:
        answer *= num

    return answer


print(solution([1, 2, 1, 2]))