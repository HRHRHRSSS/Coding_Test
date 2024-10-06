from collections import defaultdict

def solution(clothes):
    clothes_map = defaultdict(list)
    for p1,p2 in clothes:
        clothes_map[p2].append(p1)
    
    answer = 1 #곱셈을 위한 초기값 1
    for c in clothes_map:
        # 카테고리별 입지 않는 경우 추가(+1)
        answer *= (len(clothes_map[c])+1)
    # 최소 1개는 입어야하기 때문에
    # 아예 아무것도 입지 않은 경우 -1
    return answer-1