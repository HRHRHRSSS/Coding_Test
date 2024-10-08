from collections import deque

def solution(priorities, location):
    q = deque([i for i in range(len(priorities))])
    location = q[location] # 구할 값
    priorities = deque(priorities)
    
    answer = []
    m = max(priorities)
    while q:
        temp = q.popleft()
        if priorities[0] < m:
            q.append(temp)
            c = priorities.popleft()
            priorities.append(c)
        else:
            answer.append(temp)
            priorities.popleft()
            if priorities: # max는 효율bad. 그래서 pop될때만 업뎃되게
                # priorities가 마지막에는 빈 배열되니까 존재하는 경우만
                m = max(priorities)
    
    return answer.index(location)+1