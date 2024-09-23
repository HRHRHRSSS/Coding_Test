import math
from itertools import permutations

def Primecheck(n):
    if n < 2:
        return False
    # sqrt를 썼을 때 소수점이 있을 수 있으므로 int로 바꿔줘야 한다
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    temp = []
    answer = []
    num_list = list(numbers)
    
    for i in range(1, len(num_list)+1):
        temp += list(permutations(num_list, i))
    
    # 조합으로 얻은 애들 붙이기
    num_list2 = [int(''.join(t)) for t in temp]
    
    for i in num_list2:
        if Primecheck(i):
            answer.append(i)
    
    return len(set(answer))