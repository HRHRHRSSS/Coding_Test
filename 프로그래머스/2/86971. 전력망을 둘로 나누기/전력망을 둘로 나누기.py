import copy
from collections import deque

def solution(n, wires):
    graph = {i: [] for i in range(1,n+1)}
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    min_diff = float('inf') #일단 무한대로 초기화
    
    # 하나의 전선 끊고 각각의 전력망 크기 계산
    for v1,v2 in wires:
        
        # 전선 끊기
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        # BFS나 DFS를 통해 한쪽의 송전탑 개수 구하기
        count1 = bfs(graph, v1, n)
        count2 = n - count1 # 나머지 송전탑 개수
        
        # 두 전력망 차이 계산
        min_diff = min(min_diff, abs(count1-count2))
        
        #전선 복구
        graph[v1].append(v2)
        graph[v2].append(v1)
    return min_diff


def bfs(graph, start, n):
    visited = [False]*(n+1)
    visited[start]=True
    q = deque([start])
    count = 1
    
    while q:
        temp = q.popleft()
        for next in graph[temp]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                count += 1
    return count