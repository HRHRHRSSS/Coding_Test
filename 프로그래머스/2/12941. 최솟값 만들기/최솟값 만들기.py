from collections import deque

def solution(A,B):
    answer = 0
    # A, B를 정렬부터 해줌
    A = sorted(A)
    B = sorted(B, reverse=True)
        
    # 데크 형태로 만들어줌
    A = deque(A)
    B = deque(B)
    
    for i in range(len(A)):
        # 최소값과 최대값 뽑기 + pop으로 제거
        tempA = A.popleft()
        tempB = B.popleft()
        
        # 누적합에 추가
        answer += tempA * tempB
        
    return answer