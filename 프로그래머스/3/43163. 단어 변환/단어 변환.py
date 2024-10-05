from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    return bfs(begin, target, words)

def bfs(begin, target, words):
    
    q = deque()
    q.append([begin, 0]) #시작 단어와 단계 0으로 초기화
    
    while q:
        now, step = q.popleft()
        
        if now == target:
            return step
        
        # 단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            diff = 0
            for c1, c2 in zip(now, word):
                if c1 != c2:
                    diff += 1
                    
            if diff == 1:
                q.append([word, step+1])