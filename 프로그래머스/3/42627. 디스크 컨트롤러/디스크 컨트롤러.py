import heapq

def solution(jobs):
    jobs.sort() #요청시간순으로 정렬
    count, last = 0,-1
    
    wait = [] #지금 수행할 수 있는 작업들 저장(최소힙) - 작업 소요시간(t)기준 최소힙
    time = jobs[0][0] #첫번째 작업의 요청시간
    answer = 0 #반환할 값
    
    while count < len(jobs):
        # 현재 진행되고 있는 작업과 겹치는지 확인
        for s, t in jobs:
            # 다음 작업이 지금 수행 중인 작업의 사이에 있다면
            if last < s <= time:
                heapq.heappush(wait,(t,s)) # 그 작업을 대기열에 넣어(소요시간 기준이니까 t를 앞에)
        
        if wait: # 대기열에 작업이 있으면
            last = time #업데이트
            term, start = heapq.heappop(wait)
            count += 1 #작업 하나 수행~
            time += term # 소요시간만큼 더하기
            answer += (time - start) # 총 소요시간 구하기 위함
        else:
            time += 1 #wait안에 아무도 없다면 time 증가시키면서 기다리기
            
    return answer//len(jobs) #평균을 구해야 함