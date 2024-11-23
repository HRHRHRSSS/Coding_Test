import heapq
import sys

lst = []
heapq.heapify(lst)

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    if m!=0:
        heapq.heappush(lst,m) # 0이 아니면 값 추가
    else:
        if lst:
            min = heapq.heappop(lst)
            print(min)
        else:
            print(0)