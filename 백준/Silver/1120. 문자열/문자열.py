import sys

A, B = sys.stdin.readline().strip().split()

def solution(A, B):
    if A in B:
        return 0
    
    n = len(B) - len(A) + 1
    min_count = float('inf')  # 최소 변환 횟수를 무한대로 초기화
    
    for i in range(n):
        S = B[i:i + len(A)]
        count = 0
        for s1, a1 in zip(S, A):
            if s1 != a1:
                count += 1
        min_count = min(min_count, count)  # 최소값 업데이트
    
    return min_count

print(solution(A, B))