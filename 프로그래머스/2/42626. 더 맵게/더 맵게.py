import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # 힙 생성(최소힙)
    cnt = 0
    while len(scoville)>1 and scoville[0]<K:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new = min1 + (min2*2)
        heapq.heappush(scoville,new)
        cnt+=1
    
    if scoville[0] >= K:
        return cnt
    else:
        return -1