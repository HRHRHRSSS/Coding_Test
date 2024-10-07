def solution(array, commands):
    answer = []
    for i,q,k in commands:
        temp = array[i-1:q]
        temp = sorted(temp)
        answer.append(temp[k-1])
    return answer