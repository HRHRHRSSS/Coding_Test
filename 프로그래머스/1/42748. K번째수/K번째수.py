def solution(array, commands):
    result = []
    for p in commands:
        i,j,k = p[0],p[1],p[2]
        #슬라이싱 부분을 정확히 생각해야 할듯
        list = array[i-1:j]
        list = sorted(list)
        result.append(list[k-1])
    return result