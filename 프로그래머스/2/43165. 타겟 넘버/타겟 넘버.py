from itertools import product

def solution(numbers, target):
    combination = product(['+','-'], repeat=len(numbers))
    
    answer = 0
    for com in combination:
        temp = 0 #연산 결과 저장
        for num, sign in zip(numbers,com):
            if sign == '+':
                temp += num
            elif sign == '-':
                temp -= num
        if temp == target:
            answer += 1
    return answer