from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for s,d in tickets:
        graph[s].append(d)
        
    # 알파벳 순서가 앞서는 경로 찾기 위해
    for key in graph:
        graph[key].sort(reverse=True)
    # pop으로 꺼내야하니까 역순으로 정렬
    
    answer = []
    def dfs(current):
        while graph[current]:
            next = graph[current].pop()
            dfs(next)
        answer.append(current)
    
    dfs("ICN") # 항상 ICN에서 출발
    return answer[::-1]