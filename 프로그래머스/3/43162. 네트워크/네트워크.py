from collections import deque

def solution(n, computers):
    visited = [False] * n # 방문한 컴퓨터 기록
    count = 0 #네트워크 개수 카운트
    
    for i in range(n):
        if not visited[i]: #아직 방문x 컴퓨터면
            bfs(i,computers,visited) #bfs호출
            count += 1 # 새로운 네트워크 발견 시 카운트
    return count

def bfs(start, computers, visited):
    q = deque([start]) # 시작컴퓨터를 큐에 추가
    visited[start] = True #방문처리
    
    while q:
        cur = q.popleft()
        for next in range(len(computers)):
            if not visited[next] and computers[cur][next]:
                visited[next]=True
                q.append(next)