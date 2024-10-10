# 투포인터 인덱스 사용하기
def solution(people, limit):
    people.sort() 
    left = 0 
    right = len(people) - 1  # 가장 무거운 사람을 가리킴
    cnt = 0
    
    while left <= right:
        # 가장 가벼운 사람과 가장 무거운 사람의 합이 limit 이하인 경우
        if people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람 태우기
        
        # 무거운 사람은 항상 보트에 태움 (조건과 상관없이)
        right -= 1
        cnt += 1  # 보트 한 대 추가
    
    return cnt
