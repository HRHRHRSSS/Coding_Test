def solution(citations):
    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations):
        if i >= citation:
            return i
    return len(citations)