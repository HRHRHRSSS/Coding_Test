def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0:
            column = i
            # column이 주어졌을 때 row 
            row = yellow//column
            if ((row+column)*2+4)==brown:
                if row < column:
                    row, column = column, row
                answer = [row+2,column+2]
    return answer