import heapq

def solution(operations):
    answer = []
    heapq.heapify(answer)
    for order in operations:
        if order[0] == "I":
            heapq.heappush(answer,int(order[2:]))

        elif order == "D 1" and len(answer)>0:
            answer.sort() 
            answer.pop()
        
        elif order == "D -1" and len(answer)>0:
            heapq.heappop(answer)

    answer.sort()
    if len(answer)>0:
        return [answer[-1], answer[0]]
    else:
        return [0,0]