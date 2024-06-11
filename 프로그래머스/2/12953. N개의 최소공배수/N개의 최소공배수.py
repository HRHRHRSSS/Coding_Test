import math

def findlcm(a,b):
    l = (a*b)//math.gcd(a,b)
    return l

def solution(arr):
    # 0부터니까 범위 -1 !
    for i in range(len(arr)-1):
    
        if i==0: # 젤 처음은 0과 1의 최소공배수 구하기
            temp = findlcm(arr[0],arr[1])
        else: #나머지는 구해진 최소공배수와 구하기
            temp = findlcm(temp, arr[i+1])
        
    return temp