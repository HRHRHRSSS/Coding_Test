from collections import deque

def solution(people, limit):
    # people 배열 정렬
    people = sorted(people)
    people = deque(people)
    cnt = 0
    # 젤 적 + 젤 많 < limit이면 둘 제거
    while people:
        if len(people)==1:
            cnt+= 1
            break
            
        if people[0]+people[-1] <= limit:
            people.popleft() #가장 가벼운
            people.pop() #가장 무거운
            cnt += 1 #구명보트 카운트
        else:
            people.pop()
            cnt += 1

    return cnt