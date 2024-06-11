def solution(N, A, B):
    # 0-based index로 변환
    A -= 1
    B -= 1
    round = 0
    
    # A와 B가 같아질 때까지 라운드를 진행
    while A != B:
        A //= 2
        B //= 2
        round += 1
        
    return round