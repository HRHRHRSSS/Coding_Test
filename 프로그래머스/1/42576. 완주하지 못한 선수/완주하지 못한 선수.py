from collections import Counter

def solution(participant, completion):
    
    P = Counter(participant)
    C = Counter(completion)
    answer = P - C

    return list(answer.keys())[0]