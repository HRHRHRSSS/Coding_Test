def solution(k, tangerine):
    answer = 0
    a = {}
    # 주어진 리스트 tangerine에서 각 귤의 개수를 세어줌
    for i in tangerine:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    # 딕셔너리 값을 기준으로 내림차순 정렬
    a = dict(sorted(a.items(), key=lambda x:x[1], reverse = True))
    # 정렬된 value 값을 상자에 담을 수 있는 귤 개수(k)에서 빼주며 반복
    # 정렬된 순서대로 귤을 선택하면서 k를 초과한 순간 선택 멈춤
    # 이 때 선택된 귤의 종류 수 반환!
    for i in a:
        if k<=0:
            return answer
        k-=a[i]
        answer+=1
    return answer