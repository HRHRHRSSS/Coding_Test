from collections import deque

def solution(priorities, location):
    q = deque([i for i in range(len(priorities))])
    location = q[location] # 구할 값
    priorities = deque(priorities)
    
    answer = []
    while q:
        temp = q.popleft()
        if priorities[0] < max(priorities):
            q.append(temp)
            c = priorities.popleft()
            priorities.append(c)
        else:
            answer.append(temp)
            priorities.popleft()
    
    return answer.index(location)+1