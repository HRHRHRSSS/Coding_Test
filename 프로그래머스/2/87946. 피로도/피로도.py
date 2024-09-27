from itertools import permutations

def solution(k, dungeons):
    l = len(dungeons)
    # dungeons 순열 arr 저장
    arr = list(permutations(dungeons,l))
    # 조합 하나씩 돌기
    answer_list = []
    for i in arr:
        temp = k # 현재 피로도 저장. 조합마다 초기화
        answer = 0
         # 던전 수 카운트
        for q in i:
            # 인덱스 0은 최소필요피로도 / 인덱스 1은 소모피로도
            if temp >= q[0]:
                temp = temp - q[1]
                answer += 1
        answer_list.append(answer)             
    return max(answer_list)