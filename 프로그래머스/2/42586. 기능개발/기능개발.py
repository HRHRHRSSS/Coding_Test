from math import ceil
from collections import deque

def solution(progresses, speeds):
    remaining = [100-x for x in progresses]
    
    # remaining을 speeds로 나눠야함. 근데 이제 ceil을 곁들인..
    days = []
    for t,d in zip(remaining,speeds):
        days.append(ceil(t/d))
    days = deque(days)
    
    answer = []
    while days:
        cnt=1
        temp = days.popleft()
        while days and days[0] <= temp:
            cnt += 1
            days.popleft()
        answer.append(cnt)
    
    return answer